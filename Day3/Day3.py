# ADVENT OF CODE 2019 - Day 3
import math
from itertools import accumulate, count

# Open file and return lines as list
with open("input.txt") as fp:
    data = fp.readlines()
    wires = list(l.split(',') for l in data)

move = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}

def get_steps(wire):
    step = (move[inst[0]] for inst in wire for _ in range(int(inst[1:])))
    return dict(reversed(list(zip(zip(*map(accumulate, zip(*step))), count(1)))))

def manhattan(point):
    return (abs(point[0]) + abs(point[1]))

route1 = get_steps(wires[0])
route2 = get_steps(wires[1])

# Get duplicate points in each route
duplicate_points = set(route1.keys()) & set(route2.keys())

def part_1():
    return min(map(manhattan, duplicate_points))

def part_2():
    # Get distance for each duplicate point
    distances = ((route1[p], route2[p]) for p in duplicate_points)
    return int(min(map(sum, distances)))

if __name__ == "__main__":
    print(f"Day2: pt.1 Result: {part_1()}")
    print(f"Day2: pt.2 Result: {part_2()}")