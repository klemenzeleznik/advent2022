from helpers.helpers import Helpers
import numpy as np


class Day4(object):
    numberOfCoveredSections = 0
    numberOfOverlaps = 0
    pair1 = []
    pair2 = []

    @staticmethod
    def runDay4Challenge():
        Helpers.write_console('Checking covered ranges...')
        sectionsFile = open('../day4/assets/sections.txt')
        for line in sectionsFile.read().splitlines():
            splitPairs = line.split(',')
            Day4.pair1 = []
            Day4.pair2 = []
            Day4.calculateCoveredSectionsTotal(splitPairs)
            Day4.pair1 = []
            Day4.pair2 = []
            Day4.calculateOverlapsTotal(splitPairs)
        Helpers.write_console('Number of covered sections: {0}'.format(Day4.numberOfCoveredSections))
        Helpers.write_console('Checking total overlaps...')
        Helpers.write_console('Number of covered sections: {0}'.format(Day4.numberOfOverlaps))

    @staticmethod
    def calculateCoveredSectionsTotal(splitPairs):
        Day4.pair1.extend(range(int(splitPairs[0].split('-')[0]), int(splitPairs[0].split('-')[1]) + 1))
        Day4.pair2.extend(range(int(splitPairs[1].split('-')[0]), int(splitPairs[1].split('-')[1]) + 1))
        if np.isin(Day4.pair2, Day4.pair1).all() or np.isin(Day4.pair1, Day4.pair2).all():
            Day4.numberOfCoveredSections += 1

    @staticmethod
    def calculateOverlapsTotal(splitPairs):
        Day4.pair1.extend(range(int(splitPairs[0].split('-')[0]), int(splitPairs[0].split('-')[1]) + 1))
        Day4.pair2.extend(range(int(splitPairs[1].split('-')[0]), int(splitPairs[1].split('-')[1]) + 1))
        if np.in1d(Day4.pair1, Day4.pair2).any():
            Day4.numberOfOverlaps += 1
