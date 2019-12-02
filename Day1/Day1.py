# ADVENT OF CODE 2019 - Day 1
import math

# Open file and return lines as list
with open("input.txt") as fp:
    data = fp.readlines()

def calculate_fuel(mass):
    return math.floor(mass/3)-2

def calculate_all_fuel(mass):
    while (mass := calculate_fuel(int(mass))) > 0:
        yield mass

def part_1():
    """
    Sum fuel calculation for all masses in input
    """
    result = sum(calculate_fuel(int(mass)) for mass in data)
    print(f"Day 1 pt.1 Result: {result}")

def part_2():
    """
    For each fuel calculation, calculate fuel until req <= 0. Add to total
    """
    total_fuel = sum(f for mass in data for f in calculate_all_fuel(int(mass)))

    print(f"Day 1 pt.2 Result: {total_fuel}")

if __name__ == "__main__":
    part_1()
    part_2()