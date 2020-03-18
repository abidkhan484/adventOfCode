#! /usr/bin/python3


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

