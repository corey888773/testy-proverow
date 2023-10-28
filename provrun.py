import subprocess
import os

from customerrors import RFGError, RFGTimeoutError

class ProverRunner:
    def __init__(self, prover, input_file):
        # remember parameters for later use
        self.input_file = input_file
        self.prover = prover

    def performMeasurements(self, output_file):
        try:
            # run the prover with given file
            self.runProver(output_file=output_file)
        except subprocess.TimeoutExpired:
            # change the error type so that it prints in a desired way
            raise RFGTimeoutError(output_file)
        # return the measurements of prover execution
        return self.getMeasuresFromOutputFile()

    def runProver(self, output_file=None, time_limit=300):
        # if prover name is given, save it
        if output_file != None:
            self.output_file = output_file
        # else replace it with a generic name
        else:
            self.output_file = "prover_output.out"

        if self.prover == 'prover9':
            # run Prover9 with search time limit (parameter -t) and using a file (parameter -f), redirect the output to a file
            command = ["prover9 -t", str(time_limit), "-f", self.input_file, ">", self.output_file]
            command = " ".join(command)
            # execute the command in a new process, with additional time_limit for the entire execution
            subprocess.call(command, shell=True, timeout=time_limit)
        elif self.prover == 'spass':
            # run SPASS Prover with time limit (parameter -TimeLimit), redirect the output to a file
            command = [f'SPASS -TimeLimit={str(time_limit)}', self.input_file, ">", self.output_file]
            command = " ".join(command)
            # execute the command in a new process
            subprocess.call(command, shell=True)
        elif self.prover == 'cvc4':
            command = ["cvc4", "--lang", "smt", "--stats", "--tlimit", str(time_limit),self.input_file, ">", self.output_file, "2>>", self.output_file]
            command = " ".join(command)
            # execute the command in a new process
            subprocess.call(command, shell=True)
        elif self.prover == 'z3':
            command = ["python3", self.input_file, ">", self.output_file]
            command = " ".join(command)
            # execute the command in a new process
            subprocess.call(command, shell=True)
        elif self.prover == 'vampire':
            command = ["~/solvers/vampire/bin/vampire_rel", "--mode", "casc_sat", "-t", str(time_limit), "<", self.input_file, ">", self.output_file]
            command = " ".join(command)
            # execute the command in a new process
            subprocess.call(command, shell=True)
        elif self.prover == 'snake':
            command = ["~/solvers/snake/bin/vampire_rel --input_syntax tptp --proof off --output_axiom_names on --mode portfolio --schedule snake_tptp_uns --cores 1 -m 12000","-t", str(time_limit), self.input_file, ">", self.output_file]
            command = " ".join(command)
            # execute the command in a new process
            subprocess.call(command, shell=True)

    def getMeasuresFromOutputFile(self):
        total_time = 0      # in seconds
        total_memory = 0    # in MB
        sat = None          # proving result

        # set the initial state
        if self.prover == 'prover9':
            state = "P9_FindStatisticsBlock"
        elif self.prover == 'spass':
            state = "SP_FindResult"
        elif self.prover in ["vampire","snake"]:
            state = "VS_FindResult"
        elif self.prover == 'z3':
            state = "Z3_FindResult"
        elif self.prover == 'cvc4':
            state = "CV_FindResult"

        # count valid lines in output file to see if there were any
        valid_line_counter = 0

        with open(self.output_file,'r') as log:
            for line in log:
                # if beginning of the line doesn't match any of demanded patterns, skip it to speed up the search
                if not line.startswith(('=','%','G','M','U',"SPASS",'\t',' ','u','s','d')):
                    continue
                # else line might be used, count it as valid
                valid_line_counter += 1
                if state == "P9_FindStatisticsBlock":
                    # look for the beggining of Prover9 statistics block
                    if line == "============================== STATISTICS ============================\n":
                        # proceed to reading the result
                        state = "P9_ReadSat"
                elif state == "P9_ReadSat":
                    # the result line looks somewhat like "Given=0. Generated=1. Kept=0. proofs=1."
                    # get the number of proofs
                    sat_report = line.split(" ")
                    proofs_statistic = sat_report[3].split("=")
                    if int(proofs_statistic[1][0]) == 0:
                        # if there are none, the formula is satisfiable or there was an error, set it as satisfiable for now
                        sat = "True"
                    else:
                        # if there are proofs, the formula is unsatisfiable
                        sat = "False"
                    # proceed to reading the memory usage
                    state = "P9_FindMegabytes"
                elif state == "P9_FindMegabytes":
                    # the memory line looks somewhat like "Megabytes=0.04."
                    # get the number of megabytes
                    if line.startswith("Megabytes"):
                        mem_report = line.split("=")
                        # add it to memory result
                        total_memory += float(mem_report[1][:-2])
                        if total_memory > 1024:
                            # if it's higher than 1024 (the limit), the result should be changed from satisfiable to memory limit error
                            sat = "Memory limit"
                        # proceed to reading the time usage
                        state = "P9_ReadTime"
                elif state == "P9_ReadTime":
                    # the time line looks somewhat like "User_CPU=0.01, System_CPU=0.00, Wall_clock=0."
                    # get the User_CPU value as it is the exact time of prover's work
                    if line.startswith("User_CPU"):
                        time_report = line.split(", ")
                        cpu_time = time_report[0].split("=")
                        # add it to time result
                        total_time += float(cpu_time[1])
                        # all results were read, mark the success and finish reading the file
                        state = "P9_Success"
                        break
                elif state == "SP_FindResult":
                    # look for the beggining of SPASS statistics block
                    # the result line looks somewhat like "SPASS beiseite: {result string}"
                    if line[6:14] == "beiseite":
                        result_report = line.split(' ')
                        # if time limit was exceeded, the result string is "Ran out of time. SPASS was killed." or simply "Ran out of time."
                        if len(result_report) >= 6 and result_report[5] == "time.":
                            sat = "Timeout"
                        # else, the results string is "Completion found." if formula is satisfiable and "Proof found." if it's unsatisfiable
                        else:
                            sat = str((result_report[2] == "Completion"))
                        # proceed to reading the memory usage
                        state = "SP_FindMemLine"
                elif state == "SP_FindMemLine":
                    # the memory line looks somewhat like "SPASS allocated 85016 KBytes."
                    if line[6:15] == "allocated":
                        mem_report = line.split(' ')
                        # read the number and divide it so that it is expressed in megabytes
                        total_memory += int(mem_report[2])/1024
                        # proceed to reading the time usage
                        state = "SP_ReadTimeLines"
                elif state == "SP_ReadTimeLines":
                    # the time lines look somewhat like "SPASS spent	0:00:00.13 on the problem.
                    #                                               \t\t0:00:00.04 for the input.
                    #                                               \t\t0:00:00.02 for the FLOTTER CNF translation.
                    #                                               \t\t0:00:00.00 for inferences.
                    #                                               \t\t0:00:00.00 for the backtracking.
                    #                                               \t\t0:00:00.00 for the reduction."
                    # the first value is the total time, read it
                    if line[6:11] == "spent":
                        split_line = line.split(" ")
                        times = split_line[1].split("\t")[1]
                        split_times = times.split(":")
                        # convert hours and minutes to seconds
                        total_time += float(split_times[0]) * 3600
                        total_time += float(split_times[1]) * 60
                        total_time += float(split_times[2])
                        # all results were read, mark the success and finish reading the file
                        state = "SP_Success"
                        break
                    
            
                # Vampire, Snake
                elif state == "VS_FindResult":
                    if "Memory used" in line:
                        total_memory=int(line.split(":")[-1])
                    elif "Termination reason" in line:
                        sat=str(line.split(":")[-1][1:]=="Success")
                    elif "Success in time" in line:
                        
                        total_time=float(line.split(" ")[-2])
                        # print(line.split(" ")[-2], total_time)
                    if total_memory!=0 and sat!=None and total_time!=0:
                        state="VS_Success"
                        break

                # Z3
                elif state == "Z3_FindResult":
                    if "memory" in line:
                        total_memory=int(float(line.split(" ")[-1])*100)
                    elif "sat" in line:
                        sat=str(line==" sat")
                    elif "unknown" in line:
                        sat="unknown"
                    elif "time" in line:
                        total_time=float(line.split(" ")[-1][:-2])
                    if total_memory!=0 and sat!=None and total_time!=0:
                        state="Z3_Success"
                        break
                # CVC4
                elif state == "CV_FindResult":
                    if "resourceUnitsUsed" in line:
                        total_memory=int(line.split(" ")[-1])
                    elif "sat" in line and ":" not in line:
                        sat=str(line=="sat")
                    elif "unknown" in line and ":" not in line:
                        sat=str("unknown")
                    elif "totalTime" in line:
                        total_time=float(line.split(" ")[-1])
                    if total_memory!=0 and sat!=None and total_time!=0:
                        state="CV_Success"
                        break
                    
            # if SPASS output file is empty or has one empty line, a memory limit error occured
            if state == "SP_FindResult" and valid_line_counter <= 1:
                sat = "Memory limit"
                state = "SP_Success"
            

        # if results were not read successfuly, raise an error
        if state != "P9_Success" and state != "SP_Success" and state!="VS_Success" and state!="Z3_Success" and state!="CV_Success":
            att = self.output_file.split(".")[:-1][0]
            att = att.split("/")[-1]
            print({"memory": total_memory, "time": total_time, "sat": sat, "att": att})
            # print(state)
            # raise RFGError(f"ProverRunner.getMeasuresFromOutputFile: Results not found in output file or had incorrect result {state}.", self.output_file)
        
        return {"memory": total_memory, "time": total_time, "sat": sat}
