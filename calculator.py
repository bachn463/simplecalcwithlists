def calculator(expression):
    list_exp = split_exp(expression)
    print(list_exp)
    numbers = []
    operators = []
    for element in list_exp:
        if get_token_type(element) == "N":
            numbers.append(element)
        elif element == "(":
            operators.append(element)
        elif element == ")":
            while operators[-1] != "(":
                pop_calculate_push(numbers, operators)
            del operators[-1]
        else:
            while len(operators) > 0 and can_pop(operators[len(operators) - 1], element):
                pop_calculate_push(numbers, operators)
            operators.append(element)
    while len(operators) > 0:
        pop_calculate_push(numbers, operators)
    return numbers[0]


def get_token_type(token):
    if 48 <= ord(token[0]) <= 57:
        return "N"
    return "O"


def split_exp(exp):
    op = "+-*/^"
    num = "1234567890"
    constructing_str = ""
    for character in exp:
        if character in op:
            constructing_str += " " + character + " "
        elif character == "(":
            constructing_str += character + " "
        elif character == ")":
            constructing_str += " " + character
        elif character in num:
            constructing_str += character
        else:
            return "invalid character detected"
    return constructing_str.split(" ")


def can_pop(op1, op2):
    order_of_op = {"^": 2,
                   "*": 1,
                   "/": 1,
                   "+": 0,
                   "-": 0,}
    if op1 != "(" and order_of_op[op1] >= order_of_op[op2]:
        return True
    return False


def evaluate(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "div by 0 error"
    elif op == "^":
        return num1 ** num2
    return "operator does not exist"


def pop_calculate_push(num_list, op_list):
    subresult = evaluate(float(num_list[len(num_list) - 2]), float(num_list[len(num_list) - 1]),op_list[len(op_list) - 1])
    del num_list[len(num_list) - 2:len(num_list)]
    del op_list[len(op_list) - 1]
    num_list.append(subresult)


a = "4*(1+2)-(((5+1)/2)^2)*2"
print(calculator(a))
#prints out -6.0
