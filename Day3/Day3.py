# ADVENT OF CODE 2019 - Day 1
import math

# Open file and return lines as list
with open("input.txt") as fp:
    data = fp.readlines()
    lines = list(l.split(',') for l in data)

line1, line2 = lines[:2]

def part_1():
    central_pos = (0, 0)
    current_pos = central_pos
    all_points_visited = []
    duplicate_points = []

    for (num, line) in enumerate(lines):  
        print(line)
        print(num)
        current_pos = (0,0)
        line_points_visted = []
        # For each move extract direction and distance
        for move in line:
            direction, distance = move[0], int(move[1:])

            # Determine new line position and points visited in between
            if direction == "R":
                new_pos = (current_pos[0] + distance, current_pos[1])
                points_visited = list((x , current_pos[1]) for x in range(current_pos[0], new_pos[0]))
            elif direction == "L":
                new_pos = (current_pos[0] - distance, current_pos[1])
                points_visited = list((x , current_pos[1]) for x in range(current_pos[0], new_pos[0], -1))
            elif direction == "U":
                new_pos= (current_pos[0], current_pos[1] + distance)
                points_visited = list((current_pos[0] , y) for y in range(current_pos[1], new_pos[1]))
            elif direction == "D":
                new_pos = (current_pos[0], current_pos[1] - distance)
                points_visited = list((current_pos[0] , y) for y in range(current_pos[1], new_pos[1], -1))
            else:
                raise Exception(f"part1: Undefined direction {direction}")

            current_pos = new_pos

            # Add points visited in this move to line total
            line_points_visted.extend(list(point for point in points_visited))

        all_points_visited.append(line_points_visted)

    if all_points_visited[0] == all_points_visited[1]:
        print("0 = 1")

    # Find duplicates
    duplicate_points = list(set(all_points_visited[0]).intersection(all_points_visited[1]))
    duplicate_points = [i for i in duplicate_points if i != (0,0)] #Remove (0,0) points from duplicates

    # For all duplicate points, figure out shortest
    if len(duplicate_points) != 0:
        for index, point in enumerate(duplicate_points):
            point = (abs(point[0]), abs(point[1]))
            duplicate_points[index] = point

        shortest = sorted(duplicate_points, key=sum)[0]
        return shortest, sum(shortest)
            
def part_2():
    pass


if __name__ == "__main__":
    print(f"Day2: pt.1 Result: {part_1()}")
    print(f"Day2: pt.2 Result: {part_2()}")