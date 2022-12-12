from helpers.helpers import Helpers
from enum import Enum


class OpponentMoves(Enum):
    A = 'ROCK'
    B = 'PAPER'
    C = 'SCISSORS'


class MyMoves(Enum):
    X = 'ROCK'
    Y = 'PAPER'
    Z = 'SCISSORS'


class Result(Enum):
    X = 'LOOSE'
    Y = 'DRAW'
    Z = 'WIN'


class Day2:
    wins = 0
    winsUltimate = 0

    loses = 0
    losesUltimate = 0

    draws = 0
    drawsUltimate = 0

    pickPoints = 0
    pickPointsUltimate = 0

    matchPoints = 0
    matchPointsUltimate = 0

    totalPoints = 0
    totalPointsUltimate = 0

    strategyFile = open('../day2/assets/strategy.txt')

    @staticmethod
    def runDay2Challenge():
        for index, line in enumerate(Day2.strategyFile.readlines()):
            Day2.calculatePickPoints(line)
            Day2.calculatePickPointsUltimate(line)
            Day2.checkMatchOutcome(line)
            Day2.checkMatchOutcomeUltimate(line)

        Helpers.write_console('Calculating pick and match points for task 1...')
        Day2.calculateMatchPoints()
        Helpers.write_console('Match points: {0}'.format(Day2.matchPoints))
        Helpers.write_console('Pick points: {0}'.format(Day2.pickPoints))
        Helpers.write_console('Total points: {0}'.format(Day2.matchPoints + Day2.pickPoints))
        Helpers.write_console('Calculating pick and match points for task 2...')
        Day2.calculateMatchPointsUltimate()
        Helpers.write_console('Match points ultimate: {0}'.format(Day2.matchPointsUltimate))
        Helpers.write_console('Pick points ultimate: {0}'.format(Day2.pickPointsUltimate))
        Helpers.write_console('Total points ultimate: {0}'.format(Day2.matchPointsUltimate + Day2.pickPointsUltimate))

    @staticmethod
    def checkMatchOutcome(line):
        if OpponentMoves[line[0]].value == MyMoves[line[2]].value:
            Day2.draws += 1
        elif (OpponentMoves[line[0]].value == 'ROCK' and MyMoves[line[2]].value == 'PAPER') or\
                (OpponentMoves[line[0]].value == 'SCISSORS' and MyMoves[line[2]].value == 'ROCK') or\
                (OpponentMoves[line[0]].value == 'PAPER' and MyMoves[line[2]].value == 'SCISSORS'):
            Day2.wins += 1
        else:
            Day2.loses += 1

    @staticmethod
    def checkMatchOutcomeUltimate(lineUltimate):
        match Result[lineUltimate[2]].value:
            case 'WIN':
                Day2.winsUltimate += 1
            case 'DRAW':
                Day2.drawsUltimate += 1
            case 'LOOSE':
                Day2.losesUltimate += 1

    @staticmethod
    def calculatePickPoints(line):
        if MyMoves[line[2]].value == 'ROCK':
            Day2.pickPoints += 1
        elif MyMoves[line[2]].value == 'PAPER':
            Day2.pickPoints += 2
        else:
            Day2.pickPoints += 3

    @staticmethod
    def calculatePickPointsUltimate(lineUltimate):
        match Result[lineUltimate[2]].value:
            case 'WIN':
                if OpponentMoves[lineUltimate[0]].value == 'ROCK':
                    Day2.pickPointsUltimate += 2
                if OpponentMoves[lineUltimate[0]].value == 'PAPER':
                    Day2.pickPointsUltimate += 3
                if OpponentMoves[lineUltimate[0]].value == 'SCISSORS':
                    Day2.pickPointsUltimate += 1
            case 'DRAW':
                if OpponentMoves[lineUltimate[0]].value == 'ROCK':
                    Day2.pickPointsUltimate += 1
                if OpponentMoves[lineUltimate[0]].value == 'PAPER':
                    Day2.pickPointsUltimate += 2
                if OpponentMoves[lineUltimate[0]].value == 'SCISSORS':
                    Day2.pickPointsUltimate += 3
            case 'LOOSE':
                if OpponentMoves[lineUltimate[0]].value == 'ROCK':
                    Day2.pickPointsUltimate += 3
                if OpponentMoves[lineUltimate[0]].value == 'PAPER':
                    Day2.pickPointsUltimate += 1
                if OpponentMoves[lineUltimate[0]].value == 'SCISSORS':
                    Day2.pickPointsUltimate += 2

    @staticmethod
    def calculateMatchPoints():
        Day2.matchPoints = Day2.wins * 6 + Day2.draws * 3

    @staticmethod
    def calculateMatchPointsUltimate():
        Day2.matchPointsUltimate = Day2.winsUltimate * 6 + Day2.drawsUltimate * 3
