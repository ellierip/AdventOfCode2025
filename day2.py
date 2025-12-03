import time

file = "inputs/day2input.txt"

currInput = ""
invalidTotal = 0

def isInvalidPt1(id):
    idLength = len(id)
    if(idLength % 2 == 1): # if odd it can't have two repeating sequences
        return False
    
    midpoint = int(idLength / 2)
    half1 = id[:midpoint]
    half2 = id[midpoint:]

    return(half1 == half2)

def isInvalid(id):
    id = str(id)
    idLength = len(id)

    if idLength % 2 == 0:
        endRange = int(idLength / 2)
    else:
        endRange = int((idLength - 1) / 2)

    for i in range(endRange, 0, -1):
        # skip if it can't be split evenly
        if(idLength % i != 0):
            continue
        
        splitId = []
        for j in range(0, idLength, i):
            splitId.append(id[j:j + i])

        # check each element of the split
        invalid = True
        for el in splitId:
            if el != splitId[0]:
                invalid = False
                break
        
        if invalid == True:
            return True
    return False
        
with open(file) as f:
    for line in f:
        startTime = time.time()

        currInput = line
        while("," in currInput):
            id1 = int(currInput[:currInput.find("-")])
            id2 = int(currInput[currInput.find("-") + 1:currInput.find(",")])

            for i in range(id1, id2 + 1):
                if(isInvalid(str(i))):
                    invalidTotal += i

            currInput = currInput[currInput.find(",") + 1:] # cut off input
        id1 = int(currInput[:currInput.find("-")])
        id2 = int(currInput[currInput.find("-") + 1:])
        for i in range(id1, id2 + 1):
            if(isInvalid(str(i))):
                invalidTotal += i
        
        endTime = time.time()
        print("Total time:", round((endTime - startTime) * 1000), "ms")

    print("Answer:", invalidTotal)