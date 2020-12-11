import sys


def main():
    first_pass = dict()
    inputs = list()

    for line in sys.stdin:
        num = int(line.strip())
        key = 2020 - num

        inputs.append(num)

        first_pass[key] = num

    for a in inputs:
        for b in inputs:
            if a + b in first_pass:
                print(a, b, first_pass[a+b])
                print(a * b * first_pass[a + b])


if __name__ == '__main__':
    main()
