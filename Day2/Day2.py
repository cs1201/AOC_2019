# ADVENT OF CODE 2019 - Day 2
# from itertools import xrange

# Open file and return memory as list
with open("input.txt") as fp:
    # Delimit input by , and convert to int
    data = list(map(int, fp.read().split(',')))

def restore_1201():
    memory = data[:]
    # Restore 1201 program status
    memory[1] = 12
    memory[2] = 2
    return memory

def place_noun_verb(noun, verb):
    memory = data[:]
    memory[1] = noun
    memory[2] = verb
    return memory

def compute(memory):
    """
        Performs instructions on memory and returns modified memory set
    """
    op_index = 0
    # Now pass op codes
    while (op_code := memory[op_index]) != 99:
        # Get intcode params
        a, b, c = memory[op_index+1:op_index+4]
        # Perform op
        if op_code == 1:
            memory[c] = memory[a] + memory[b]
        elif op_code == 2:
            memory[c] = memory[a] * memory[b]
        else:
            raise Exception(f"Wrong Op-code: {op_code} at pos: {op_index}")
        # Update op_code
        op_index += 4

    return memory

def part_1():
    memory = compute(restore_1201())
    return memory[0]

def part_2():
    target = 19690720
    for noun, verb in ((a, b) for a in range(100) for b in range(100)):
        if compute(place_noun_verb(noun, verb))[0] == target:
            return 100 * noun + verb


if __name__ == "__main__":
    print(f"Day2: pt.1 Result: {part_1()}")
    print(f"Day2: pt.2 Result: {part_2()}")

