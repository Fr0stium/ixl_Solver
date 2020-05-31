import readline
import mpmath
from .global_functions import copy
from sympy import parse_expr, Symbol

def introduction():
    print("\nA2.A1 - evaluate variable expressions involving integers\n")
    print("enter the expression. you will be asked what each variable's value is.")
    print("the program will return the solution.\n")
    print("type 'e' to exit.\n")

def solve_ixl():
    while True:
        try:
            user_input = input()
            if user_input == "e":
                print("exiting a2.a1...\n")
                break

            expression = parse_expr(user_input) # transform the input into a mathematical expression
            variables = expression.free_symbols # get all the variables from the expression
            variable_value_pairs = [] # create a list of 2-tuples: item 1 is the variable, item 2 is its value

            for variable in variables:
                print(str(variable) + " = ", end = "") # ask the user what each variable's value is
                substitution = int(input()) # cast to int since this ixl deals only with integers
                variable_value_pairs.append((variable, substitution))

            answer = str(int(expression.subs(variable_value_pairs)))

            print(answer + "\n")
            copy(answer)

        except Exception as e:
            print(str(e) + "\n")