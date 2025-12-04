import time

file = "inputs/day4input.txt"

totalRolls = 0

def printArr(arr):
    temp = " "
    for i in range (0, len(arr)):
        temp += str(i)
    print(temp)
    for row in range(0, len(arr)):
        temp = ""
        temp += str(row)
        for col in range(0, len(arr[row])):
            temp += arr[row][col]
        print(temp)

def checkCanBeAccessed(arr, row, col):
    # print(row, col, ":")
    counter = 0
    for rowOffset in range(-1, 2, 1):
        for colOffset in range(-1, 2, 1):
            # print(rowOffset, colOffset)
            currRow = row + rowOffset
            currCol = col + colOffset
            if(not(currRow == row and currCol == col)): # ensure we're not on the original coord
                if(not((currRow < 0 or currRow > len(arr) - 1) or (currCol < 0 or currCol > len(arr[currRow]) - 1))): # check bounds
                    # print(currRow, currCol)
                    if(arr[currRow][currCol] == "@"):
                        # print(currRow, currCol)
                        counter += 1
                    if(counter >= 4):
                        return False
    return True

with open(file) as f:
    arr = []
    newArr = []

    # fill array
    for line in f:
        line = line.replace("\n", "") # clean line
        innerArr = list(line)
        arr.append(innerArr)
        newArr.append(innerArr.copy())

    # print("Original:")
    # printArr(arr)

    startTime = time.time()

    newTotalRolls = 1
    while(newTotalRolls > 0):
        newTotalRolls = 0
        for row in range(0, len(arr)):
            for col in range(0, len(arr[row])):
                if(arr[row][col] == "@"):
                    if(checkCanBeAccessed(arr, row, col)):
                        newTotalRolls += 1
                        totalRolls += 1
                        newArr[row][col] = "x"
        arr = newArr.copy()

    endTime = time.time()
    print("Total time:", round((endTime - startTime) * 1000), "ms")

    print("Answer:", totalRolls)

    # print("New:")
    # printArr(newArr)