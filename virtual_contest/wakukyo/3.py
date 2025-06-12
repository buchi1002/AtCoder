from itertools import product
def main():
    A, B, C, D = input()

    for opts in product(["+", "-"], ["+", "-"], ["+", "-"]):
        formula = f"{A}{opts[0]}{B}{opts[1]}{C}{opts[2]}{D}"
        if eval(f"{formula}==7"):
            print(formula + "=7")
            return


main()