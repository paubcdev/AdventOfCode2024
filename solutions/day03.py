import re

input = open("../inputs/day03")

D = input.read().strip()

part1 = 0
part2 = 0

enabled = True

for i in range(len(D)):
    if D[i:].startswith('do()'):
        enabled = True
    if D[i:].startswith("don't()"):
        enabled = False
    instruction = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', D[i:])
    if instruction is not None:
        x, y = int(instruction.group(1)), int(instruction.group(2))
        part1 += x*y
        if enabled:
            part2 += x*y

print(part1)
print(part2)
