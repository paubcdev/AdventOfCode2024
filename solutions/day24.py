def part1():
    def read_input_file(file_path: str) -> list[str]:
        with open(file=file_path, mode="r") as input_file:
            lines = input_file.readlines()
            return [line.strip() for line in lines]

    def solution(lines: list[str]):
        divider = lines.index("")
        initial_wires = lines[:divider]
        configurations = lines[divider + 1 :]

        wires_map = {}
        unprocessed_gates = set()
        ready_gates = set()
        z_outputs = []

        for wires in initial_wires:
            wire_name, wire_value = [wire.strip() for wire in wires.split(":")]

            if wire_name not in wires_map:
                wires_map[wire_name] = bool(int(wire_value))

        for gates in configurations:
            input_config, output_wire = gates.split(" -> ")
            wire_a, gate_type, wire_b = input_config.split(" ")

            if (wire_a in wires_map) and (wire_b in wires_map):
                ready_gates.add((wire_a, wire_b, gate_type, output_wire))
            else:
                unprocessed_gates.add((wire_a, wire_b, gate_type, output_wire))

        while True:
            while ready_gates:
                wire_a, wire_b, gate_type, output_wire = ready_gates.pop()

                if gate_type == "AND":
                    output_wire_value = wires_map[wire_a] and wires_map[wire_b]
                elif gate_type == "OR":
                    output_wire_value = wires_map[wire_a] or wires_map[wire_b]
                else:
                    output_wire_value = wires_map[wire_a] != wires_map[wire_b]

                wires_map[output_wire] = output_wire_value
                if output_wire.startswith("z"):
                    z_outputs.append((output_wire, output_wire_value))

            if not unprocessed_gates:
                break

            for wire_a, wire_b, gate_type, output_wire in list(unprocessed_gates):
                if (wire_a in wires_map) and (wire_b in wires_map):
                    ready_gates.add((wire_a, wire_b, gate_type, output_wire))
                    unprocessed_gates.remove((wire_a, wire_b, gate_type, output_wire))

        binary_num = ""
        for _, wire_value in sorted(z_outputs):
            binary_num = str(int(wire_value)) + binary_num

        print(int(binary_num, 2))

    lines = read_input_file(file_path="../inputs/day24")
    solution(lines)


def part2():
    def read_input_file(file_path: str) -> list[str]:
        with open(file=file_path, mode="r") as input_file:
            lines = input_file.readlines()
            return [line.strip() for line in lines]

    def find_gate(x_wire: str, y_wire: str, gate_type: str, configurations: list[str]):
        sub_str_a = f"{x_wire} {gate_type} {y_wire} -> "
        sub_str_b = f"{y_wire} {gate_type} {x_wire} -> "

        for config in configurations:
            if (sub_str_a in config) or (sub_str_b in config):
                return config.split(" -> ")[-1]

    def swap_output_wires(wire_a: str, wire_b: str, configurations: list[str]):
        new_configurations = []

        for config in configurations:
            input_wires, output_wire = config.split(" -> ")

            if output_wire == wire_a:
                new_configurations.append(" -> ".join([input_wires] + [wire_b]))

            elif output_wire == wire_b:
                new_configurations.append(" -> ".join([input_wires] + [wire_a]))

            else:
                new_configurations.append(" -> ".join([input_wires] + [output_wire]))

        return new_configurations

    def check_parallel_adders(configurations: list[str]):
        current_carry_wire = None
        swaps = []
        bit = 0

        while True:
            x_wire = f"x{bit:02d}"
            y_wire = f"y{bit:02d}"
            z_wire = f"z{bit:02d}"

            if bit == 0:
                current_carry_wire = find_gate(x_wire, y_wire, "AND", configurations)
            else:
                ab_xor_gate = find_gate(x_wire, y_wire, "XOR", configurations)
                ab_and_gate = find_gate(x_wire, y_wire, "AND", configurations)

                cin_ab_xor_gate = find_gate(
                    ab_xor_gate, current_carry_wire, "XOR", configurations
                )
                if cin_ab_xor_gate is None:
                    swaps.append(ab_xor_gate)
                    swaps.append(ab_and_gate)
                    configurations = swap_output_wires(
                        ab_xor_gate, ab_and_gate, configurations
                    )
                    bit = 0
                    continue

                if cin_ab_xor_gate != z_wire:
                    swaps.append(cin_ab_xor_gate)
                    swaps.append(z_wire)
                    configurations = swap_output_wires(
                        cin_ab_xor_gate, z_wire, configurations
                    )
                    bit = 0
                    continue

                cin_ab_and_gate = find_gate(
                    ab_xor_gate, current_carry_wire, "AND", configurations
                )

                carry_wire = find_gate(
                    ab_and_gate, cin_ab_and_gate, "OR", configurations
                )
                current_carry_wire = carry_wire

            bit += 1
            if bit >= 45:
                break

        return swaps

    def solution(lines: list[str]):
        divider = lines.index("")
        configurations = lines[divider + 1 :]

        swaps = check_parallel_adders(configurations)
        print(",".join(sorted(swaps)))

    lines = read_input_file(file_path="../inputs/day24")
    solution(lines)


part1()
part2()
