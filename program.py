import a2_a1

def introduction():
    print("type an IXL name, and this program will solve it for you:")

def main():
    introduction()
    user_input = input()
    if "a2.a.1" in user_input:
        a2_a1.solve()

main()