from testenv import TestEnv
from randomgen import Generator
import os

def main() -> None:
    # enviroment = TestEnv(os.path.dirname(os.path.abspath(__file__)) + "/dane_testowe/scenario")
    # enviroment.makeTests()

    # test = Generator('problem3', clauses_num=2000, atoms_num_coeff=0.5)
    # files = test.translateAndSave()
    # runner = ProverRunner("prover9", input_file=files["prover9_input"])
    # current_output_file = files["prover9_input"][:-2] + "out"
    # usage_dict = runner.performMeasurements(current_output_file)
    # print(usage_dict)


if __name__ == '__main__':
    main()