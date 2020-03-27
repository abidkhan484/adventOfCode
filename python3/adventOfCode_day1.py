#! /usr/bin/python3


"""
Advent Of Code: 2019
Problem statement: https://adventofcode.com/2019/day/1
First Task Commit: https://github.com/abidkhan484/adventOfCode/commit/13ca3aad1de1cae6ffc1c3a6e4a748d74fdda5f7
"""

file_ = "aoc_d1_input.txt"

def requirement(i, res=0):
    t = ((i // 3)-2)
    if (t <= 0):
        return res
    res += t
    return requirement(t, res)


res = 0
with open(file_) as f:
    data = map(int, f.readlines())
    for i in data:
        res += requirement(i)

print(res)

