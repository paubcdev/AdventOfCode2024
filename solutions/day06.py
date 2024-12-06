input = open("../inputs/day06")

part1 = 0
part2 = 0

D = input.read().strip()

lines = D.split('\n')
R = len(lines)
C = len(lines[0])

for r in range(R):
    for c in range(C):
        if lines[r][c] == '^':
            sr,sc = r,c

for o_r in range(R):
    for o_c in range(C):
        r,c = sr,sc
        d = 0
        SEEN = set()
        SEEN_RC = set()
        while True:
            if (r,c,d) in SEEN:
                part2 += 1
                break
            SEEN.add((r,c,d))
            SEEN_RC.add((r,c))
            dr,dc = [(-1,0),(0,1),(1,0),(0,-1)][d]
            rr = r+dr
            cc = c+dc
            if not (0<=rr<R and 0<=cc<C):
                if lines[o_r][o_c]=='#':
                    part1 = len(SEEN_RC)
                break
            if lines[rr][cc]=='#' or rr==o_r and cc==o_c:
                d = (d+1)%4
            else:
                r = rr
                c = cc
print(part1)
print(part2)
