# ADVENT OF CODE 2019 - Day 6
import math

# Open file and return lines as list
def load_map():
    with open("input.txt") as fp:
        return map(str.strip, fp.readlines())


"""                     SAN
                        /      
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I 
                 \
                 SAN
"""

def map_objects_1(data):
    objects = {}
    orbits = 0

    for orbit in data:
        objA, objB = orbit.split(")")
        objects[objB] = objA

    for obj in objects:
        lorb = 1
        a = objects[obj]
        while a in objects:
            b = a
            a = objects[a]
            lorb += 1
        orbits += lorb
        
    return orbits

def find_path(graph, start, end, path=[]):
    path = path + [start]
    print(path)
    if start == end:
        return path
    if start not in graph:
        print("start not in graph")
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: 
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def map_objects_2(data):
    objects = {}

    for orbit in data:
        objA, objB = orbit.split(')')
        objects[objB] = [objA]
        if objA in objects:
            objects[objA].append(objB)

    return find_path(objects, "SAN", "YOU")

def generate_orbit_map(data):
    return dict(reversed(orbit.split(")")) for orbit in data)

def get_path(orbit_map, val):
    path = []
    for val in iter(lambda: orbit_map.get(val), None):
        path.append(val)
    return path

def part_1():
    orbit_map = generate_orbit_map(load_map())
    return sum(len(get_path(orbit_map, obj)) for obj in orbit_map)
    
def part_2():
    orbit_map = generate_orbit_map(load_map())
    you_path = set(get_path(orbit_map, "YOU"))
    san_path = set(get_path(orbit_map, "SAN"))
    return len(you_path^san_path)

if __name__ == "__main__":
    print(f"Day2: pt.1 Result: {part_1()}")
    print(f"Day2: pt.2 Result: {part_2()}")