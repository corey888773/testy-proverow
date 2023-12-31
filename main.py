from testenv import TestEnv
from generation.randomgen import Generator
from run.provrun import ProverRunner
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))

def main() -> None:
    enviroment = TestEnv(curr_dir + "/data/scenarios/scenario5")
    enviroment.makeTests()

    # test = Generator('problem3', clauses_num=2000, atoms_num_coeff=0.5)
    # files = test.translateAndSave()
    # runner = ProverRunner("prover9", input_file="generated_files_in/problem1_c50_a25_prec50_lengths_2_3_4_6_8_10_prover9.in")
    # current_output_file = "problem1_c50_a25_prec50_lengths_2_3_4_6_8_10_prover9." + "out"
    # usage_dict = runner.performMeasurements(current_output_file)
    # print(usage_dict)


if __name__ == '__main__':
    main()