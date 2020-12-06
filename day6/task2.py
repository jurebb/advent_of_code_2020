import sys


def extract_count_groups_from_stdin(groups):
    current_group = set()
    sum_of_pos_answers = 0
    new_current = True

    for line in sys.stdin:
        line = line.strip()

        if line == '':

            if current_group:
                groups.append(current_group)

                sum_of_pos_answers += len(current_group)

            new_current = True
            current_group = set()

        elif new_current:
            current_group = set(line)
            new_current = False

        else:
            new_current = False
            current_group &= set(line)

        print('cg', current_group)

    if current_group:
        groups.append(current_group)

        sum_of_pos_answers += len(current_group)

    return sum_of_pos_answers


def main():
    groups = list()

    sum_of_pos_answers = extract_count_groups_from_stdin(groups)

    print(groups)
    print(sum_of_pos_answers)


if __name__ == '__main__':
    main()
