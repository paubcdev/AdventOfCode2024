input = open("../inputs/day04")
D = input.read().strip()
lines = D.split("\n")

R = len(lines)
C = len(lines[0])

part1 = 0
part2 = 0

for r in range(R):
    for c in range(C):
        if (
            c + 3 < C
            and lines[r][c] == "X"
            and lines[r][c + 1] == "M"
            and lines[r][c + 2] == "A"
            and lines[r][c + 3] == "S"
        ):
            part1 += 1
        if (
            r + 3 < R
            and lines[r][c] == "X"
            and lines[r + 1][c] == "M"
            and lines[r + 2][c] == "A"
            and lines[r + 3][c] == "S"
        ):
            part1 += 1
        if (
            r + 3 < R
            and c + 3 < C
            and lines[r][c] == "X"
            and lines[r + 1][c + 1] == "M"
            and lines[r + 2][c + 2] == "A"
            and lines[r + 3][c + 3] == "S"
        ):
            part1 += 1
        if (
            c + 3 < C
            and lines[r][c] == "S"
            and lines[r][c + 1] == "A"
            and lines[r][c + 2] == "M"
            and lines[r][c + 3] == "X"
        ):
            part1 += 1
        if (
            r + 3 < R
            and lines[r][c] == "S"
            and lines[r + 1][c] == "A"
            and lines[r + 2][c] == "M"
            and lines[r + 3][c] == "X"
        ):
            part1 += 1
        if (
            r + 3 < R
            and c + 3 < C
            and lines[r][c] == "S"
            and lines[r + 1][c + 1] == "A"
            and lines[r + 2][c + 2] == "M"
            and lines[r + 3][c + 3] == "X"
        ):
            part1 += 1
        if (
            r - 3 >= 0
            and c + 3 < C
            and lines[r][c] == "S"
            and lines[r - 1][c + 1] == "A"
            and lines[r - 2][c + 2] == "M"
            and lines[r - 3][c + 3] == "X"
        ):
            part1 += 1
        if (
            r - 3 >= 0
            and c + 3 < C
            and lines[r][c] == "X"
            and lines[r - 1][c + 1] == "M"
            and lines[r - 2][c + 2] == "A"
            and lines[r - 3][c + 3] == "S"
        ):
            part1 += 1

        # part 2 starts here
        if (
            r + 2 < R
            and c + 2 < C
            and lines[r][c] == "M"
            and lines[r + 1][c + 1] == "A"
            and lines[r + 2][c + 2] == "S"
            and lines[r + 2][c] == "M"
            and lines[r][c + 2] == "S"
        ):
            part2 += 1
        if (
            r + 2 < R
            and c + 2 < C
            and lines[r][c] == "M"
            and lines[r + 1][c + 1] == "A"
            and lines[r + 2][c + 2] == "S"
            and lines[r + 2][c] == "S"
            and lines[r][c + 2] == "M"
        ):
            part2 += 1
        if (
            r + 2 < R
            and c + 2 < C
            and lines[r][c] == "S"
            and lines[r + 1][c + 1] == "A"
            and lines[r + 2][c + 2] == "M"
            and lines[r + 2][c] == "M"
            and lines[r][c + 2] == "S"
        ):
            part2 += 1
        if (
            r + 2 < R
            and c + 2 < C
            and lines[r][c] == "S"
            and lines[r + 1][c + 1] == "A"
            and lines[r + 2][c + 2] == "M"
            and lines[r + 2][c] == "S"
            and lines[r][c + 2] == "M"
        ):
            part2 += 1

print(part1)
print(part2)
