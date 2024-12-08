from collections import defaultdict

input = open("../inputs/day08")

part1 = 0
part2 = 0

D = input.read().strip()
lines = D.split("\n")
R = len(lines)
C = len(lines[0])
P = defaultdict(list)
for r in range(R):
    for c in range(C):
        if lines[r][c] != ".":
            P[lines[r][c]].append((r, c))

A1 = set()
A2 = set()
for r in range(R):
    for c in range(C):
        for k, vs in P.items():
            for r1, c1 in vs:
                for r2, c2 in vs:
                    if (r1, c1) != (r2, c2):
                        d1 = abs(r - r1) + abs(c - c1)
                        d2 = abs(r - r2) + abs(c - c2)

                        dr1 = r - r1
                        dr2 = r - r2
                        dc1 = c - c1
                        dc2 = c - c2

                        if (
                            (d1 == 2 * d2 or d1 * 2 == d2)
                            and 0 <= r < R
                            and 0 <= c < C
                            and (dr1 * dc2 == dc1 * dr2)
                        ):
                            A1.add((r, c))
                        if 0 <= r < R and 0 <= c < C and (dr1 * dc2 == dc1 * dr2):
                            A2.add((r, c))


part1 = len(A1)
part2 = len(A2)
print(part1)
print(part2)
