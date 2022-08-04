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
            sum_list.append(int(user_input[i]))
        if i % 2 == 1:
            sum_list.append(user_input[i])

    for i in sum_list:
        if i == '+':
            result = sum_list[0] + sum_list[2]
        elif i == '-':
            result = sum_list[0] - sum_list[2]
        elif i == '*':
            result = sum_list[0] * sum_list[2]
        elif i == '/':
            result = sum_list[0] / sum_list[2]

    return result



