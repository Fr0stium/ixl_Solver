import readline
import mpmath
from .global_functions import copy
from sympy import parse_expr, simplify, Symbol


def introduction():
    print("\nA2.A3 - simplify variable expressions using properties.\n")
    print("enter the expression.")
    print("the program will return the simplified version of the expression.")
    print("type 'e' to exit.\n")


def solve_ixl():
    while True:
        try:
            user_input = input()
            if user_input == "e":
                print("exiting a2.a3...\n")
                break

            expression = parse_expr(user_input)
            answer = str(simplify(expression))

            print(answer + "\n")
            copy(answer)

        except Exception as e:
            print(str(e) + "\n")
