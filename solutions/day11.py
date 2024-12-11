input = open("../inputs/day11")

D = input.read().strip()
D = [int(x) for x in D.split()]

ITER_1 = 25
ITER_2 = 75

part1 = 0
part2 = 0

DP = {}


def solver(x, t):
    if (x, t) in DP:
        return DP[(x, t)]
    if t == 0:
        ret = 1
    elif x == 0:
        ret = solver(1, t - 1)
    elif len(str(x)) % 2 == 0:
        dstr = str(x)
        left = dstr[: len(dstr) // 2]
        right = dstr[len(dstr) // 2 :]
        left, right = (int(left), int(right))
        ret = solver(left, t - 1) + solver(right, t - 1)
    else:
        ret = solver(x * 2024, t - 1)
    DP[(x, t)] = ret
    return ret


def solve_all(t):
    solve = sum(solver(x, t) for x in D)
    return solve


print(solve_all(ITER_1))
print(solve_all(ITER_2))
