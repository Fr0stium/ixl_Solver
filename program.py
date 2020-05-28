from algebra2 import a2_a1
from algebra2 import a2_a2

def introduction():
    print("type 'e' to exit")
    print("type an IXL name, and this program will solve it for you:\n")

def if_exit(user_input):
    if user_input == "e":
        print("exiting...\n")
        exit()

def do_ixl(user_input):
    ixl = user_input.replace(".", "_")
    eval("%s.introduction()" % ixl)
    eval("%s.solve()" % ixl)

def main():
    while True:
        try:
            introduction()
            user_input = input().lower()
            if_exit(user_input)
            do_ixl(user_input)
        except Exception as e:
            print(e)

# run main method
main()