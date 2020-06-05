from algebra2 import a2_a1
from algebra2 import a2_a2
from algebra2 import a2_a3
from algebra2 import a2_b1
from algebra2 import a2_b6
from algebra2 import a2_c4


def introduction():
    print("type an IXL name, and this program will solve it for you:\n")


def if_exit(user_input):
    if user_input == "e":
        print("exiting...\n")
        exit()


def do_ixl(user_input):
    ixl = user_input.replace(".", "_")
    eval("%s.introduction()" % ixl)
    eval("%s.solve_ixl()" % ixl)


def main():
    print("type 'e' to exit")
    while True:
        try:
            introduction()
            user_input = input().lower()
            if_exit(user_input)
            do_ixl(user_input)
        except Exception as e:
            print(str(e) + "\n")


# run main method
main()
