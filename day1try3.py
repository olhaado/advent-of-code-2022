import os
import sys

file = open(os.path.join(sys.path[0], 'input1.txt'),'r')

def part1(file):

    cals = 0
    maxCals = 0

    for i in file:
        if i not in['\n', '\r', '\r\n']:
            cals += int(i)
            if cals > maxCals:
                maxCals = cals
        else:
            cals = 0
    return maxCals

def checkType(file):
    for i in file:
        print(type(i))

answer = part1(file)
print(answer)