def parse_line(instruction) -> tuple:
    t = instruction.split()
    return t[0], int(t[1])


def run(program):
    line_executed = [False] * len(program)
    accumulator = 0
    pc = 0

    while pc < len(program):
        if line_executed[pc]:
            return None
        line_executed[pc] = True
        if program[pc][0] == 'nop':
            pc += 1
        elif program[pc][0] == 'acc':
            accumulator += program[pc][1]
            pc += 1
        elif program[pc][0] == 'jmp':
            pc += program[pc][1]

    return accumulator

def jitter_instruction(i):
    if i[0] == 'nop':
        return ('jmp', i[1])
    if i[0] == 'jmp':
        return ('nop', i[1])
    print(f'Weird instruction: {i}')

def main():
    program = []

    with open('input.p1', 'r') as f:
        program = list(map(parse_line, f))

    op = program.copy()

    for i in range(len(program)):
        # don't jitter acc
        if program[i][0] == 'acc':
            continue

        # jitter the instruction at i
        program[i] = jitter_instruction(program[i])
        result = run(program)
        if result is not None:
            print(f'Result is: {result}')
        else:
            # fix the instruction back
            program[i] = jitter_instruction(program[i])

        # this seems to be giving multiple correct answers??


if __name__ == '__main__':
    main()
