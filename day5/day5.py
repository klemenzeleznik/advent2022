import re

from helpers.helpers import Helpers


class Day5(object):
    stackOfCrates9000 = [['R', 'P', 'C', 'D', 'B', 'G'], ['H', 'V', 'G'], ['N', 'S', 'Q', 'D', 'J', 'P', 'M'],
                         ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'], ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'],
                         ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'], ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'],
                         ['C', 'M', 'D', 'B', 'F'], ['F', 'C', 'Q', 'G']]
    stackOfCrates9001 = [['R', 'P', 'C', 'D', 'B', 'G'], ['H', 'V', 'G'], ['N', 'S', 'Q', 'D', 'J', 'P', 'M'],
                         ['P', 'S', 'L', 'G', 'D', 'C', 'N', 'M'], ['J', 'B', 'N', 'C', 'P', 'F', 'L', 'S'],
                         ['Q', 'B', 'D', 'Z', 'V', 'G', 'T', 'S'], ['B', 'Z', 'M', 'H', 'F', 'T', 'Q'],
                         ['C', 'M', 'D', 'B', 'F'], ['F', 'C', 'Q', 'G']]

    @staticmethod
    def runDay5Challenge():
        Day5.useCrateMover9000()
        Day5.useCrateMover9001()

    @staticmethod
    def useCrateMover9000():
        Helpers.write_console('Moving crates with CrateMover 9000...')
        movesFile = open('../day5/assets/moves.txt')
        for line in movesFile.readlines():
            numbers = re.findall(r'\d+', line)
            for i in range(int(numbers[0])):
                movedCrate = Day5.stackOfCrates9000[int(numbers[1]) - 1].pop()
                Day5.stackOfCrates9000[int(numbers[2]) - 1].append(movedCrate)

        Helpers.write_console('Final crates position:')
        for stack in Day5.stackOfCrates9000:
            Helpers.write_console(stack)

    @staticmethod
    def useCrateMover9001():
        Helpers.write_console('Moving crates with CrateMover 9001...')
        movesFile = open('../day5/assets/moves.txt')
        for line in movesFile.readlines():
            movedCrates = []
            numbers = re.findall(r'\d+', line)
            for i in range(int(numbers[0])):
                movedCrate = Day5.stackOfCrates9001[int(numbers[1]) - 1].pop()
                movedCrates.insert(0, movedCrate)
            Day5.stackOfCrates9001[int(numbers[2]) - 1].extend(movedCrates)

        Helpers.write_console('Final crates position:')
        for stack in Day5.stackOfCrates9001:
            Helpers.write_console(stack)
