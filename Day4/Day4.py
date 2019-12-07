# ADVENT OF CODE 2019 - Day 4
from collections import Counter

input = "245318-765747"

def compute():
    l_limit, u_limit = input.split("-")
    part_1, part_2 = 0, 0
    # Search all numbers in range  
    for num in range(int(l_limit), int(u_limit)+1):
        if (s:= str(num)) == "".join(sorted(s)): #If number only increases, it will = itself sorted
            c = set(Counter(s).values())

            # PART 1: If 6-digit, to contain duplciates, must have 2,3,4,5,6 in c
            if bool(c & {2,3,4,5,6}):
                part_1 += 1

            # PART 2: If duplicate is not in rest of number, there must be a 2 in c
            if bool(c & {2}):
                part_2 += 1

    return part_1, part_2

if __name__ == "__main__":
    part_1, part_2 = compute()
    print(f"Day2: pt.1 Result: {part_1}")
    print(f"Day2: pt.2 Result: {part_2}")