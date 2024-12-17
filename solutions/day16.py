import heapq

input = open("../inputs/day16")

G = input.read().strip().split("\n")

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


R = len(G)
C = len(G[0])
G = [[G[r][c] for c in range(C)] for r in range(R)]

for r in range(R):
    for c in range(C):
        if G[r][c] == "S":
            sr, sc = r, c
        if G[r][c] == "E":
            er, ec = r, c

Q = []
SEEN = set()
heapq.heappush(Q, (0, sr, sc, 1))
DIST = {}
best = None


def part1(best):
    while Q:
        d, r, c, dir = heapq.heappop(Q)
        if (r, c, dir) not in DIST:
            DIST[(r, c, dir)] = d
        if r == er and c == ec and best is None:
            best = d
        if (r, c, dir) in SEEN:
            continue
        SEEN.add((r, c, dir))
        dr, dc = DIRS[dir]
        rr, cc = r + dr, c + dc
        if 0 <= cc < C and 0 <= rr < R and G[rr][cc] != "#":
            heapq.heappush(Q, (d + 1, rr, cc, dir))
        heapq.heappush(Q, (d + 1000, r, c, (dir + 1) % 4))
        heapq.heappush(Q, (d + 1000, r, c, (dir + 3) % 4))
    print(best)


def part2(best):
    for dir in range(4):
        heapq.heappush(Q, (0, er, ec, dir))
    DIST2 = {}
    while Q:
        d, r, c, dir = heapq.heappop(Q)
        if (r, c, dir) not in DIST2:
            DIST2[(r, c, dir)] = d
        if (r, c, dir) in SEEN:
            continue
        SEEN.add((r, c, dir))
        dr, dc = DIRS[(dir + 2) % 4]
        rr, cc = r + dr, c + dc
        if 0 <= cc < C and 0 <= rr < R and G[rr][cc] != "#":
            heapq.heappush(Q, (d + 1, rr, cc, dir))
        heapq.heappush(Q, (d + 1000, r, c, (dir + 1) % 4))
        heapq.heappush(Q, (d + 1000, r, c, (dir + 3) % 4))

    OK = set()
    for r in range(R):
        for c in range(C):
            for dir in range(4):
                if (
                    (r, c, dir) in DIST
                    and (r, c, dir) in DIST2
                    and DIST[(r, c, dir)] + DIST2[(r, c, dir)] == best
                ):
                    OK.add((r, c))
    print(len(OK))


part1(best)
part2(best)
