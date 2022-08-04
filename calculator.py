from decimal import *

getcontext().prec = 6


def calculation(user_input):
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
            number = int(user_input[i])
            sum_list.append(number)
        if i % 2 == 1:
            operator = user_input[i]
            sum_list.append(operator)

    for i in sum_list:
        if i == operator:
            num1 = sum_list[sum_list.index(operator) - 1]
            num2 = sum_list[sum_list.index(operator) + 1]
        if i == '+':
            result = num1 + num2
        elif i == '-':
            result = num1 - num2
        elif i == '*':
            result = num1 * num2
        elif i == '/':
            result = num1 / num2

    return result



