import math
import sys


def calculate_earliest_bus_ride(earliest_depart_time, busses):
    best_bus_id = -sys.maxsize
    best_bus_wait_mins = sys.maxsize

    for bus_id in busses:
        bus_ride_time = math.ceil(earliest_depart_time / bus_id) * bus_id
        wait_mins = bus_ride_time - earliest_depart_time

        if wait_mins < best_bus_wait_mins:
            best_bus_wait_mins = wait_mins
            best_bus_id = bus_id

    return best_bus_id, best_bus_wait_mins


def parse_stdin():
    earliest_depart_time = int(sys.stdin.readline().strip())
    busses = list(map(lambda x: int(x), filter(lambda x: x != 'x', sys.stdin.readline().strip().split(','))))

    return earliest_depart_time, busses


def main():
    earliest_depart_time, busses = parse_stdin()
    earliest_bus, wait_mins = calculate_earliest_bus_ride(earliest_depart_time, busses)

    print(earliest_bus * wait_mins)


if __name__ == '__main__':
    main()
