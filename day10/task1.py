import sys


def find_diffs(adapters):
    one_jolt_diffs = 0
    three_jolt_diffs = 0

    for i in range(len(adapters) - 1):
        diff = adapters[i + 1] - adapters[i]

        if diff == 1:
            one_jolt_diffs += 1
        elif diff == 3:
            three_jolt_diffs += 1

    return one_jolt_diffs, three_jolt_diffs


def read_adapters_from_stdin():
    adapters = [0]

    for line in sys.stdin:
        adapter_rating = int(line.strip())

        adapters.append(adapter_rating)

    adapters = sorted(adapters)
    adapters.append(adapters[-1] + 3)

    return sorted(adapters)


def main():
    adapters = read_adapters_from_stdin()
    one_jolt_diffs, three_jolt_diffs = find_diffs(adapters)

    print(one_jolt_diffs * three_jolt_diffs)


if __name__ == '__main__':
    main()
