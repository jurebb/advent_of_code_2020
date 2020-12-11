import re
import sys


def check_pwd(first_index, second_index, chr, pwd):
    return (pwd[first_index-1] == chr) != (pwd[second_index-1] == chr)


def main():
    correct_pwds = 0

    for line in sys.stdin:
        fi, si, chr, _, pwd = re.split(r"[-:\s]", line.strip())

        if check_pwd(int(fi), int(si), chr, pwd):
            correct_pwds += 1

    print(correct_pwds)


if __name__ == '__main__':
    main()
