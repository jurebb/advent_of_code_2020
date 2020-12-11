import math
import sys


TOTAL_ROWS = 128
TOTAL_COLS = 8
ROW_SIGNS = 7
COL_SIGNS = 3
ROW_WEIGHT = 8
COL_WEIGHT = 1


class Partition:
    def __init__(self):
        self.lower = 0
        self.upper = None
        self.lower_sign = None
        self.upper_sign = None

    def __str__(self):
        return '[{}, {}]'.format(self.lower, self.upper)

    def partition(self, sign):
        if sign == self.lower_sign:
            self.upper -= math.ceil((self.upper - self.lower) / 2)
        elif sign == self.upper_sign:
            self.lower += math.ceil((self.upper - self.lower) / 2)

    def get_position(self):
        if self.lower == self.upper:
            return self.lower
        else:
            print('not fully partitioned! {}'.format(self))


class PartitionRows(Partition):
    def __init__(self):
        super().__init__()
        self.upper = TOTAL_ROWS - 1
        self.lower_sign = 'F'
        self.upper_sign = 'B'


class PartitionCols(Partition):
    def __init__(self):
        super().__init__()
        self.upper = TOTAL_COLS - 1
        self.lower_sign = 'L'
        self.upper_sign = 'R'


def print_candidate_seats(max_seat_id, seat_ids):
    for candidate_seat_id in range(max_seat_id):
        if candidate_seat_id not in seat_ids:
            if (candidate_seat_id - 1) in seat_ids and (candidate_seat_id + 1) in seat_ids:
                print(candidate_seat_id)


def get_seat_id(row_part, col_part):
    return row_part.get_position() * ROW_WEIGHT + col_part.get_position() * COL_WEIGHT


def partition_board_pass(board_pass):
    rp = PartitionRows()

    for sign in board_pass[:ROW_SIGNS]:
        rp.partition(sign)

    cp = PartitionCols()

    for sign in board_pass[-COL_SIGNS:]:
        cp.partition(sign)

    return cp, rp


def main():
    seat_ids = list()

    for line in sys.stdin:
        board_pass = line.strip()

        cp, rp = partition_board_pass(board_pass)

        sid = get_seat_id(rp, cp)
        seat_ids.append(sid)

    max_seat_id = max(seat_ids)
    seat_ids = set(seat_ids)

    print_candidate_seats(max_seat_id, seat_ids)


if __name__ == '__main__':
    main()
