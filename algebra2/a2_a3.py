import readline
import mpmath
from subprocess import check_call
from sympy import parse_expr, simplify, Symbol
from sys import platform

def introduction():
    print("\nA2.A3 - simplify variable expressions using properties.\n")
    print("enter the expression.")
    print("the program will return the simplified version of the expression.")
    print("type 'e' to exit.\n")

def copy(answer): # copy to clipboard
    cmd = ("echo " + answer.strip() + "|clip") if platform == "Windows" else ("echo " + answer.strip() + "|pbcopy")
    return check_call(cmd, shell=True)

def solve_ixl():
    while True:
        try:
            user_input = input()
            if user_input == "e":
                print("exiting a2.a3...\n")
                break
            expression = parse_expr(user_input) # transform the input into a mathematical expression
            answer = str(simplify(expression))
            print(answer + "\n")
            copy(answer)
        except Exception as e:
            print(str(e) + "\n")