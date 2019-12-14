# ADVENT OF CODE 2019 - Day 1
import math

def load_data():
    # Open file and return lines as list
    with open("input.txt") as fp:
        data = list(map(int, fp.read().split(',')))
        return data

def compute_alt(mem, start_index, input_val):
    i = start_index #Mem index
    op = -1 #OP code
    dc = [] #diagnostic code

    while True:
        # Read op 
        op = str(mem[i])
        
        pm1, pm2 = 0, 0
        # If param_modes in op_code
        if len(op) > 2:
            # Get param_mode 1
            pm1 = int(op[-3])
            # If non-zero, get param_mode 2
            if len(op) > 3:
                pm2 = 1
            op = op[-1]
        op = int(op)

        if op == 99:
            return dc

        p1 = mem[i+1] if pm1==1 else mem[mem[i+1]]
        if op in [1, 2, 5, 6, 7, 8]: #Only these op-codes take a 2nd/3rd parameter
            p2 = mem[i+2] if pm2==1 else mem[mem[i+2]]
            p3 = mem[i+3]

        # Execute instruction
        if op == 1: #ADD
            mem[p3] = p1 + p2
            i += 4
        elif op == 2: #MULTIPLY
            mem[p3] = p1 * p2
            i += 4
        elif op == 3: #INPUT
            mem[mem[i+1]] = input_val
            i += 2
        elif op == 4: #OUTPUT
            dc.append(p1)
            i += 2
        elif op == 5: #JUMP-IF-TRUE
            i = p2 if p1 else i+3
        elif op == 6: #JUMP-IF-FALSE
            i = p2 if not p1 else i+3
        elif op == 7: #LESS THAN
            mem[p3] = 1 if p1 < p2 else 0
            i += 4
        elif op == 8: #EQUALS
            mem[p3] = 1 if p1 == p2 else 0
            i += 4


def part_1():
    data = load_data()
    output_code = compute_alt(data, start_index=0, input_val=1)
    result = output_code.pop()
    return result

def part_2():
    data = load_data()
    output_code = compute_alt(data, start_index=0, input_val=5)
    result = output_code.pop()
    return result


if __name__ == "__main__":
    print(f"Day2: pt.1 Result: {part_1()}")
    print(f"Day2: pt.2 Result: {part_2()}")