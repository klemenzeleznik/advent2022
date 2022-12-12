from helpers.helpers import Helpers


class Day8(object):
    visibleTrees = 0
    treesMatrix = []
    trees = open('../day8/assets/trees.txt')

    @staticmethod
    def runDay8Challenge():
        Helpers.write_console('Creating trees matrix...')
        Day8.createTreesMatrix()
        Helpers.write_console('Calculation number of visible trees...')
        Day8.checkVisibleTrees()
        Helpers.write_console('Number of visible trees: {0}'.format(Day8.visibleTrees))
        Helpers.write_console('Checking for best scenic score...')
        Day8.checkScenicScore()

    @staticmethod
    def createTreesMatrix():
        for index, trees in enumerate(Day8.trees.read().splitlines()):
            Day8.treesMatrix.append([])
            for tree in trees:
                Day8.treesMatrix[index].append(tree)

    @staticmethod
    def checkVisibleTrees():
        for indexY, treeLine in enumerate(Day8.treesMatrix):
            for indexX, tree in enumerate(Day8.treesMatrix[indexY]):
                if indexY == 0 or indexX == 0 or indexX == len(treeLine) - 1 or indexY == len(treeLine) - 1:
                    Day8.visibleTrees += 1
                elif Day8.checkVisibleFromTop(tree, indexY, indexX):
                    Day8.visibleTrees += 1
                elif Day8.checkVisibleFromBottom(tree, indexY, indexX):
                    Day8.visibleTrees += 1
                elif Day8.checkVisibleFromLeft(tree, indexY, indexX):
                    Day8.visibleTrees += 1
                elif Day8.checkVisibleFromRight(tree, indexY, indexX):
                    Day8.visibleTrees += 1

    @staticmethod
    def checkScenicScore():
        bestScenicScore = 0;
        for indexY, treeLine in enumerate(Day8.treesMatrix):
            for indexX, tree in enumerate(Day8.treesMatrix[indexY]):
                scenicScore = Day8.sumScenicScores(tree, indexY, indexX)
                if scenicScore > bestScenicScore:
                    bestScenicScore = scenicScore
        Helpers.write_console('Best scenic score is {0}'.format(bestScenicScore))

    @staticmethod
    def sumScenicScores(tree, indexY, indexX):
        return Day8.countVisibilityTop(tree, indexY, indexX) * \
               Day8.countVisibilityBottom(tree, indexY, indexX) * \
               Day8.countVisibilityLeft(tree, indexY, indexX) * \
               Day8.countVisibilityRight(tree, indexY, indexX)

    @staticmethod
    def checkVisibleFromTop(tree, indexY, indexX):
        treeYPosition = indexY - 1
        isTreeVisible = False
        while treeYPosition != -1:
            if Day8.treesMatrix[treeYPosition][indexX] < tree:
                isTreeVisible = True
            else:
                isTreeVisible = False
                break
            treeYPosition -= 1
        return isTreeVisible

    @staticmethod
    def checkVisibleFromBottom(tree, indexY, indexX):
        treeYPosition = indexY + 1
        isTreeVisible = True
        counter = 1
        while treeYPosition != 99:
            if Day8.treesMatrix[treeYPosition][indexX] >= tree:
                isTreeVisible = False
                break
            counter += 1
            treeYPosition += 1
        return isTreeVisible

    @staticmethod
    def checkVisibleFromLeft(tree, indexY, indexX):
        treexPosition = indexX - 1
        isTreeVisible = False
        counter = 1
        while treexPosition != -1:
            if Day8.treesMatrix[indexY][treexPosition] < tree:
                counter += 1
                isTreeVisible = True
            else:
                isTreeVisible = False
                break
            treexPosition -= 1
        return isTreeVisible

    @staticmethod
    def checkVisibleFromRight(tree, indexY, indexX):
        treexPosition = indexX + 1
        isTreeVisible = True
        while treexPosition != 99:
            if Day8.treesMatrix[indexY][treexPosition] >= tree:
                isTreeVisible = False
                break
            treexPosition += 1
        return isTreeVisible

    @staticmethod
    def countVisibilityTop(tree, indexY, indexX):
        treeYPosition = indexY - 1
        counter = 0
        while treeYPosition != -1:
            if Day8.treesMatrix[treeYPosition][indexX] < tree:
                counter += 1
            else:
                counter += 1
                break
            treeYPosition -= 1
        return counter

    @staticmethod
    def countVisibilityBottom(tree, indexY, indexX):
        treeYPosition = indexY + 1
        counter = 0
        while treeYPosition != 99:
            if Day8.treesMatrix[treeYPosition][indexX] >= tree:
                counter += 1
                break
            counter += 1
            treeYPosition += 1
        return counter

    @staticmethod
    def countVisibilityLeft(tree, indexY, indexX):
        treexPosition = indexX - 1
        counter = 0
        while treexPosition != -1:
            if Day8.treesMatrix[indexY][treexPosition] < tree:
                counter += 1
            else:
                counter += 1
                break
            treexPosition -= 1
        return counter

    @staticmethod
    def countVisibilityRight(tree, indexY, indexX):
        treexPosition = indexX + 1
        counter = 0
        while treexPosition != 99:
            if Day8.treesMatrix[indexY][treexPosition] >= tree:
                counter += 1
                break
            counter += 1
            treexPosition += 1
        return counter
