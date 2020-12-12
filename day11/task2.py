import numpy as np
import sys


SKIP_CHAR = 'O'
UNOCC_CHAR = 'L'
OCC_CHAR = '#'
FLOOR_CHAR = '.'
ADJACENCY_INDICES = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

def count_occupied(layout_status):
    return (layout_status == OCC_CHAR).sum()


def count_adj_occ(layout_status, i, j):
    count = 0

    for indcs in ADJACENCY_INDICES:
        for multiplier in range(1, sys.maxsize):
            curr_ind = layout_status[i + indcs[0] * multiplier, j + indcs[1] * multiplier]

            if curr_ind in {SKIP_CHAR, UNOCC_CHAR}:
                break
            elif curr_ind == OCC_CHAR:
                count += 1
                break

    return count


def check_no_adj_occ(layout_status, i, j):
    for indcs in ADJACENCY_INDICES:
        for multiplier in range(1, sys.maxsize):
            curr_ind = layout_status[i + indcs[0] * multiplier, j + indcs[1] * multiplier]

            if curr_ind == SKIP_CHAR:
                break
            elif curr_ind == OCC_CHAR:
                return False
            elif curr_ind == UNOCC_CHAR:
                break

    return True


def apply_rules(layout_status, i, j):
    if layout_status[i, j] == UNOCC_CHAR and check_no_adj_occ(layout_status, i, j):
        return OCC_CHAR

    if layout_status[i, j] == OCC_CHAR and count_adj_occ(layout_status, i, j) >= 5:
        return UNOCC_CHAR

    return layout_status[i, j]


def simulation_round(layout_status):
    new_layout_status = layout_status.copy()

    for i in range(layout_status.shape[0]):
        for j in range(layout_status.shape[1]):
            new_layout_status[i, j] = apply_rules(layout_status, i, j)

    return new_layout_status


def simulate_seating(layout_status):
    while True:
        new_layout_status = simulation_round(layout_status)

        if (new_layout_status == layout_status).all():
            break

        layout_status = new_layout_status

    return new_layout_status


def read_seating_layout():
    layout = list()
    first_line = True

    for line in sys.stdin:
        line = line.strip()

        if first_line:
            layout.append([SKIP_CHAR for _ in range(len(line) + 2)])
            first_line = False

        layout.append([SKIP_CHAR] + list(line) + [SKIP_CHAR])

    layout.append([SKIP_CHAR for _ in range(len(line) + 2)])

    return np.array(layout)


def main():
    layout = read_seating_layout()

    layout = simulate_seating(layout)
    occ_count = count_occupied(layout)
    print(occ_count)


if __name__ == '__main__':
    main()
