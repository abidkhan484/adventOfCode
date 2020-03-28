#! /usr/bin/python


"""
Advent Of Code: 2019
Problem Statement: https://adventofcode.com/2019/day/3
First Task Commit: https://github.com/abidkhan484/adventOfCode/commit/2590ca911faf78b5a60612ebb3b065d0b66f2fef
"""

file_name = 'aoc_d3_input.txt'
with open(file_name) as f:
    moving_input_1, moving_input_2 = f.read().split('\n')


def get_direction_points(input_list):
    initial_x, initial_y = 0, 0
    directions = {'U' : 1, 'D' : -1, 'R' : 1, 'L' : -1}
    direction_list = [ [initial_x, initial_y] ]
    steps_list = []

    total_steps = 0
    for item in input_list:
        step = int(item[1:])
        total_steps += step
        steps_list.append(total_steps)

        if (item[0] == 'U' or item[0] == 'D'):
            initial_x, initial_y = initial_x, initial_y + directions[item[0]] * step
        else:
            initial_x, initial_y = initial_x + directions[item[0]] * step, initial_y
        direction_list.append([initial_x, initial_y])

    return direction_list, steps_list

def check_in_between_two_numbers(a, b, x):
    # check if x is in between a and b
    return True if ((x - a) * (x - b)) < 0 else False

def check_intersection(point1, point2, point3, point4):
    # point1 and point2 are the first_direction_list points
    # point3 and point4 are the second_direction_list points

    x_axis = check_in_between_two_numbers(point1[0], point2[0], point3[0])    
    y_axis = check_in_between_two_numbers(point3[1], point4[1], point1[1])

    if (x_axis and y_axis):
        # (point3[0], point1[1]) is the intersection point
        return (point3[0], point1[1])

    return -1

def get_minimum_distance(intersections):
    return min([(abs(item[0]) + abs(item[1])) for item in intersections])

def get_minimum_steps(steps_in_intersection):
    return min(steps_in_intersection)

def merge_input_find_intersection_and_steps(moving_input_1, moving_input_2):
    first_direction_list, first_direction_step_list = get_direction_points(moving_input_1)
    second_direction_list, second_direction_step_list = get_direction_points(moving_input_2)

    first_direction_list_count = len(first_direction_list) - 1
    second_direction_list_count = len(second_direction_list) - 1

    steps_in_intersection = []
    intersections = []
    for i in range(first_direction_list_count):

        for j in range(second_direction_list_count):
            # point1 and point2 are the first_direction_list points
            point1, point2 = first_direction_list[i], first_direction_list[i+1]
            # point3 and point4 are the second_direction_list points
            point3, point4 = second_direction_list[j], second_direction_list[j+1]

            if (point1[0] == point2[0]):
                point1, point2, point3, point4 = point3, point4, point1, point2

            distance = check_intersection(point1, point2, point3, point4)

            if ( distance != -1):
                intersections.append(distance)

                step_x = first_direction_step_list[i] - abs(point2[0] - distance[0])
                step_y = second_direction_step_list[j] - abs(point4[1] - distance[1])

                steps_in_intersection.append( step_x + step_y )
    
    return intersections, steps_in_intersection


moving_input_1 = moving_input_1.split(',')
moving_input_2 = moving_input_2.split(',')

intersections, steps_in_intersection = merge_input_find_intersection_and_steps(moving_input_1, moving_input_2)

distance = get_minimum_distance(intersections)
steps = get_minimum_steps(steps_in_intersection)

print(f"Minimum distance is {distance} with {steps} combined steps")
