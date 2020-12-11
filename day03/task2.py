import sys

from functools import reduce


TREE_CHR = '#'


def increment_right_step(right_step, pattern_len, RIGHT_INCR):
    return (right_step + RIGHT_INCR) % pattern_len


def check_tree(pattern, right_step):
    print(pattern[right_step], right_step)
    print(' ' * (right_step), end='')
    print('^', end='')
    print(' ' * (len(pattern) - right_step))
    return pattern[right_step] == TREE_CHR


def main():
    lines = list()
    for line in sys.stdin:
        lines.append(line)

    results = list()

    for RIGHT_INCR, DOWN_INCR in zip([1, 3, 5, 7, 1], [1, 1, 1, 1, 2]):
        obstacles_count = 0
        down_step = 0
        right_step = 0

        skip_step = 0
        for line in lines:
            skip_step += 1
            line = line.strip()
            line_len = len(line)
            print(line, 'skipping')

            if skip_step < DOWN_INCR:
                continue
            else:
                break

        right_step = increment_right_step(right_step, line_len, RIGHT_INCR)

        first_iter = True
        for line in lines[DOWN_INCR:]:
            line = line.strip()
            line_len = len(line)

            down_step += 1
            if (down_step < DOWN_INCR) and not first_iter:
                continue

            print(line, end='   ')
            if check_tree(line, right_step):
                obstacles_count += 1

            down_step = 0
            right_step = increment_right_step(right_step, line_len, RIGHT_INCR)
            first_iter = False

        print(obstacles_count)
        results.append(obstacles_count)

    print(results)
    print(reduce((lambda x, y: x * y), results))


if __name__ == '__main__':
    main()
