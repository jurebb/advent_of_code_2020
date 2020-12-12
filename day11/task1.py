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
    return sum([1 if layout_status[i + indcs[0], j + indcs[1]] == OCC_CHAR else 0 for indcs in ADJACENCY_INDICES])


def check_no_adj_occ(layout_status, i, j):
    return all([layout_status[i + indcs[0], j + indcs[1]] != OCC_CHAR for indcs in ADJACENCY_INDICES])


def apply_rules(layout_status, i, j):
    if layout_status[i, j] == UNOCC_CHAR and check_no_adj_occ(layout_status, i, j):
        return OCC_CHAR

    if layout_status[i, j] == OCC_CHAR and count_adj_occ(layout_status, i, j) >= 4:
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
