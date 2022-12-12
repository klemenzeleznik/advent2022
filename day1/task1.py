import os

from helpers.helpers import Helpers


class Day1(object):
    maxCalories = 0;
    caloriesFile = open('../day1/assets/calories.txt', 'r')
    elfBagsArray = []

    @staticmethod
    def runDay1Challenge():
        Helpers.write_console('Calculating max calories...')
        Day1.calculateAndSetMaxCalories()
        Helpers.write_console('Max calories in an elf bag is: {0} '.format(Day1.maxCalories))
        Helpers.write_console('Calculating top 3 bags...')
        Day1.getTop3BagsSize()

    @staticmethod
    def calculateAndSetMaxCalories():
        elfCalories = 0
        for index, line in enumerate(Day1.caloriesFile.readlines()):
            if line.strip() and index != len(Day1.caloriesFile.readlines()) + 1:
                elfCalories += int(line)
            else:
                if elfCalories > Day1.maxCalories:
                    Day1.maxCalories = elfCalories
                Day1.elfBagsArray.append(elfCalories)
                elfCalories = 0

    @staticmethod
    def getTop3BagsSize():
        Day1.elfBagsArray.sort(reverse=True)
        top3BagsSum = sum(Day1.elfBagsArray[:3])
        Helpers.write_console('Sum of calories in tosssp 3 bags is {0}'.format(top3BagsSum))
