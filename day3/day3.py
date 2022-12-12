from helpers.helpers import Helpers


class Day3(object):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'X', 'Y', 'Z']
    priorityTotal = 0

    @staticmethod
    def runDay3Challenge():
        Helpers.write_console('Searching rucksacks for duplicate items...')
        Day3.findSharedItems()
        Helpers.write_console('Priority total for common items: {0}'.format(Day3.priorityTotal))
        Helpers.write_console('Searching rucksacks for badges...')
        Day3.findBadges()
        Helpers.write_console('Priority total for badges: {0}'.format(Day3.priorityTotal))

    @staticmethod
    def findBadges():
        Day3.priorityTotal = 0
        rucksacksFile = open('../day3/assets/rucksacks.txt')
        lines = rucksacksFile.readlines()
        for x in range(100):
            elf1 = lines[0]
            elf2 = lines[1]
            elf3 = lines[2]
            lines.remove(lines[0])
            lines.remove(lines[0])
            lines.remove(lines[0])
            sameItems = list(set(elf1) & set(elf2) & set(elf3))
            if '\n' in sameItems:
                sameItems.remove('\n')
            Day3.addToPriorityTotal(sameItems[0])

    @staticmethod
    def findSharedItems():
        rucksacksFile = open('../day3/assets/rucksacks.txt')
        for index, line in enumerate(rucksacksFile.readlines()):
            compartment1 = line[0:len(line)//2]
            compartment2 = line[len(line)//2:len(line)]
            Day3.compareCompartments(compartment1, compartment2)

    @staticmethod
    def addToPriorityTotal(item):
        Day3.priorityTotal += Day3.alphabet.index(item) + 1

    @staticmethod
    def compareCompartments(compartment1, compartment2):
        foundItem = False
        for x in compartment1:
            for y in compartment2:
                if x == y and not foundItem:
                    Day3.addToPriorityTotal(x)
                    foundItem = True
