import copy

with open("../inputs/day17") as f:
    registers, programs = f.read().split("\n\n")

programs = [int(num) for num in programs.replace("\n", "").split()[1].split(",")]  # noqa
registers = {
    line.split(": ")[0].split()[1]: int(line.split(": ")[1])
    for line in registers.splitlines()
}
registers_original = {
    line.split(": ")[0].split()[1]: int(line.split(": ")[1])
    for line in registers.splitlines()
}


outputs = []


def part1(programs, registers):
    def combo(num, registers):
        if num <= 3:
            return num
        elif num == 4:
            return registers["A"]
        elif num == 5:
            return registers["B"]
        elif num == 6:
            return registers["C"]

    def adv(num, registers, instr):
        registers["A"] = registers["A"] // (2 ** combo(num, registers))
        return registers, instr + 2

    def bxl(num, registers, instr):
        registers["B"] = registers["B"] ^ num
        return registers, instr + 2

    def bst(num, registers, instr):
        registers["B"] = combo(num, registers) % 8
        return registers, instr + 2

    def jnz(num, registers, instr):
        if registers["A"] == 0:
            return registers, instr + 2
        else:
            return registers, num

    def bxc(num, registers, instr):
        registers["B"] = registers["B"] ^ registers["C"]
        return registers, instr + 2

    def out(num, registers, instr):
        outputs.append(combo(num, registers) % 8)
        return registers, instr + 2

    def bdv(num, registers, instr):
        registers["B"] = registers["A"] // (2 ** combo(num, registers))
        return registers, instr + 2

    def cdv(num, registers, instr):
        registers["C"] = registers["A"] // (2 ** combo(num, registers))
        return registers, instr + 2

    length = len(programs)
    instr = 0
    while instr in range(length):
        opcode = programs[instr]
        function = [adv, bxl, bst, jnz, bxc, out, bdv, cdv][opcode]
        num = programs[instr + 1]
        registers, instr = function(num, registers, instr)

    answer = ",".join(str(num) for num in outputs)
    return answer


def part2(programs, registers_original):
    def combo(num, registers):
        if num <= 3:
            return num
        elif num == 4:
            return registers["A"]
        elif num == 5:
            return registers["B"]
        elif num == 6:
            return registers["C"]

    def adv(num, registers, instr, outputs):
        registers["A"] = registers["A"] // (2 ** combo(num, registers))
        return registers, instr + 2, outputs

    def bxl(num, registers, instr, outputs):
        registers["B"] = registers["B"] ^ num
        return registers, instr + 2, outputs

    def bst(num, registers, instr, outputs):
        registers["B"] = combo(num, registers) % 8
        return registers, instr + 2, outputs

    def jnz(num, registers, instr, outputs):
        if registers["A"] == 0:
            return registers, instr + 2, outputs
        else:
            return registers, num, outputs

    def bxc(num, registers, instr, outputs):
        registers["B"] = registers["B"] ^ registers["C"]
        return registers, instr + 2, outputs

    def out(num, registers, instr, outputs):
        outputs.append(combo(num, registers) % 8)
        return registers, instr + 2, outputs

    def bdv(num, registers, instr, outputs):
        registers["B"] = registers["A"] // (2 ** combo(num, registers))
        return registers, instr + 2, outputs

    def cdv(num, registers, instr, outputs):
        registers["C"] = registers["A"] // (2 ** combo(num, registers))
        return registers, instr + 2, outputs

    def get_output(a):
        outputs = []
        registers = copy.deepcopy(registers_original)
        registers["A"] = a
        length = len(programs)
        instr = 0
        while instr in range(length):
            opcode = programs[instr]
            function = [adv, bxl, bst, jnz, bxc, out, bdv, cdv][opcode]
            num = programs[instr + 1]
            registers, instr, outputs = function(num, registers, instr, outputs)  # noqa
        return outputs

    valid = [0]
    for length in range(1, len(programs) + 1):
        oldvalid = valid
        valid = []
        for num in oldvalid:
            for offset in range(8):
                newnum = 8 * num + offset
                if get_output(newnum) == programs[-length:]:
                    valid.append(newnum)

    answer = min(valid)
    return answer


print(part1(programs, registers))
print(part2(programs, registers_original))
