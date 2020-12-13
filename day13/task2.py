import sys


def get_multiplier_step(times_busses, max_bus_id, max_bus_id_offset):
    factor = 1

    for time_offset, bus_id in times_busses:
        if time_offset - max_bus_id_offset == bus_id:
            factor *= (time_offset - max_bus_id_offset)

    return factor


def calculate_earliest_consecutive_timestamp_o2(times_busses):
    assert times_busses[0][0] == 0, 'error in parsed data'
    max_bus_id = max([time_bus[1] for time_bus in times_busses])
    max_bus_id_offset = [time_bus[0] for time_bus in times_busses if time_bus[1] == max_bus_id][0]
    times_busses = [time_bus for time_bus in times_busses if time_bus[1] != max_bus_id]
    times_busses = sorted(times_busses, key=(lambda x: x[1]), reverse=True)
    len_times_busses = len(times_busses)

    print('max_bus_id', max_bus_id)
    print('max_bus_id_offset', max_bus_id_offset)
    print('times_busses', times_busses)
    print('len_times_busses', len_times_busses)

    multiplier_step = get_multiplier_step(times_busses, max_bus_id, max_bus_id_offset)
    print('multiplier_step', multiplier_step)

    for multiplier in range(0, sys.maxsize, multiplier_step):
        current_earliest_timestamp = multiplier * max_bus_id - max_bus_id_offset
        found_sequence = False
        cnt = 0

        for i in range(len_times_busses):
            cnt += 1
            time_offset, bus_id = times_busses[i]

            if (current_earliest_timestamp + time_offset) % bus_id != 0:
                break

            if i == len_times_busses - 1:
                found_sequence = True

        if found_sequence:
            return multiplier * max_bus_id - max_bus_id_offset


def parse_stdin():
    _ = sys.stdin.readline()
    times_busses = list(
        map(lambda x: (x[0], int(x[1])),
            filter(lambda x: x[1] != 'x',
                   enumerate(sys.stdin.readline().strip().split(','))
                   )
            )
    )

    return times_busses


def main():
    times_busses = parse_stdin()

    earliest_timestamp = calculate_earliest_consecutive_timestamp_o2(times_busses)
    print(earliest_timestamp)


if __name__ == '__main__':
    main()
