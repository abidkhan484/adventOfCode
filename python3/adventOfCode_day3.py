#! /usr/bin/python


"""
Advent Of Code: 2019
Problem statement: https://adventofcode.com/2019/day/3
"""

file_name = 'aoc_d3_input.txt'
with open(file_name) as f:
    moving_input_1, moving_input_2 = f.read().split('\n')


def get_direction_list(input_list):
    initial_x, initial_y = 0, 0
    directions = {'U' : 1, 'D' : -1, 'R' : 1, 'L' : -1}
    direction_list = [ [initial_x, initial_y] ]
    
    for item in input_list:
        if (item[0] == 'U' or item[0] == 'D'):
            initial_x, initial_y = initial_x, initial_y + directions[item[0]] * int(item[1:])
        else:
            initial_x, initial_y = initial_x + directions[item[0]] * int(item[1:]), initial_y
        direction_list.append([initial_x, initial_y])

    return direction_list

def check_in_between_two_numbers(a, b, x):
    # check if x is in between a and b
    res = (x - a) * (x - b)
    return True if res < 0 else False

def check_intersection(point1, point2, point3, point4):
    # point1 and point2 are the first_direction_list points
    # point3 and point4 are the second_direction_list points
    if (point1[0] == point2[0]):
        point1, point2, point3, point4 = point3, point4, point1, point2

    x_axis = check_in_between_two_numbers(point1[0], point2[0], point3[0])    
    y_axis = check_in_between_two_numbers(point3[1], point4[1], point1[1])

    if (x_axis and y_axis):
        # (point3[0], point1[1]) is the intersection point
        return abs(point3[0]) + abs(point1[1])

    return -1



moving_input_1 = moving_input_1.split(',')
moving_input_2 = moving_input_2.split(',')

first_direction_list = get_direction_list(moving_input_1)
second_direction_list = get_direction_list(moving_input_2)

first_direction_list_count = len(first_direction_list) - 1
second_direction_list_count = len(second_direction_list) - 1

minimum_distance = 10000000001
intersections = []
for i in range(first_direction_list_count):
    # point1 and point2 are the first_direction_list points
    point1, point2 = first_direction_list[i], first_direction_list[i+1]

    for j in range(second_direction_list_count):
        # point3 and point4 are the second_direction_list points
        point3, point4 = second_direction_list[j], second_direction_list[j+1]
        distance = check_intersection(point1, point2, point3, point4)

        if ( distance != -1 and minimum_distance > distance):
            minimum_distance = distance

print(minimum_distance)
