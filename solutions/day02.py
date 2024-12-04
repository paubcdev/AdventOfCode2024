input = open("../inputs/day02")

D = input.read().strip()
lines = D.split("\n")


def is_good(xs):
    inc_or_dec = xs == sorted(xs) or xs == sorted(xs, reverse=True)
    ok = True
    for i in range(len(xs) - 1):
        diff = abs(xs[i] - xs[i + 1])
        if not 1 <= diff <= 3:
            ok = False
    return inc_or_dec and ok


part1 = 0
part2 = 0
for line in lines:
    xs1 = list(map(int, line.split()))
    if is_good(xs1):
        part1 += 1
    # addendum for part 2
    good = False
    for j in range(len(xs1)):
        xs = xs1[:j] + xs1[j + 1 :]
        if is_good(xs):
            good = True
    if good:
        part2 += 1


print(part1)
print(part2)
