import sys


def main():
    calcs = dict()

    for line in sys.stdin:
        num = int(line.strip())
        key = 2020 - num

        if num not in calcs:
            calcs[key] = num

        else:
            print(num, key)
            print(num * key)


if __name__ == '__main__':
    main()
