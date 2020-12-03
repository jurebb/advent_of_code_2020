import sys


RIGHT_INCR = 3
DOWN_INCR = 1
TREE_CHR = '#'


def increment_right_step(right_step, pattern_len):
    return (right_step + RIGHT_INCR) % pattern_len


def check_tree(pattern, right_step):
    print(pattern[right_step])
    return pattern[right_step] == TREE_CHR


def main():
    obstacles_count = 0
    down_step = 0
    right_step = 0

    for line in sys.stdin:
        line = line.strip()
        line_len = len(line)

        down_step += 1
        if down_step < DOWN_INCR:
            continue

        print(line, end='   ')
        if check_tree(line, right_step):
            obstacles_count += 1

        down_step = 0
        right_step = increment_right_step(right_step, line_len)

    print(obstacles_count)


if __name__ == '__main__':
    main()
