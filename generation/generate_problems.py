from generation.randomgen import Generator

n = [50, 100, 200, 500, 1000]
m = [2, 3, 4, 5]
distribution = ["even", "more_short", "more_long"]
percentage = [10, 20, 35, 50, 65, 80, 90]

# Problem 1
for i in n:

    # Problem 1
    problem_1 = Generator(test_type = 'problem1', clauses_num=i)
    files = problem_1.translateAndSave()

    # Problem 2
    problem_2 = Generator(test_type = 'problem2', clauses_num=i)
    files = problem_2.translateAndSave()

    # Problem 3
    problem_3 = Generator(f'problem3', clauses_num=i, atoms_num_coeff=2)
    files = problem_3.translateAndSave()

    # Problem 4
    for j in m:
        problem_4 = Generator(f'problem4', clause_lengths=[j], clauses_num=i)
        files = problem_4.translateAndSave()

    for p in percentage:
        for d in distribution:

            # Problem 5
            problem_5 = Generator(test_type = 'problem5', clause_lengths=[1, 5, 10, 20], clauses_num=i, problem5_distribution=d)
            files = problem_5.translateAndSave()

        # Problem 6
        problem_6_poisson = Generator(test_type = 'problem6', precentage_of_safty_clauses=p, clauses_num=i, poisson=True, atoms_num_coeff=0.5, problem5_distribution="poisson")
        files = problem_6_poisson.translateAndSave()

        problem_6 = Generator(test_type = 'problem6', precentage_of_safty_clauses=p, clauses_num=i, poisson=False, problem5_distribution="poisson")
        files = problem_6.translateAndSave()

    # Problem 7
    problem_7a = Generator(test_type = 'problem7a', clauses_num=i, poisson=False)
    files = problem_7a.translateAndSave()

    problem_7a_poisson = Generator(test_type = 'problem7a', clauses_num=i, poisson=True,)
    files = problem_7a_poisson.translateAndSave()

    problem_7b = Generator(test_type = 'problem7b', clauses_num=i, poisson=False)
    files = problem_7b.translateAndSave()

    problem_7b_poisson = Generator(test_type = 'problem7b', clauses_num=i, poisson=True,)
    files = problem_7b_poisson.translateAndSave()

    # Problem 8
    problem_8a = Generator(test_type = 'problem8a', clauses_num=i, poisson=False)
    files = problem_8a.translateAndSave()

    problem_8a_poisson = Generator(test_type = 'problem8a', clauses_num=i, poisson=True)
    files = problem_8a_poisson.translateAndSave()

    problem_8b = Generator(test_type = 'problem8b', clauses_num=i, poisson=False)
    files = problem_8b.translateAndSave()

    problem_8b_poisson = Generator(test_type = 'problem8b', clauses_num=i, poisson=True)
    files = problem_8b_poisson.translateAndSave()

    problem_8c = Generator(test_type = 'problem8c', clauses_num=i, poisson=False)
    files = problem_8c.translateAndSave()

    problem_8c_poisson = Generator(test_type = 'problem8c', clauses_num=i, poisson=True)
    files = problem_8c_poisson.translateAndSave()
