#! /usr/bin/python


"""
Advent Of Code: 2019
Problem Statement: https://adventofcode.com/2019/day/3
"""


def check_criteria(number):
    num = str(number)

    # as the langth of character is fixed
    # and we iterate over the string before the last char
    length = 5
    # this checking can also be done using number % 10
    for i in range(length):
        if ( ord(num[i]) > ord(num[i+1]) ):
            return 0
    
    for i in range(length):
        if (num[i] == num[i+1]):
            return 1
    else:
        return 0



val1, val2 = map(int, input().split('-'))
# val1, val2 = 402328, 864247
val2 += 1

count = 0
for number in range(val1, val2):
    count += check_criteria(number)

print(count)
