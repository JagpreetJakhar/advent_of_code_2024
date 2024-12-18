file_path = 'data_17.txt'
#file_path='sample_17.txt'
registers=[]
program=[]
from collections import defaultdict,deque
import heapq
import re
from itertools import count
with open(file_path, "r") as file:
    data = file.readlines()
    for line in data :
        if match := re.match(r"Register A: (\d+)", line):
            registers.append(int(match.group(1)))
        elif match := re.match(r"Register B: (\d+)", line):
            registers.append(int(match.group(1)))
        elif match := re.match(r"Register C: (\d+)", line):
            registers.append(int(match.group(1)))
        elif match := re.match(r"Program: ([\d,]+)", line):
            program = list(map(int, match.group(1).split(',')))
print(registers,program)
def run(A):
    ptr = 0
    B = 0
    C = 0
    result = []
    while True:
        try:
            ins = program[ptr]
            op = program[ptr + 1]
        except:
            return result
        if op <= 3:
            combo = op
        elif op == 4:
            combo = A
        elif op == 5:
            combo = B
        elif op == 6:
            combo = C

        match ins:
            case 0:
                A //= 2**combo
            case 1:
                B ^= op
            case 2:
                B = combo % 8
            case 3:
                if A != 0:
                    ptr = op - 2
            case 4:
                B ^= C
            case 5:
                result.append(combo % 8)
            case 6:
                B = A // (2**combo)
            case 7:
                C = A // (2**combo)
        ptr += 2


print(run(registers[0]))
mid = int(next(A for i in count() if len(run(A := 10**i)) == len(program))) * 10
width = mid
spacing = width // 1000
for matching_digits in range(1, len(program) + 1):
    for A in range(mid - width, mid + width, spacing):
        res = run(A)
        if (
            len(res) == len(program)
            and res[-matching_digits:] == program[-matching_digits:]
        ):
            break
    else:
        assert False
    mid = A
    spacing //= 10
    width //= 10
    if spacing <= 10:
        spacing = 1
    if width <= 10000:
        width = 100000

print(A)
