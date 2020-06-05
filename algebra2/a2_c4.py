import readline
import mpmath
from .global_functions import copy
from sympy import parse_expr, reduce_inequalities, Symbol
from sympy.core.relational import Relational


def introduction():
    print("\nA2.C4 - solve linear inequalities\n")
    print("enter the inequality. include words like 'or', if necessary.")
    print("the program will return the solution of the inequality.")
    print("type 'e' to exit.\n")


def get_inequality_sign(inequality, is_double):
    if not is_double:
        if "<=" in inequality:
            return "<="
        elif ">=" in inequality:
            return ">="
        elif "<" in inequality:
            return "<"
        elif ">" in inequality:
            return ">"
        else:
            raise Exception("invalid inequality")
    else:
        if "<" in inequality:
            return "<"  # checking for < also includes <=
        elif ">" in inequality:
            return ">"  # likewise, checking for > includes >= as well
        else:
            raise Exception("invalid inequality")


def get_inequality_sign_count(inequality, inequality_sign):
    return inequality.count(inequality_sign)


# this ixl is limited to linear inequalities, so any letter is a variable
def get_variable(inequality):
    for char in inequality:
        if str.isalpha(char):
            return Symbol(char, real=True)


def remove_infinities(inequality):  # remove infinities to make the answer look nicer
    split_inequality = inequality.split("&")
    new_split_inequality = []
    for item in split_inequality:
        if "oo" not in item:
            new_split_inequality.append(item.strip())
    separator = ', '
    new_inequality = separator.join(new_split_inequality)
    return new_inequality


# use more familiar syntax for inequalities
def format_inequality_signs(solution):
    if "<=" in solution:
        return solution.replace("<=", "≤")
    else:
        return solution.replace(">=", "≥")


# this method is used for the order_double_inequality method
def flip_inequality_sign(inequality_sign):
    if "<=" in inequality_sign:
        return ">="
    elif ">=" in inequality_sign:
        return "<="
    elif "<" in inequality_sign:
        return ">"
    elif ">" in inequality_sign:
        return "<"


def order_double_inequality(first_inequality_solution, first_inequality_sign, second_inequality_solution, second_inequality_sign):

    # a double inequality is a valid double inequality if the following conditions are satisfied:
    #   1. inequality signs match, but the positions of the variables (x) do not:
    #       1A. (a < x)(x < b) -> a < x < b
    #       1B. (x < b)(a < x) -> a < x < b
    #   2. inequality signs do not match, but the positions of the variables (x) do:
    #       2A. (x > a)(x < b) -> a < x < b
    #       2B. (a < x)(b > x) -> a < x < b
    # if those conditions are not met, the double inequality is not valid
    # this method will consider these conditions to correctly order the double inequality

    split_first_inequality = first_inequality_solution.split(
        first_inequality_sign)
    split_second_inequality = second_inequality_solution.split(
        second_inequality_sign)
    ordered_double_inequality = []

    variable_on_left_side_1 = False
    variable_on_right_side_2 = False

    for char in split_first_inequality[0]:
        if char.isalpha():
            variable_on_left_side_1 = True
        else:
            continue
    for char in split_second_inequality[1]:
        if char.isalpha():
            variable_on_right_side_2 = True
        else:
            continue

    # condition 1A:
    if not variable_on_left_side_1 and not variable_on_right_side_2:
        ordered_double_inequality.append(first_inequality_solution)
        ordered_double_inequality.append(second_inequality_solution)
        return ordered_double_inequality

    # condition 1B:
    elif first_inequality_sign in second_inequality_sign or second_inequality_sign in first_inequality_sign:
        ordered_double_inequality.append(second_inequality_solution)
        ordered_double_inequality.append(first_inequality_solution)
        return ordered_double_inequality

    # condition 2A:
    elif variable_on_left_side_1 and not variable_on_right_side_2:
        opposite_first_inequality_sign = flip_inequality_sign(
            first_inequality_sign)
        first_inequality_solution = split_first_inequality[1] + \
            opposite_first_inequality_sign + split_first_inequality[0]
        ordered_double_inequality.append(first_inequality_solution)
        ordered_double_inequality.append(second_inequality_solution)
        return ordered_double_inequality

    # condition 2B:
    elif variable_on_right_side_2 and not variable_on_left_side_1:
        opposite_second_inequality_sign = flip_inequality_sign(
            second_inequality_sign)
        second_inequality_solution = split_second_inequality[1] + \
            opposite_second_inequality_sign + split_first_inequality[0]
        ordered_double_inequality.append(first_inequality_solution)
        ordered_double_inequality.append(second_inequality_solution)
        return ordered_double_inequality

    # no conditions met
    else:
        raise Exception("invalid double inequality")


# combine two inequalities into a double inequality
def format_double_inequality(solution, variable):
    variable = str(variable)
    solution = solution.replace("(", "")
    solution = solution.replace(")", "")
    for i in range(len(solution)):
        if solution[i] == variable:
            formatted_double_inequality = solution[:i] + solution[i+1:]
            return formatted_double_inequality


def solve_inequality(user_input):
    inequality_sign = get_inequality_sign(user_input, False)
    split_input = user_input.split(inequality_sign)
    left_side = parse_expr(split_input[0])
    right_side = parse_expr(split_input[1])

    inequality = Relational(left_side, right_side, inequality_sign)
    variable = get_variable(str(inequality))
    answer = remove_infinities(
        str(reduce_inequalities(inequality, symbols=variable)))

    if answer == "True" or answer == "False":
        raise Exception("no parallel functions allowed")

    return answer


def solve_ixl():
    while True:
        try:
            user_input = input()
            if user_input == "e":
                print("exiting a2.c4...\n")
                break

            if "or" in user_input:  # inequality with "or" (a < b or b > c)
                split_input = user_input.split("or")
                first_inequality_solution = solve_inequality(
                    split_input[0]).strip()
                second_inequality_solution = solve_inequality(
                    split_input[1]).strip()
                first_inequality_solution = format_inequality_signs(
                    first_inequality_solution)
                second_inequality_solution = format_inequality_signs(
                    second_inequality_solution)

                print(first_inequality_solution + " or " +
                      second_inequality_solution + "\n")

            # double inequality (a < b < c), which has two inequality signs
            elif get_inequality_sign_count(user_input, get_inequality_sign(user_input, True)) > 1:
                user_input = user_input.replace(" ", "")
                inequality_sign = get_inequality_sign(user_input, True)
                first_inequality_sign = inequality_sign
                second_inequality_sign = inequality_sign

                #  find the 1st inequality sign:
                first_inequality_sign_index = user_input.find(inequality_sign)
                if user_input[first_inequality_sign_index + 1] == "=":
                    first_inequality_sign = inequality_sign + "="

                #  find the 2nd inequality sign:
                start = 2 if "=" in first_inequality_sign else 1
                second_inequality_sign_index = user_input.find(
                    inequality_sign, first_inequality_sign_index + start)
                if user_input[second_inequality_sign_index + 1] == "=":
                    second_inequality_sign = inequality_sign + "="

                # solve the inequalities
                first_inequality = user_input[:second_inequality_sign_index]
                second_inequality = user_input[first_inequality_sign_index + start:]

                first_inequality_solution = solve_inequality(
                    first_inequality).strip()
                second_inequality_solution = solve_inequality(
                    second_inequality).strip()

                # format the inequalities to make them look nicer
                first_inequality_sign = get_inequality_sign(
                    first_inequality_solution, False)
                second_inequality_sign = get_inequality_sign(
                    second_inequality_solution, False)

                ordered_double_inequality = order_double_inequality(
                    first_inequality_solution, first_inequality_sign, second_inequality_solution, second_inequality_sign)
                first_inequality_solution = format_inequality_signs(
                    ordered_double_inequality[0])
                second_inequality_solution = format_inequality_signs(
                    ordered_double_inequality[1])

                double_inequality = format_double_inequality(
                    first_inequality_solution + second_inequality_solution, get_variable(first_inequality_solution + second_inequality_solution))

                print(double_inequality + "\n")
                copy(double_inequality)

            else:  # normal inequality (a < b)
                solution = solve_inequality(user_input)
                solution = format_inequality_signs(solution)
                print(solution + "\n")

        except Exception as e:
            print(str(e) + "\n")
