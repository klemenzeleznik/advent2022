from day1.task1 import Day1
from day2.day2 import Day2
from day3.day3 import Day3
from day4.day4 import Day4
from day5.day5 import Day5
from day6.day6 import Day6
from day7.day7 import Day7
from day8.day8 import Day8
from helpers.helpers import Helpers

dayNumber = 0

Helpers.write_console('Hello to advent of Code 2022')
Helpers.write_console('-------------------------------------------------------------')
Helpers.write_console('What day challenge do you want to run?')

dayNumber = input("Enter day:")

match dayNumber:
    case '1':
        Day1.runDay1Challenge()
    case '2':
        Day2.runDay2Challenge()
    case '3':
        Day3.runDay3Challenge()
    case '4':
        Day4.runDay4Challenge()
    case '5':
        Day5.runDay5Challenge()
    case '6':
        Day6.runDay6Challenge()
    case '7':
        Day7.runDay7Challenge()
    case '8':
        Day8.runDay8Challenge()
