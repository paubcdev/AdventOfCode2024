input = open("../inputs/day07")

part1 = 0
part2 = 0

D = input.read().strip()


def is_valid(target, ns, part2):
    if len(ns) == 1:
        return ns[0] == target
    if is_valid(target, [ns[0] + ns[1]] + ns[2:], part2):
        return True
    if is_valid(target, [ns[0] * ns[1]] + ns[2:], part2):
        return True
    if part2 and is_valid(target, [int(str(ns[0]) + str(ns[1]))] + ns[2:], part2):
        return True
    return False


for line in D.split("\n"):
    target, ns = line.split(":")
    target = int(target)
    ns = [int(x) for x in ns.strip().split()]
    if is_valid(target, ns, part2=False):
        part1 += target
    if is_valid(target, ns, part2=True):
        part2 += target

print(part1)
print(part2)
