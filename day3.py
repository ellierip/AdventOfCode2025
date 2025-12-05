import time

file = "inputs/day3inputtest.txt"

totalJoltage = 0

def getJoltage(joltageList):
    total = 0
    listLength = len(joltageList)
    i = listLength
    mult = 1

    for i in range(listLength - 1, -1, -1):
        total += (joltageList[i] * mult)
        mult *= 10
    
    return total

# Part 1
# def getJoltage(num1, num2):
#     return ((num1 * 10) + num2)

with open(file) as f:
    startTime = time.time()

    for line in f:
        line = line.replace("\n", "") # clean line
        lineLength = len(line)

        '''
        Part 1 solution
        largest1Index = lineLength - 2
        largest1 = int(line[largest1Index])
        largest2Index = lineLength - 1
        largest2 = int(line[largest2Index])

        for i in range(lineLength - 3, -1, -1):
            currNum = int(line[i])
            # update first number
            if(currNum >= largest1):
                largest1 = currNum
                largest1Index = i
                # update second number
                if(largest2 < 9): # don't bother updating if we've already hit 9
                    for j in range(i + 1, largest2Index):
                        currNum2 = int(line[j])
                        if(currNum2 >= largest2):
                            largest2 = currNum2
                            largest2Index = j

        totalJoltage += getJoltage(largest1, largest2)
        '''
            
    endTime = time.time()
    print("Total time:", round((endTime - startTime) * 1000), "ms")

    print("Answer:", totalJoltage)