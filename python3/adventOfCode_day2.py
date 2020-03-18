#! /usr/bin/python3

"""
Advent Of Code: 2019
Problem statement: https://adventofcode.com/2019/day/2
"""

file_name = 'aoc_d2_input.txt'
with open(file_name, 'r') as f:
    data = list(map(int, f.read().split(',')))

# requirement
data[1], data[2] = 12, 2
length = len(data)

i = 0
while (i < length):
    if (99 == data[i]):
        break
    elif (1 == data[i]):
        data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        i += 4
    elif (2 == data[i]):
        data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        i += 4

print(data[0])