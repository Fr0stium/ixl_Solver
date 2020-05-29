import readline
import mpmath
from subprocess import check_call
from sympy import parse_expr, symbols
from sys import platform

def introduction():
    print("\nA2.A2 - evaluate variable expressions involving rational numbers\n")
    print("enter the expression. you will be asked what each variable's value is.")
    print("the program will return the solution.\n")
    print("type 'e' to exit.\n")

def copy(answer): # copy to clipboard
    cmd = ("echo " + answer.strip() + "|clip") if platform == "Windows" else ("echo " + answer.strip() + "|pbcopy")
    return check_call(cmd, shell=True)

def solve_ixl():
    while True:
        try:
            user_input = input()
            if user_input == "e":
                print("exiting a2.a2...\n")
                break
            expression = parse_expr(user_input) # transform the input into a mathematical expression
            variables = expression.free_symbols # get all the variables from the expression
            variable_value_pairs = [] # create a list of 2-tuples: item 1 is the variable, item 2 is its value
            for variable in variables:
                print(str(variable) + " = ", end = "") # ask the user what each variable's value is
                substitution = float(input()) # cast to float since this ixl deals with rational numbers
                variable_value_pairs.append((variable, substitution))
            answer = str(float(expression.subs(variable_value_pairs)))
            print(answer + "\n")
            copy(answer)
        except Exception as e:
            print(str(e) + "\n")