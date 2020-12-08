import sys


class ProgramEnvironment:
    def __init__(self):
        self.acc = 0
        self.current_line_no = None
        self.visited_line_nos = set()
        self.max_line = None
        self.normal_terminated = False

    def execute_instructions(self, code):
        new_line_no = 0
        self.max_line = max(code.keys())

        while new_line_no is not False:
            self.current_line_no = new_line_no

            current_line = code[self.current_line_no]

            new_line_no = self.execute_instruction(self.current_line_no,
                                                   current_line[0],
                                                   current_line[1])

        return self.normal_terminated, self.acc

    def execute_instruction(self, line_no, instruction, argument):
        if self.detect_loop(line_no):
            print('loop detected')
            return False

        if instruction == 'nop':
            new_line = self.execute_nop(line_no, argument)
        elif instruction == 'acc':
            new_line = self.execute_acc(line_no, argument)
        elif instruction == 'jmp':
            new_line = self.execute_jmp(line_no, argument)
        else:
            raise ValueError('invalid instruction')

        self.visited_line_nos.add(line_no)

        if new_line > self.max_line:
            self.normal_terminated = True
            return False

        return new_line

    def execute_nop(self, line_no, argument):
        return line_no + 1

    def execute_acc(self, line_no, argument):
        self.acc += int(argument)

        return line_no + 1

    def execute_jmp(self, line_no, argument):
        return line_no + int(argument)

    def detect_loop(self, line_no):
        if line_no in self.visited_line_nos:
            return True

        return False


def permutate_code(code):
    permutations = list()
    change_dict = {
        'jmp': 'nop',
        'nop': 'jmp'
    }

    for line, instr_arg in code.items():
        if instr_arg[0] in {'jmp', 'nop'}:
            new_code = code.copy()
            new_code[line] = (change_dict[instr_arg[0]], instr_arg[1])
            permutations.append(new_code)

    return permutations


def execute_code(code):
    code_permutations = permutate_code(code)

    print('code_permutations', code_permutations)

    for code_permutation in code_permutations:
        pe = ProgramEnvironment()

        normal_termination, acc_value = pe.execute_instructions(code_permutation)

        if normal_termination:
            return acc_value


def read_code_from_stdin():
    code = list()

    for line in sys.stdin:
        instruction, argument = line.strip().split(' ')

        code.append((instruction, argument))

    return dict(enumerate(code))


def main():
    code = read_code_from_stdin()

    acc_value = execute_code(code)

    print(acc_value)


if __name__ == '__main__':
    main()
