import readline
import mpmath
from .global_functions import copy, format_exponents
from sympy import parse_expr, solve, Symbol

def introduction():
    print("\nA2.B6 - solve multi-variable equations\n")
    print("enter the equation, then enter the variable to solve for.")
    print("the program will return the solution of the equation in terms of that variable.")
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
            new_equation = left_side - right_side

            variable = Symbol(input("solve for: ")) # ask the user for the variable to solve for
            if variable not in new_equation.free_symbols:
                raise Exception("invalid variable")

            answer = str(solve(new_equation, variable)[-1]) # choose the last element. when outputting solutions with a sqrt(), IXL only accepts the positive square root
            answer = format_exponents(answer)

            print(answer + "\n")
            copy(answer)

        except Exception as e:
            print(str(e) + "\n")