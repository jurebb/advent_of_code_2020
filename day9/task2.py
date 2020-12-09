import math
import sys

from task1 import run_task


def find_contiguous_set(list_of_nums, target_sum):
    for i in range(0, len(list_of_nums)):
        for j in range(len(list_of_nums) - 1, 0, -1):
            if j - i > 1:
                current_subset = list_of_nums[i:j]
                if sum(current_subset) == target_sum:
                    return min(current_subset), max(current_subset)


def main():
    num, read_lines = run_task(sys.stdin)
    min_el, max_el = find_contiguous_set(read_lines, int(num))
    print(min_el + max_el)


if __name__ == '__main__':
    main()
