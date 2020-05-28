from algebra2.a2_a1 import solve as a2_a1_solve

def introduction():
    print("\nA2.A.2 - evaluate variable expressions involving rational numbers\n")
    print("enter the expression. you will be asked what each variable's value is.")
    print("the program will return the solution.\n")
    print("type 'e' to exit\n")

def solve(cast_to_int):
    a2_a1_solve(cast_to_int) # a2_a2 is identical to a2_a1, but the former deals with rational numbers rather than ints