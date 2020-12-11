import re
import sys


def check_pwd(lower_bound, upper_bound, chr, pwd):
    return lower_bound <= pwd.count(chr) <= upper_bound


def main():
    correct_pwds = 0

    for line in sys.stdin:
        lb, ub, chr, _, pwd = re.split(r"[-:\s]", line.strip())

        if check_pwd(int(lb), int(ub), chr, pwd):
            correct_pwds += 1

    print(correct_pwds)


if __name__ == '__main__':
    main()
