#! /usr/bin/python3


file_ = "aoc_d1_input.txt"

res = 0
with open(file_) as f:
    data = map(int, f.readlines())
    for i in data:
        res += ((i // 3)-2)

print(res)

