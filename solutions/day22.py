input = open("../inputs/day22")
D = input.read().strip()


def mix(x, y):
    return x ^ y


def prune(x):
    return x % 16777216


def prices(x):
    ans = [x]
    for _ in range(2000):
        x = prune(mix(x, 64 * x))
        x = prune(mix(x, x // 32))
        x = prune(mix(x, x * 2048))
        ans.append(x)
    return ans


def changes(P):
    return [P[i + 1] - P[i] for i in range(len(P) - 1)]


def getScores(P, C):
    ANS = {}
    for i in range(len(C) - 3):
        pattern = (C[i], C[i + 1], C[i + 2], C[i + 3])
        if pattern not in ANS:
            ANS[pattern] = P[i + 4]
    return ANS


part1 = 0
SCORE = {}
for line in D.split("\n"):
    P = prices(int(line))
    part1 += P[-1]
    P = [x % 10 for x in P]
    C = changes(P)
    S = getScores(P, C)
    for k, v in S.items():
        if k not in SCORE:
            SCORE[k] = v
        else:
            SCORE[k] += v
print(part1)
print(max(SCORE.values()))
