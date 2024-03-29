import itertools
import sys


PREAMBLE_LEN = 25


def update_preamble_combinations(preamble_combinations, els, new_el, oldest_els):
    new_preamble_combinations = dict()
    oldest_el = oldest_els[0]

    for sum, pairs_list in preamble_combinations.items():
        for pair in pairs_list:
            if oldest_el not in pair:
                if sum not in new_preamble_combinations:
                    new_preamble_combinations[sum] = [pair]
                else:
                    new_preamble_combinations[sum].append(pair)

    els.remove(oldest_el)
    oldest_els.remove(oldest_el)

    for el in els:
        sum = el + new_el
        if sum not in new_preamble_combinations:
            new_preamble_combinations[sum] = [(new_el, el)]
        else:
            new_preamble_combinations[sum].append((new_el, el))

    els.add(new_el)
    oldest_els.append(new_el)

    return new_preamble_combinations


def validate_next_entries(preamble_combinations, els, oldest_els, read_lines):
    entry_valid = True

    while entry_valid:
        line = sys.stdin.readline().strip()
        read_lines.append(int(line))

        if line:
            new_el = int(line)
            if new_el in preamble_combinations:
                preamble_combinations = update_preamble_combinations(preamble_combinations, els,
                                                                     new_el, oldest_els)

            else:
                break

        else:
            break

    invalid_num = line

    for line in sys.stdin:
        if line:
            read_lines.append(int(line.strip()))

    return invalid_num, read_lines


def initial_read_preamble(stdin_arg=None):
    preamble = list()
    read_lines = list()

    stdin = sys.stdin if stdin_arg is None else stdin_arg

    for _ in range(PREAMBLE_LEN):
        line = stdin.readline().strip()
        read_lines.append(int(line))

        if line:
            preamble.append(int(line))

    els = set(preamble)
    oldest_els = preamble.copy()
    preamble_combs = itertools.combinations(preamble, 2)

    preamble_combs_dict = dict()
    for comb_pair in preamble_combs:
        sum = comb_pair[0] + comb_pair[1]
        if sum not in preamble_combs_dict:
            preamble_combs_dict[sum] = [(comb_pair[0], comb_pair[1])]
        else:
            preamble_combs_dict[sum].append((comb_pair[0], comb_pair[1]))

    return preamble_combs_dict, els, oldest_els, read_lines


def run_task(stdin=None):
    preamble_combinations, els, oldest_els, read_lines = initial_read_preamble(stdin)
    num, read_lines = validate_next_entries(preamble_combinations, els, oldest_els, read_lines)
    print(num)

    return num, read_lines


if __name__ == '__main__':
    run_task()
