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
        self.heading = Heading.east

    def move_heading(self, heading, value):
        if heading == Heading.north:
            self.pos_y += value
        elif heading == Heading.east:
            self.pos_x += value
        elif heading == Heading.south:
            self.pos_y -= value
        else:
            self.pos_x -= value

    def move_forward(self, value):
        self.move_heading(self.heading, value)

    def rotate(self, degrees):
        new_heading = (self.heading.value + degrees) % 360
        self.heading = Heading(new_heading)

    def manhattan_distance(self):
        return abs(self.pos_x) + abs(self.pos_y)


def parse_and_perform_instruction(raw_instr, ship):
    instr, val = raw_instr[0], int(raw_instr[1:])

    if instr == 'N':
        ship.move_heading(Heading.north, val)
    elif instr == 'S':
        ship.move_heading(Heading.south, val)
    elif instr == 'E':
        ship.move_heading(Heading.east, val)
    elif instr == 'W':
        ship.move_heading(Heading.west, val)
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
