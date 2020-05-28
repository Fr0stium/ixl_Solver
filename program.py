from algebra2 import a2_a1
from algebra2 import a2_a2

def introduction():
    print("type 'e' to exit")
    print("type an IXL name, and this program will solve it for you:\n")

def if_exit(user_input):
    if user_input == "e":
        print("exiting...\n")
        exit()

def main():
    while True:
        try:
            introduction()
            user_input = input().lower()
            if_exit(user_input)
            if "a2.a.1" in user_input:
                a2_a1.introduction()
                a2_a1.solve(True)
            if "a2.a.2" in user_input:
                a2_a2.introduction()
                a2_a2.solve(False)
        except Exception as e:
            print(e)

# run main method
main()