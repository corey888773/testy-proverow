from typing import Callable, Tuple
from config import config


class AnalyseCtx:
    def __init__(self, prover : str, state : str):
        self.prover = prover # name of the prover
        self.state = state # state of the analysis
        self.success = False # True if all results were read successfuly
        self.sat = None # "True", "False", "Timeout", "Memory limit", "unknown"
        self.total_memory = 0 # in MB
        self.total_time = 0 # in seconds

    def __dict__(self) -> dict:
        return {"prover" : self.prover, "memory": self.total_memory, "time": self.total_time, "sat": self.sat}


def analyseP9(out_file : str, prover : str, 
                os_specyfic_analysis : Callable[[str], Tuple[str, str]]=None) -> AnalyseCtx:
    ctx = AnalyseCtx(prover, "P9_FindStatisticsBlock")

    with open(out_file,'r') as f:
        for line in f:
            # if beginning of the line doesn't match any of demanded patterns, skip it to speed up the search
            if not line.startswith(('=','%','G','M','U',"SPASS",'\t',' ','u','s','d')):
                continue

            if ctx.state == "P9_FindStatisticsBlock":
                if line == "============================== STATISTICS ============================\n":
                    ctx.state = "P9_ReadSat"

            elif ctx.state == "P9_ReadSat":
                # the result line looks somewhat like "Given=0. Generated=1. Kept=0. proofs=1."
                # get the number of proofs
                sat_report = line.split(" ")
                proofs_statistic = sat_report[3].split("=")
                if int(proofs_statistic[1][0]) == 0:
                    ctx.sat = "True"
                else:
                    ctx.sat = "False"
                ctx.state = "P9_FindMegabytes"

            elif ctx.state == "P9_FindMegabytes":
                # the memory line looks somewhat like "Megabytes=0.04."
                if line.startswith("Megabytes"):
                    mem_report = line.split("=")
                    ctx.total_memory += float(mem_report[1][:-2])
                    if ctx.total_memory > 1024:
                        # if it's higher than 1024 (the limit), the result should be changed from satisfiable to memory limit error
                        ctx.sat = "Memory limit"
                    ctx.state = "P9_ReadTime"

            elif ctx.state == "P9_ReadTime":
                # the time line looks somewhat like "User_CPU=0.01, System_CPU=0.00, Wall_clock=0."
                # get the User_CPU value as it is the exact time of prover's work
                if line.startswith("User_CPU"):
                    time_report = line.split(", ")
                    cpu_time = time_report[0].split("=")
                    ctx.total_time += float(cpu_time[1])

                    # all results were read, mark the success and finish reading the file
                    ctx.state = "P9_Success"
                    ctx.success = True
                    break

    if os_specyfic_analysis != None:
        time, memory = os_specyfic_analysis(out_file)
        ctx.total_time = time
        ctx.total_memory = memory
        ctx.state="P9_Success"
        ctx.success = True

    return ctx


def analyseSPASS(out_file : str, prover : str, 
                os_specyfic_analysis : Callable[[str], Tuple[str, str]]=None) -> AnalyseCtx:
    ctx = AnalyseCtx(prover, "SP_FindResult")

    valid_lines = 0
    with open(out_file,'r') as f:
        for line in f:
            if not line.startswith(('=','%','G','M','U',"SPASS",'\t',' ','u','s','d')):
                continue
            valid_lines += 1

            if ctx.state == "SP_FindResult":
                # the result line looks somewhat like "SPASS beiseite: {result string}"
                if line[6:14] == "beiseite":
                    result_report = line.split(' ')

                    # if time limit was exceeded, the result string is "Ran out of time. SPASS was killed." or simply "Ran out of time."
                    if len(result_report) >= 6 and result_report[5] == "time.":
                        ctx.sat = "Timeout"

                    # else, the results string is "Completion found." if formula is satisfiable and "Proof found." if it's unsatisfiable
                    else:
                        ctx.sat = str((result_report[2] == "Completion"))
                    ctx.state = "SP_FindMemLine"

            if ctx.state == "SP_FindMemLine":
                # the memory line looks somewhat like "SPASS allocated 85016 KBytes."
                if line[6:15] == "allocated":
                    mem_report = line.split(' ')

                    ctx.total_memory += int(mem_report[2])/1024 # convert to MB
                    ctx.state = "SP_ReadTimeLines"

            if ctx.state == "SP_ReadTimeLines":
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
                    ctx.total_time += float(split_times[0]) * 3600
                    ctx.total_time += float(split_times[1]) * 60
                    ctx.total_time += float(split_times[2])

                    # all results were read, mark the success and finish reading the file
                    ctx.state = "SP_Success"
                    ctx.success = True
                    break


        # if SPASS output file is empty or has one empty line, a memory limit error occured
        if ctx.state == "SP_FindResult" and valid_lines <= 1:
            ctx.sat = "Memory limit"
            ctx.state = "SP_Success"
            ctx.success = True

    if os_specyfic_analysis != None:
        time, memory = os_specyfic_analysis(out_file)
        ctx.total_time = time
        ctx.total_memory = memory
        ctx.state="SP_Success"
        ctx.success = True

    return ctx


def analyseVampireOrSnake(out_file : str, prover : str, 
                os_specyfic_analysis : Callable[[str], Tuple[str, str]]=None) -> AnalyseCtx:
    ctx = AnalyseCtx(prover, "VS_FindResult")

    SAT_MAP = {"Unsatisfiable" : "False", "Satisfiable" : "True"}

    with open(out_file,'r') as f:
        for line in f:
            if not line.startswith(('=','%','G','M','U',"SPASS",'\t',' ','u','s','d')):
                continue
        
            if ctx.state == "VS_FindResult":
                if "Memory used" in line:
                    ctx.total_memory=int(line.split(":")[-1])

                elif "SZS status" in line:
                    result = line.split(" ")[-3].rstrip().replace('\n', '')
                    if result in SAT_MAP:
                        ctx.sat = SAT_MAP[result]
                    else:
                        ctx.sat = "unknown"
                    
                elif "Success in time" in line:
                    ctx.total_time=float(line.split(" ")[-2])

                if ctx.total_memory != 0 and ctx.sat != None and ctx.total_time != 0:
                    ctx.state="VS_Success"
                    ctx.success = True
                    break
            
    if os_specyfic_analysis != None:
        time, memory = os_specyfic_analysis(out_file)
        ctx.total_time = time
        ctx.total_memory = memory
        ctx.state="VS_Success"
        ctx.success = True

    return ctx


def analyseZ3(out_file : str, prover : str, 
                os_specyfic_analysis : Callable[[str], Tuple[str, str]]=None) -> AnalyseCtx:
    ctx = AnalyseCtx(prover, "Z3_FindResult")

    SAT_MAP = {"sat": "True", "unsat": "False"}

    with open(out_file,'r') as f:
        for idx, line in enumerate(f):
            if ctx.state == "Z3_FindResult":
                # result is in the first line
                if idx == 0:
                    line = line.split(" ")
                    result = line[0].rstrip().replace('\n', '')
                    if result in SAT_MAP:
                        ctx.sat = SAT_MAP[result]
                    else:
                        ctx.sat = "unknown"

                if "memory" in line:
                    ctx.total_memory = int(float(line.split(" ")[-1]) * 100)

                elif "unknown" in line:
                    ctx.sat = "unknown"

                elif "time" in line:
                    ctx.total_time = float(line.split(" ")[-1][:-2])

                if ctx.total_memory != 0 and ctx.sat != None and ctx.total_time != 0:
                    ctx.state = "Z3_Success"
                    ctx.success = True
                    break

    if os_specyfic_analysis != None:
        time, memory = os_specyfic_analysis(out_file)
        ctx.total_time = time
        ctx.total_memory = memory
        ctx.state="Z3_Success"
        ctx.success = True

    return ctx


def analyseCVC5(out_file : str, prover : str, 
                os_specyfic_analysis : Callable[[str], Tuple[str, str]]=None) -> AnalyseCtx:
    ctx = AnalyseCtx(prover, "CV_FindResult")

    SAT_MAP = {"sat": "True", "unsat": "False"}

    with open(out_file,'r') as f:
        for idx, line in enumerate(f):
            if ctx.state == "CV_FindResult":
                if "resourceUnitsUsed" in line:
                    ctx.total_memory = int(line.split(" ")[-1])

                if idx == 0:
                    line = line.split(" ")
                    result = line[0].replace('\n', '')
                    if result in SAT_MAP:
                        ctx.sat = SAT_MAP[result]
                    else:
                        ctx.sat = "unknown"

                elif "totalTime" in line:
                    total_time_in_ms = line.split(" ")[-1].rstrip() # e.g 21ms
                    ctx.total_time = float(total_time_in_ms[:-2]) / 1000 # convert to seconds
                    

                if ctx.total_memory != 0 and ctx.sat != None and ctx.total_time != 0:
                    ctx.state="CV_Success"
                    ctx.success = True
                    break

    if os_specyfic_analysis != None:
        time, memory = os_specyfic_analysis(out_file)
        ctx.total_time = time
        ctx.total_memory = memory
        ctx.state="CV_Success"
        ctx.success = True

    return ctx


def analyseE(out_file : str, prover : str, 
            os_specyfic_analysis : Callable[[str], Tuple[str, str]]=None) -> AnalyseCtx:
    ctx = AnalyseCtx(prover, "E_FindResult")

    SAT_MAP = {"Satisfiable": "True", "Unsatisfiable": "False"}

    with open(out_file,'r') as f:
        for line in f:
            if not line.startswith(('#')):
                continue

            elif ctx.state == "E_FindResult":
                if "resident set size" in line:
                    ctx.total_memory = int(line.split(" ")[-2])

                elif "SZS status" in line:
                    result = line.split(" ")[-1].rstrip().replace('\n', '')
                    if result in SAT_MAP:
                        ctx.sat = SAT_MAP[result]
                    else:
                        ctx.sat = "unknown"

                elif "Total time" in line:
                    ctx.total_time = float(line.split(" ")[-2])

                if ctx.total_memory != 0 and ctx.sat != None and ctx.total_time != 0:
                    ctx.state="E_Success"
                    ctx.success = True
                    break

    if os_specyfic_analysis != None:
        time, memory = os_specyfic_analysis(out_file)
        ctx.total_time = time
        ctx.total_memory = memory
        ctx.state="E_Success"
        ctx.success = True

    return ctx


def analyse_macos_specifc_stats(out_file):
    time = 0
    memory = 0

    with open(out_file,'r') as f:
        # for the last 19 lines
        for line in f.readlines()[-19:]:
            # if line containser real user sys
            if all(x in line for x in ["real", "user", "sys"]):
                # strip the spaces and split by space
                line = line.strip().split(" ")
                time = float(line[0])

            if "maximum resident set size" in line:
                line = line.strip().split(" ")
                memory = float(line[0])

    return time, memory
                

OS_SPECIFIC_STATS = {
    "macos_arm64": analyse_macos_specifc_stats
}

PROVER_ANALYSER = { 
    "prover9": analyseP9,
    "spass": analyseSPASS,
    "vampire": analyseVampireOrSnake,
    "snake": analyseVampireOrSnake,
    "z3": analyseZ3,
    "cvc5": analyseCVC5,
    "e": analyseE
}   
def getMeasuresFromFile(prover, out_file) -> dict:
    func = PROVER_ANALYSER[prover]
    os_specific_stats_func = OS_SPECIFIC_STATS[config.OS_NAME]

    ctx = func(out_file, prover, os_specific_stats_func)

    if ctx.success == False:
        att = out_file.split(".")[:-1][0]
        att = att.split("/")[-1]

        print(ctx.__dict__(), att)
        # raise RFGError(f"ProverRunner.getMeasuresFromOutputFile: Results not found in output file or had incorrect result {state}.", out_file)
        
    return ctx.__dict__()

