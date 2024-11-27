import math

def significantFiguresCalculation(number, significantFigures):
    intPart = int(number)
    decPart = number - int(intPart)
    counter = 0
    truncatedNumber = 0
    flag = False
    
    numberArray = []
    while intPart > 0:
        theNumber = intPart % 10
        intPart = int(intPart / 10)
        
        counter += 1
        if counter == significantFigures:
            flag = True
        numberArray.append(theNumber)
    for i in range(min(significantFigures, len(numberArray))):
        truncatedNumber += numberArray[len(numberArray)-i-1] * 10**(len(numberArray)-i-1)
    if flag == False:
        truncatedNumber = int(truncatedNumber) + decPart 
        truncatedNumber = math.trunc(truncatedNumber * 10**(significantFigures-counter)) 
        truncatedNumber/= 10**(significantFigures-counter)
        return truncatedNumber
    else:
        return truncatedNumber
        
            
