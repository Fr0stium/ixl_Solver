import sympy
from sympy.parsing.sympy_parser import parse_expr

def introduction():
    print("A2.A.1 - evaluate variable expressions involving integers\n")
    print("enter the expression. use * for multiplication and / for division.")
    print("after you have entered the expression, you will be asked what each variable's value is.")
    print("the program will return the solution.\n")
    print("type 'e' to exit\n")
    
def if_exit(user_input):
    if user_input == "e":
        print("exiting...")
        exit()
        
def solve():
    introduction()
    while True:
        try:
            user_input = input()
            if_exit(user_input)
            expression = parse_expr(user_input) # transform the input into a mathematical expression
            variables = expression.free_symbols # get all the variables from the expression
            equivalences = [] # create a list of 2-tuples: item 1 is the variable, item 2 is its value
            for variable in variables:
                print(str(variable) + " = ", end = "")
                substitution = int(input()) # we can cast to integer because this ixl exclusively deals with integers
                equivalences.append((variable, substitution))
            print("%d\n" % int(expression.subs(equivalences)))
        except Exception as e:
            print(str(e))