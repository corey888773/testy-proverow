import subprocess
import os

from config import config
from customerrors import RFGError, RFGTimeoutError
from analyse_provrun import getMeasuresFromFile

class ProverRunner:
    def __init__(self, prover, input_file):
        # remember parameters for later use
        self.input_file = input_file
        self.prover = prover

    def performMeasurements(self, output_file, time_limit=300, os_specific_stats='') -> dict:
        try:
            # run the prover with given file
            self.runProver(output_file, time_limit, os_specific_stats)
        except subprocess.TimeoutExpired:
            raise RFGTimeoutError(output_file)
        except Exception as e:
            raise RFGError(output_file, e)
        
        # return the measurements of prover execution
        return getMeasuresFromFile(self.prover, output_file)

    def runProver(self, output_file, time_limit, os_specific_stats):
        # if prover name is given, save it
        if output_file != None:
            self.output_file = output_file
        # else replace it with a generic name
        else:
            self.output_file = 'prover_output.out'

        if self.prover == 'prover9':
            # run Prover9 with search time limit (parameter -t) and using a file (parameter -f), redirect the output to a file
            command = [os_specific_stats, f'{config.BINARIES_DIR}/prover9/bin/prover9 -t', str(time_limit/5), '-f', self.input_file, '&>', self.output_file]
            command = ' '.join(command)
            # execute the command in a new process, with additional time_limit for the entire execution
            subprocess.call(command, shell=True, timeout=time_limit/5)
        elif self.prover == 'spass':
            # run SPASS Prover with time limit (parameter -TimeLimit), redirect the output to a file
            command = [os_specific_stats, f'{config.BINARIES_DIR}/spass/bin/spass -TimeLimit={str(time_limit)}', self.input_file, '&>', self.output_file]
            command = ' '.join(command)
            # execute the command in a new process
            subprocess.call(command, shell=True)
        elif self.prover == 'cvc5':
            time_limit_ms = time_limit * 1000
            command = [os_specific_stats, f'{config.BINARIES_DIR}/cvc5/bin/cvc5' , '--lang', 'smt2', '--stats', '--tlimit', str(time_limit_ms),self.input_file, '&>', self.output_file, '2>>', self.output_file]
            command = ' '.join(command)
            # execute the command in a new process
            subprocess.call(command, shell=True)
        elif self.prover == 'z3':
            command = [os_specific_stats, 'python3', self.input_file, '&>', self.output_file]
            command = ' '.join(command)
            # execute the command in a new process
            subprocess.call(command, shell=True)
        elif self.prover == 'vampire':
            command = [os_specific_stats, f'{config.BINARIES_DIR}/vampire/bin/vampire', '--mode', 'casc_sat', '-t', str(time_limit), '<', self.input_file, '&>', self.output_file]
            command = ' '.join(command)
            # execute the command in a new process
            subprocess.call(command, shell=True)
        elif self.prover == 'snake':
            command = [os_specific_stats, f'{config.BINARIES_DIR}/snake/bin/snake --input_syntax tptp --proof off --output_axiom_names on --mode portfolio --schedule snake_tptp_uns --cores 1 -m 12000','-t', str(time_limit), self.input_file, '&>', self.output_file]
            command = ' '.join(command)
            # execute the command in a new process
            subprocess.call(command, shell=True)
        elif self.prover == 'e':
            command = [os_specific_stats, f'{config.BINARIES_DIR}/e/bin/eprover --cpu-limit={str(time_limit)}', '-sR', self.input_file, '&>', self.output_file]
            command = ' '.join(command)
            subprocess.call(command, shell=True)

            #~/solvers/spass/bin/dfg2tptp 