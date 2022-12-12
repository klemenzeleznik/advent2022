from helpers.helpers import Helpers


class TreeNode(object):
    def __init__(self, name, content, parent, size):
        self.name = name
        self.content = content
        self.size = size
        self.parent = parent


class Day7(object):
    commands = open('../day7/assets/commands.txt')
    minDeletionSize = None

    @staticmethod
    def runDay7Challenge():
        Helpers.write_console('Creating directory structure...')
        rootTreeNode = None
        treeNode = None

        for command in Day7.commands.read().splitlines():
            if '$ cd' in command:
                splitCommand = command.split()
                match splitCommand[2]:
                    case '/':
                        rootTreeNode = TreeNode(splitCommand[2], [], None, 0)
                        treeNode = rootTreeNode
                    case '..':
                        treeNode = treeNode.parent
                    case _:
                        treeNode = [node for node in treeNode.content if node.name == splitCommand[2]][0]
            elif 'dir' in command:
                splitCommand = command.split()
                newTreeNode = TreeNode(splitCommand[1], [], treeNode, 0)
                treeNode.content.append(newTreeNode)
            elif '$ ls' in command:
                continue
            else:
                splitCommand = command.split()
                newTreeNode = TreeNode(splitCommand[1], None, treeNode, int(splitCommand[0]))
                treeNode.content.append(newTreeNode)
        Helpers.write_console('Setting node sizes...')
        Day7.setNodeSizes(rootTreeNode, rootTreeNode.size)
        Helpers.write_console('Summing sizes of folders less than 100000...')
        Helpers.write_console('Sum of is {0}'.format(Day7.findSizesLessThan(rootTreeNode, 0)[1]))
        Helpers.write_console('Finding folder to match threshold....')
        Day7.findFolderToDelete(rootTreeNode)
        Helpers.write_console('Minimum deletion folder size is {0}'.format(Day7.minDeletionSize))

    @staticmethod
    def setNodeSizes(node, size):
        if node.content is not None:
            size_sum = sum([Day7.setNodeSizes(child, size)[1] for child in node.content])
            node.size += size_sum
        return node, node.size

    @staticmethod
    def findSizesLessThan(node, size):
        if node.content is not None:
            if node.size <= 100000:
                size += node.size
            for childNode in node.content:
                size = Day7.findSizesLessThan(childNode, size)[1]
        return node, size

    @staticmethod
    def findFolderToDelete(rootNode):
        threshold = 30000000 - (70000000 - rootNode.size)
        Day7.checkIfNodeIsOverThreshold(rootNode, threshold)

    @staticmethod
    def checkIfNodeIsOverThreshold(node, threshold):
        if not Day7.minDeletionSize:
            Day7.minDeletionSize = node.size
        if threshold < node.size < Day7.minDeletionSize:
            Day7.minDeletionSize = node.size
        if node.content is not None:
            for child in node.content:
                Day7.checkIfNodeIsOverThreshold(child, threshold)

    @staticmethod
    def printNode(node):
        Helpers.write_console('name {0}, size: {1}, length: {2}'.format(node.name, node.size, len(node.content)))
