import subprocess
import os

from customerrors import RFGError, RFGTimeoutError
from analyse_provrun import getMeasuresFromFile

class ProverRunner:
    def __init__(self, prover, input_file):
        # remember parameters for later use
        self.input_file = input_file
        self.prover = prover

    def performMeasurements(self, output_file) -> dict:
        try:
            # run the prover with given file
            self.runProver(output_file=output_file)
        except subprocess.TimeoutExpired:
            # change the error type so that it prints in a desired way
            raise RFGTimeoutError(output_file)
        
        # return the measurements of prover execution
        return getMeasuresFromFile(self.prover, output_file)

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