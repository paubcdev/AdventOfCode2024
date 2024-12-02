from collections import Counter

input = open("../inputs/day01")

D = input.read().strip()

lines = D.split("\n")

LEFT_COL = []
RIGHT_COL = []
RC = Counter()

for line in lines:
    left, right = line.split()
    left, right = int(left), int(right)
    LEFT_COL.append(left)
    RIGHT_COL.append(right)
    RC[right] += 1

part1 = 0

LEFT_COL = sorted(LEFT_COL)
RIGHT_COL = sorted(RIGHT_COL)

for left, right in zip(LEFT_COL, RIGHT_COL):
    part1 += abs(right-left)

print(part1)

part2 = 0

for left in LEFT_COL:
    part2 += left * RC.get(left, 0)

print(part2)
