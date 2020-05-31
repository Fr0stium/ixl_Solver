import readline
import mpmath
from .global_functions import copy
from sympy import parse_expr, solve, Symbol

def introduction():
    print("\nA2.B1 - solve linear equations\n")
    print("enter the equation.")
    print("the program will return the solution of the equation.")
    print("type 'e' to exit.\n")

def solve_ixl():
    while True:
        try:
            user_input = input()
            if user_input == "e":
                print("exiting a2.b1...\n")
                break

            split_input = user_input.split("=") # split input into two sides to generate a new equation that can be set to 0
            left_side = parse_expr(split_input[0])
            right_side = parse_expr(split_input[1])

            if (len((left_side - right_side).free_symbols) > 1): # check if there is more than one variable in the expression
                raise Exception("too many variables")

            new_equation = left_side - right_side
            answer = str(solve(new_equation)[0])

            print(answer + "\n")
            copy(answer)

        except Exception as e:
            print(str(e) + "\n")