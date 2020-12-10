def parse_line(instruction) -> tuple:
    t = instruction.split()
    return t[0], int(t[1])


def main():
    program = []

    with open('test.p1', 'r') as f:
        program = list(map(parse_line, f))

    line_executed = [False] * len(program)
    accumulator = 0
    pc = 0

    while True:
        if line_executed[pc]:
            break
        line_executed[pc] = True
        if program[pc][0] == 'nop':
            pc += 1
        elif program[pc][0] == 'acc':
            accumulator += program[pc][1]
            pc += 1
        elif program[pc][0] == 'jmp':
            pc += program[pc][1]

    print(f'Accumulator Before Loop: {accumulator}')


if __name__ == '__main__':
    main()
