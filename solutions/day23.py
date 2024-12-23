from collections import defaultdict
import random

input = open("../inputs/day23")
D = input.read().strip()

E = defaultdict(set)
for line in D.split("\n"):
    (
        a,
        b,
    ) = line.split("-")
    E[a].add(b)
    E[b].add(a)

xs = sorted(E.keys())


def part1(xs):
    part1 = 0
    for i, a in enumerate(xs):
        for j in range(i + 1, len(xs)):
            for k in range(j + 1, len(xs)):
                b = xs[j]
                c = xs[k]
                if a in E[b] and a in E[c] and b in E[c]:
                    if a.startswith("t") or b.startswith("t") or c.startswith("t"):
                        part1 += 1
    return part1


def part2(xs):
    best = None
    for t in range(1000):
        random.shuffle(xs)
        clique = []
        for x in xs:
            ok = True
            for y in clique:
                if x not in E[y]:
                    ok = False
            if ok:
                clique.append(x)
        if best is None or len(clique) > len(best):
            best = clique
    return ",".join(sorted(best))


print(part1(xs))
print(part2(xs))
