from helpers.helpers import Helpers


class Day6(object):

    @staticmethod
    def runDay6Challenge():
        Day6.findMarker()
        Day6.findMessage()

    @staticmethod
    def findMarker():
        Helpers.write_console('Buffering in search of start-of-packet marker...')
        stream = open('../day6/assets/datastream.txt').readline()
        counter = 0
        char4buffer = []
        for char in stream:
            counter += 1
            if len(char4buffer) >= 4:
                del char4buffer[0]
                char4buffer.append(char)
            else:
                char4buffer.append(char)
            if len(char4buffer) == 4 and len(char4buffer) == len(set(char4buffer)):
                break
        Helpers.write_console('Marker found after {0} processed characters!'.format(counter))

    @staticmethod
    def findMessage():
        Helpers.write_console('Buffering in search of message...')
        stream = open('../day6/assets/datastream.txt').readline()
        counter = 0
        char4buffer = []
        for char in stream:
            counter += 1
            if len(char4buffer) >= 14:
                del char4buffer[0]
                char4buffer.append(char)
            else:
                char4buffer.append(char)
            if len(char4buffer) == 14 and len(char4buffer) == len(set(char4buffer)):
                break
        Helpers.write_console('Message found after {0} processed characters!'.format(counter))