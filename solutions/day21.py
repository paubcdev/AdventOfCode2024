import heapq
import re
from collections import deque
from copy import deepcopy


def ints(s):
    return [int(x) for x in re.findall("-?\d+", s)]


input = open("../inputs/day21")
ans = 0
D = input.read().strip()

pad1 = ["789", "456", "123", " 0A"]
pad2 = [" ^A", "<v>"]


def getPad1(part1):
    r, c = part1
    if not (0 <= r < len(pad1) and 0 <= c < len(pad1[r])):
        return None
    if pad1[r][c] == " ":
        return None
    return pad1[r][c]


def getPad2(p):
    r, c = p
    if not (0 <= r < len(pad2) and 0 <= c < len(pad2[r])):
        return None
    if pad2[r][c] == " ":
        return None
    return pad2[r][c]


def applyPad1(p, move):
    if move == "A":
        return (p, getPad1(p))
    elif move == "<":
        return ((p[0], p[1] - 1), None)
    elif move == "^":
        return ((p[0] - 1, p[1]), None)
    elif move == ">":
        return ((p[0], p[1] + 1), None)
    elif move == "v":
        return ((p[0] + 1, p[1]), None)


def applyPad2(p, move):
    if move == "A":
        return (p, getPad2(p))
    elif move == "<":
        return ((p[0], p[1] - 1), None)
    elif move == "^":
        return ((p[0] - 1, p[1]), None)
    elif move == ">":
        return ((p[0], p[1] + 1), None)
    elif move == "v":
        return ((p[0] + 1, p[1]), None)


def solve1(code, pads):
    start = [0, (3, 2), "A", "", ""]
    Q = []
    heapq.heappush(Q, start)
    SEEN = {}
    while Q:
        d, part1, part2, out, path = heapq.heappop(Q)
        assert part2 in ["<", ">", "v", "^", "A"]
        if out == code:
            return d
        if not code.startswith(out):
            continue
        if getPad1(part1) is None:
            continue
        key = (part1, part2, out)
        if key in SEEN:
            assert d >= SEEN[key], f"{key=} {d=} {SEEN[key]=}"
            continue
        SEEN[key] = d
        for move in ["^", "<", "v", ">", "A"]:
            new_part1 = part1
            new_out = out
            new_part1, output = applyPad1(part1, move)
            if output is not None:
                new_out = out + output
            cost_move = cost2(move, part2, pads)
            new_path = path
            assert cost_move >= 0
            heapq.heappush(Q, [d + cost_move, new_part1, move, new_out, new_path])


def cost2_slow(ch, prev_move, pads):
    start_pos = {"^": (0, 1), "<": (1, 0), "v": (1, 1), ">": (1, 2), "A": (0, 2)}[
        prev_move
    ]
    start = [0, start_pos, ""]
    for _ in range(pads - 1):
        start.append((0, 2))
    Q = deque([start])
    SEEN = set()
    while Q:
        d, part1, path, *ps = Q.popleft()
        key = (part1, tuple(ps))
        if key in SEEN:
            continue
        if getPad2(part1) is None:
            continue
        ok = True
        for p in ps:
            if getPad2(p) is None:
                ok = False
                break
        if not ok:
            continue
        SEEN.add(key)
        for move in ["^", "<", "v", ">", "A"]:
            new_part1 = part1
            new_ps = deepcopy(ps)
            new_move = move
            for i, p in reversed(list(enumerate(ps))):
                new_ps[i], new_move = applyPad2(ps[i], new_move)
                if new_move is None:
                    break
                else:
                    for j in range(len(ps)):
                        if j > i:
                            assert new_ps[j] == (0, 2)
            if new_move is not None:
                new_part1, output = applyPad2(part1, new_move)
                if output == ch:
                    return path + move
            Q.append([d + 1, new_part1, path + move] + new_ps)
    assert False, f"{ch=} {prev_move=} {pads=}"


DP = {}


def cost2(ch, prev_move, pads):
    key = (ch, prev_move, pads)
    if key in DP:
        return DP[key]
    if pads == 0:
        return 1
    else:
        assert ch in ["^", ">", "v", "<", "A"]
        assert prev_move in ["^", ">", "v", "<", "A"]
        assert pads >= 1
        Q = []
        start_pos = {"^": (0, 1), "<": (1, 0), "v": (1, 1), ">": (1, 2), "A": (0, 2)}[
            prev_move
        ]
        heapq.heappush(Q, [0, start_pos, "A", "", ""])
        SEEN = {}
        while Q:
            d, p, prev, out, path = heapq.heappop(Q)
            if getPad2(p) is None:
                continue
            if out == ch:
                DP[key] = d
                return d
            elif len(out) > 0:
                continue
            seen_key = (p, prev)
            if seen_key in SEEN:
                assert d >= SEEN[seen_key]
                continue
            SEEN[seen_key] = d
            for move in ["^", "<", "v", ">", "A"]:
                new_p, output = applyPad2(p, move)
                cost_move = cost2(move, prev, pads - 1)
                new_d = d + cost_move
                new_path = path
                new_out = out
                if output is not None:
                    new_out = new_out + output
                heapq.heappush(Q, [new_d, new_p, move, new_out, new_path])
        assert False, f"{ch=} {pads=}"


def solve2(code):
    start = [0, (0, 2), "", ""]
    Q = deque([start])
    SEEN = set()
    while Q:
        d, p, out, path = Q.popleft()
        key = (p, out)
        if out == code:
            yield path
        if not code.startswith(out):
            continue
        if key in SEEN:
            continue
        SEEN.add(key)
        if getPad2(p) is None:
            continue
        for move in ["^", "<", "v", ">", "A"]:
            new_p = p
            new_out = out
            new_p, output = applyPad2(p, move)
            if output is not None:
                new_out = out + output
            heapq.heappush(Q, [d + 1, new_p, new_out, path + move])


def slowSolve(code, PADS):
    start = [0, (3, 2), "", ""]
    for _ in range(PADS):
        start.append((0, 2))
    Q = deque([start])
    SEEN = set()
    while Q:
        d, part1, out, path, *ps = Q.popleft()
        key = (part1, out, tuple(ps))
        if out == code:
            return path
        if not code.startswith(out):
            continue
        if key in SEEN:
            continue
        if getPad1(part1) is None:
            continue
        ok = True
        for p in ps:
            if getPad2(p) is None:
                ok = False
                break
        if not ok:
            continue
        SEEN.add(key)
        if len(SEEN) % 10**5 == 0:
            print(len(SEEN), key)
        for move in ["^", "<", "v", ">", "A"]:
            new_part1 = part1
            new_out = out
            new_ps = deepcopy(ps)
            new_move = move

            for i, p in reversed(list(enumerate(ps))):
                new_ps[i], new_move = applyPad2(ps[i], new_move)
                if new_move is None:
                    break
                else:
                    for j in range(len(ps)):
                        if j > i:
                            assert new_ps[j] == (0, 2)
            if new_move is not None:
                new_part1, output = applyPad1(part1, new_move)
                if output is not None:
                    new_out = out + output
            Q.append([d + 1, new_part1, new_out, path + move] + new_ps)


part1 = 0
part2 = 0
for line in D.split("\n"):
    s1 = solve1(line, 2)
    s2 = solve1(line, 25)
    line_int = ints(line)[0]
    part1 += line_int * s1
    part2 += line_int * s2
print(part1)
print(part2)
