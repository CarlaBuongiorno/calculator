from decimal import *

getcontext().prec = 6


def calculation(user_input):
    
    sum_list = get_sum_list(user_input)
    new_sum_list = calculate_new_sum_list(sum_list)

    return new_sum_list


def get_sum_list(user_input):
    # Credit -> https://thispointer.com/python-replace-multiple-characters-in-a-string/
    char_to_replace = {'+': ' + ',
                       '-': ' - ',
                       '*': ' * ',
                       '/': ' / '
                       }
    for key, value in char_to_replace.items():
        user_input = user_input.replace(key, value)
        
    user_input = user_input.split(" ")
    sum_list = []

    for i in range(0, len(user_input)):
        if i % 2 == 0:
            number = Decimal(user_input[i])
            sum_list.append(number)
        if i % 2 == 1:
            operator = user_input[i]
            sum_list.append(operator)
    
    return sum_list


def calculate_new_sum_list(sum_list):

    while len(sum_list) >= 3:
        num1 = sum_list[0]
        num2 = sum_list[2]
        operator = sum_list[1]

        if operator == '+':
            new_sum_list = num1 + num2
        elif operator == '-':
            new_sum_list = num1 - num2
        elif operator == '*':
            new_sum_list = num1 * num2
        elif operator == '/':
            new_sum_list = num1 / num2

        if len(sum_list) >= 3:
            del sum_list[0:2]
            sum_list.insert(0, new_sum_list)
    
    return new_sum_list