input = open("../inputs/day19")

D = input.read().strip()
words, targets = D.split("\n\n")
words = words.split(", ")

part1 = 0
part2 = 0
DP = {}


def ways(words, target):
    if target in DP:
        return DP[target]
    ans = 0
    if not target:
        ans = 1
    for word in words:
        if target.startswith(word):
            ans += ways(words, target[len(word) :])
    DP[target] = ans
    return ans


for target in targets.split("\n"):
    target_ways = ways(words, target)
    if target_ways > 0:
        part1 += 1
    part2 += target_ways

print(part1)
print(part2)
