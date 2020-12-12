from enum import Enum
import sys


class Heading(Enum):
    north = 0
    east = 90
    south = 180
    west = 270


class ShipStatus:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.wp_x = 10
        self.wp_y = 1

    def move_wp(self, heading, value):
        if heading == Heading.north:
            self.wp_y += value
        elif heading == Heading.east:
            self.wp_x += value
        elif heading == Heading.south:
            self.wp_y -= value
        else:
            self.wp_x -= value

    def move_forward(self, value):
        self.pos_x += value * self.wp_x
        self.pos_y += value * self.wp_y

    def rotate(self, degrees):
        degrees = degrees % 360
        assert degrees % 90 == 0

        number_of_rotations = int(abs(degrees) / 90)

        if degrees > 0:
            for _ in range(number_of_rotations):
                self.wp_x, self.wp_y = self.wp_y, -self.wp_x
        else:
            for _ in range(number_of_rotations):
                self.wp_x, self.wp_y = -self.wp_y, self.wp_x

    def manhattan_distance(self):
        return abs(self.pos_x) + abs(self.pos_y)


def parse_and_perform_instruction(raw_instr, ship):
    instr, val = raw_instr[0], int(raw_instr[1:])

    if instr == 'N':
        ship.move_wp(Heading.north, val)
    elif instr == 'S':
        ship.move_wp(Heading.south, val)
    elif instr == 'E':
        ship.move_wp(Heading.east, val)
    elif instr == 'W':
        ship.move_wp(Heading.west, val)
    elif instr == 'L':
        ship.rotate(-val)
    elif instr == 'R':
        ship.rotate(val)
    elif instr == 'F':
        ship.move_forward(val)
    else:
        raise Exception('invalid instruction')


def simulate_stdin_instructions():
    ship = ShipStatus()

    for line in sys.stdin:
        parse_and_perform_instruction(line.strip(), ship)

    return ship


def main():
    ship = simulate_stdin_instructions()
    print(ship.manhattan_distance())


if __name__ == '__main__':
    main()
