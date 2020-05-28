import sympy
from sympy.parsing.sympy_parser import parse_expr

def introduction():
    print("\nA2.A.1 - evaluate variable expressions involving integers\n")
    print("enter the expression. you will be asked what each variable's value is.")
    print("the program will return the solution.\n")
    print("type 'e' to exit\n")
        
def solve(cast_to_int): # cast_to_int is a bool that casts numbers to ints or floats. this is so a2_a2.py can borrow this function
    while True:
        try:
            user_input = input()
            if user_input == "e":
                print("exiting a2.a1...\n")
                break
            expression = parse_expr(user_input) # transform the input into a mathematical expression
            variables = expression.free_symbols # get all the variables from the expression
            equivalences = [] # create a list of 2-tuples: item 1 is the variable, item 2 is its value
            for variable in variables:
                print(str(variable) + " = ", end = "")
                substitution = int(input()) if cast_to_int else float(input()) # cast to int or float depending on cast_to_int
                equivalences.append((variable, substitution))
            print("%d\n" % int(expression.subs(equivalences)) if cast_to_int else "%f\n" % float(expression.subs(equivalences)))
        except Exception as e:
            print(str(e) + "\n")