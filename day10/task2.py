import operator
import sys


def calculate_subtree_arrangements_o1(current_val, all_vals, cache):
    if current_val == 0:
        return 1

    candidate_vals_diffs = list()
    ind_diff = 1
    for candidate_val in all_vals[:3]:
        diff = current_val - candidate_val

        if diff in {1, 2, 3}:
            candidate_vals_diffs.append((candidate_val, ind_diff))

        ind_diff += 1

    sum_arrangs = 0
    if not current_val in cache:
        for candidate_val, ind_diff in candidate_vals_diffs:
            arrangs = calculate_subtree_arrangements_o1(candidate_val, all_vals[ind_diff:], cache)
            sum_arrangs += arrangs

    else:
        sum_arrangs = cache[current_val]

    cache[current_val] = sum_arrangs

    return sum_arrangs


def calculate_total_arrangements(sorted_adapters):
    first_val = sorted_adapters[0]

    cache = dict()
    total_arrangements = calculate_subtree_arrangements_o1(first_val, sorted_adapters, cache)

    return total_arrangements


def read_adapters_from_stdin():
    adapters = [0]
    max_rating = 0

    for line in sys.stdin:
        adapter_rating = int(line.strip())

        if adapter_rating > max_rating:
            max_rating = adapter_rating

        adapters.append(adapter_rating)

    adapters.append(max_rating + 3)
    adapters = sorted(adapters, reverse=True)

    return adapters


def main():
    adapters = read_adapters_from_stdin()
    total_arrangements = calculate_total_arrangements(adapters)

    print(total_arrangements)


if __name__ == '__main__':
    main()
