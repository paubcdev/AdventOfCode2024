from collections import defaultdict, deque

input = open("../inputs/day05")
D = input.read().strip()
lines = D.split("\n")

part1 = 0
part2 = 0

edges, queries = D.split("\n\n")


E = defaultdict(set)
ER = defaultdict(set)
for line in edges.split("\n"):
    x, y = line.split("|")
    x, y = int(x), int(y)
    E[y].add(x)
    ER[x].add(y)

for query in queries.split("\n"):
    vs = [int(x) for x in query.split(",")]
    assert len(vs) % 2 == 1
    is_Ok = True
    for i, x in enumerate(vs):
        for j, y in enumerate(vs):
            if i < j and y in E[x]:
                is_Ok = False
    if is_Ok:
        part1 += vs[len(vs) // 2]

    # part 2 starts here
    else:
        good = []
        Q = deque([])
        D = {v: len(E[v] & set(vs)) for v in vs}
        for v in vs:
            if D[v] == 0:
                Q.append(v)
        while Q:
            x = Q.popleft()
            good.append(x)
            for y in ER[x]:
                if y in D:
                    D[y] -= 1
                    if D[y] == 0:
                        Q.append(y)
        part2 += good[len(good) // 2]

print(part1)
print(part2)
