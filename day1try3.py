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
    file.close()

def part2(file):
    
    cals = 0
    firstElf = 0
    secondElf = 0
    thirdElf = 0
    
    for i in file:
        if i not in['\n', '\r', '\r\n']:
            cals += int(i)
            print(int(i))
        else:
            print("no")
            if cals > firstElf:
                print("yes")
                thirdElf = secondElf
                secondElf = firstElf
                firstElf = cals
                print(f"{firstElf},{secondElf},{thirdElf}")
            cals = 0
    top3 = [firstElf, secondElf, thirdElf]
    return top3
    file.close()

#answer = part1(file)
#print(answer)

answer = part2(file)
print(sum(answer))