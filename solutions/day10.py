from collections import deque

input = open("../inputs/day10")
D = input.read().strip().split("\n")

part1 = 0
part2 = 0

G = [[int(x) for x in row] for row in D]
R = len(G)
C = len(G[0])


def ways1(sr, sc):
    Q = deque([(sr, sc)])
    ans = 0
    SEEN = set()
    while Q:
        r, c = Q.popleft()
        if (r, c) in SEEN:
            continue
        SEEN.add((r, c))
        if G[r][c] == 0:
            ans += 1
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == G[r][c] - 1:
                Q.append((rr, cc))
    return ans


DP = {}


def ways2(r, c):
    if G[r][c] == 0:
        return 1
    if (r, c) in DP:
        return DP[(r, c)]
    ans = 0
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        rr = r + dr
        cc = c + dc
        if 0 <= rr < R and 0 <= cc < C and G[rr][cc] == G[r][c] - 1:
            ans += ways2(rr, cc)
    DP[(r, c)] = ans
    return ans


for r in range(R):
    for c in range(C):
        if G[r][c] == 9:
            part1 += ways1(r, c)
            part2 += ways2(r, c)

print(part1)
print(part2)
