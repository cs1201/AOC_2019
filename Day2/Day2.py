# ADVENT OF CODE 2019 - Day 2

# Open file and return data as list
with open("input.txt") as fp:
    # Delimit input by , and convert to int
    data = list(map(int, fp.read().split(',')))



print(data)
