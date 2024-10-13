def factorial(num):
    if(isinstance(num, int) and (num >= 0)):
        if (num == 0):
            return 1
        else:
            return num * factorial(num - 1)
    else:
        raise ValueError("Error: Missing parameters.")

def classMark(startIntervals, endIntervals):
    return (startIntervals + endIntervals) / 2

def median(startIntervals, endIntervals=None, frecuencies=None):
    #Check if there is only 1 list.
    if((startIntervals is not None) and (endIntervals is None) and (frecuencies is None)):
        totalData = len(startIntervals)
        #Check if it's odd.
        if(totalData % 2 == 0):
            return (startIntervals[int(totalData / 2)] + (startIntervals[int((totalData) / 2)] + 1)) / 2
        else:
            return startIntervals[int((totalData + 1) / 2)]
    #Check if there are 3 lists.
    elif((startIntervals is not None) and (endIntervals is not None) and (frecuencies is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals) == len(frecuencies)):
            #Declare variables
            accumulatedFrecuency = 0
            totalData = sum(frecuencies)
            #Check if it's odd.
            if(totalData % 2 == 0):
                data = totalData / 2
                for i in range(0, len(startIntervals)):
                    accumulatedFrecuency += frecuencies[i]
                    if(accumulatedFrecuency >= data):
                        break
                data1 = classMark(startIntervals[i], endIntervals[i])
                #Re-start variable.
                accumulatedFrecuency = 0
                for i in range(0, len(startIntervals)):
                    accumulatedFrecuency += frecuencies[i]
                    if(accumulatedFrecuency >= data + 1):
                        break
                data2 = classMark(startIntervals[i], endIntervals[i])
                return (data1 + data2) / 2
            else:
                data = (totalData + 1) / 2
                for i in range(0, len(startIntervals)):
                    accumulatedFrecuency += frecuencies[i]
                    if(accumulatedFrecuency >= data):
                        break
            return classMark(startIntervals[i], endIntervals[i])
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")

def mode(startIntervals, endIntervals=None, frecuencies=None):
    #Check if there is only 1 list.
    if((startIntervals is not None) and (endIntervals is None) and (frecuencies is None)):
        #Declare variables
        dataFrecuency = {}
        modes = []
        for i in range(0, len(startIntervals)):
            try:
                dataFrecuency[startIntervals[i]] += 1
            except:
                dataFrecuency[startIntervals[i]] = 1
        biggerFrecuency = max(dataFrecuency.values())
        if(biggerFrecuency != 1):
            for key, value in dataFrecuency.items():
                if(biggerFrecuency == value):
                    modes.append(key)
            if(len(modes) != len(dataFrecuency)):
                return modes
            else:
                return "amodal"
        else:
            return "amodal"
    #Check if there are 3 lists.
    elif((startIntervals is not None) and (endIntervals is not None) and (frecuencies is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals) == len(frecuencies)):
            #Declare variables
            dataFrecuency = {}
            modes = []
            for i in range(0, len(startIntervals)):
                dataFrecuency[(startIntervals[i], endIntervals[i])] = frecuencies[i]
            biggerFrecuency = max(dataFrecuency.values())
            if(biggerFrecuency != 1):
                for key, value in dataFrecuency.items():
                    if(biggerFrecuency == value):
                        modes.append(key)
                if(len(modes) != len(dataFrecuency)):
                    return modes
                else:
                    return "amodal"
            else:
                return "amodal"
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")

def amplitude(startIntervals, endIntervals=None):
    #Check if there is only 1 list.
    if((startIntervals is not None) and (endIntervals is None)):
        return max(startIntervals) - min(startIntervals)
    #Check if there are 3 lists.
    elif((startIntervals is not None) and (endIntervals is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals)):
            intervals = list(zip(startIntervals, endIntervals))
            intervals.sort(key=lambda x: x[0])
            return intervals[-1][1] - intervals[0][0]
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")

def geometricMean(startIntervals, endIntervals=None, frecuencies=None):
    #Set variables
    multiplicationMean = 1
    #Check if there is only 1 list.
    if((startIntervals is not None) and (endIntervals is None) and (frecuencies is None)):
        for i in range(0, len(startIntervals)):
            multiplicationMean *= startIntervals[i]
        return multiplicationMean ** (1 / len(startIntervals))
    #Check if there are 3 lists.
    elif((startIntervals is not None) and (endIntervals is not None) and (frecuencies is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals) == len(frecuencies)):
            for i in range(0, len(startIntervals)):
                multiplicationMean *= classMark(startIntervals[i], endIntervals[i]) * frecuencies[i]
            return multiplicationMean ** (1 / sum(frecuencies))
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")

def aritmeticMean(startIntervals, endIntervals=None, frecuencies=None):
    #Set variables
    sumMean = 0
    #Check if there is only 1 list.
    if((startIntervals is not None) and (endIntervals is None) and (frecuencies is None)):
        for i in range(0, len(startIntervals)):
            sumMean += startIntervals[i]
        return sumMean / len(startIntervals)
    #Check if there are 3 lists.
    elif((startIntervals is not None) and (endIntervals is not None) and (frecuencies is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals) == len(frecuencies)):
            for i in range(0, len(startIntervals)):
                sumMean += classMark(startIntervals[i], endIntervals[i]) * frecuencies[i]
            return sumMean / sum(frecuencies)
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")

def meanDeviation(startIntervals, endIntervals=None, frecuencies=None):
    #Set variables
    sumMeanDeviation = 0
    #Check if there is only 1 list.
    if((startIntervals is not None) and (endIntervals is None) and (frecuencies is None)):
        meanDeviation = aritmeticMean(startIntervals)
        for i in range(0, len(startIntervals)):
            sumMeanDeviation += abs(startIntervals[i] - meanDeviation)
        return sumMeanDeviation / len(startIntervals)
    #Check if there are 3 lists.
    elif((startIntervals is not None) and (endIntervals is not None) and (frecuencies is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals) == len(frecuencies)):
            meanDeviation = aritmeticMean(startIntervals, endIntervals, frecuencies)
            for i in range(0, len(startIntervals)):
                sumMeanDeviation += abs(classMark(startIntervals[i], endIntervals[i]) - meanDeviation) * frecuencies[i]
            return sumMeanDeviation / sum(frecuencies)
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")
    
def variance(startIntervals, endIntervals=None, frecuencies=None):
    #Set variables
    sumVariance = 0
    #Check if there is only 1 list.
    if((startIntervals is not None) and (endIntervals is None) and (frecuencies is None)):
        meanVariance = aritmeticMean(startIntervals)
        for i in range(0, len(startIntervals)):
            sumVariance += (startIntervals[i] - meanVariance) ** 2
        return sumVariance / len(startIntervals)
    #Check if there are 3 lists.
    elif((startIntervals is not None) and (endIntervals is not None) and (frecuencies is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals) == len(frecuencies)):
            meanVariance = aritmeticMean(startIntervals, endIntervals, frecuencies)
            for i in range(0, len(startIntervals)):
                sumVariance += ((classMark(startIntervals[i], endIntervals[i]) - meanVariance) ** 2) * frecuencies[i]
            return sumVariance / sum(frecuencies)
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")

def standarDeviation(startIntervals, endIntervals=None, frecuencies=None):
    return variance(startIntervals, endIntervals, frecuencies) * (1/2)

def permutation(amountData, repetitions=None):
    #Check if there is only 1 list.
    if((amountData is not None) and ((repetitions is None) or (repetitions is False))):
        return factorial(amountData)
    #Check if there are 2 lists.
    elif((amountData is not None) and (repetitions is not None)):
        #Declare initial variable.
        multiplicacionRepetitions = 1
        for repetition in repetitions:
            multiplicacionRepetitions *= repetition
        return factorial(amountData) / multiplicacionRepetitions
    else:
        raise ValueError("Error: Missing parameters.")
    
def variation(amountData, choosen, repetitions=None):
    #Revisar si solo se introdujeron dos listas
    if((amountData is not None) and (choosen is not None) and ((repetitions is None) or (repetitions is False))):
        return factorial(amountData) / factorial(amountData - choosen)
    #Check if there are 3 lists.
    elif((amountData is not None) and (choosen is not None) and (repetitions is not None)):
        return amountData ** choosen
    else:
        raise ValueError("Error: Missing parameters.")
    
def combination(amountData, choosen, repetitions=None):
    #Check if there is only 1 list.
    if((amountData is not None) and (choosen is not None) and ((repetitions is None) or (repetitions is False))):
        return factorial(amountData) / (factorial(choosen) * factorial(amountData - choosen))
    #Check if there are 3 lists.
    elif((amountData is not None) and (choosen is not None) and (repetitions is not None)):
        return factorial(amountData + choosen - 1) / (factorial(amountData - 1) * factorial(choosen))
    else:
        raise ValueError("Error: Missing parameters.")
    
def quartile(wantedPart, startIntervals, endIntervals=None, frecuencies=None):
    #Check if there is only 1 list.
    if((wantedPart is not None) and (startIntervals is not None) and (endIntervals is None) and (frecuencies is None)):
        dataPosition = int((wantedPart * len(startIntervals)) / 4)
        startIntervals.sort()
        if(dataPosition == 0):
            return startIntervals[0]
        else:
            return startIntervals[dataPosition - 1]
    #Check if there are 3 lists.
    elif((wantedPart is not None) and (startIntervals is not None) and (endIntervals is not None) and (frecuencies is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals) == len(frecuencies)):
            totalData = sum(frecuencies)
            dataPosition = (wantedPart * totalData) / 4
            accumulatedFrecuency = 0
            for i in range(0, len(startIntervals)):
                accumulatedFrecuency += frecuencies[i]
                if(accumulatedFrecuency >= dataPosition):
                    previousAccumulatedFrecuency = accumulatedFrecuency - frecuencies[i]
                    break
            intervals = [startIntervals[i], endIntervals[i]]
            classAmplitude = intervals[1] - intervals[0]
            return intervals[0] + ((dataPosition - previousAccumulatedFrecuency) / frecuencies[i]) * classAmplitude
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")
    
def quintile(wantedPart, startIntervals=None, endIntervals=None, frecuencies=None):
    #Check if there is only 1 list.
    if((wantedPart is not None) and (startIntervals is not None) and (endIntervals is None) and (frecuencies is None)):
        dataPosition = int((wantedPart * len(startIntervals)) / 5)
        startIntervals.sort()
        if(dataPosition == 0):
            return startIntervals[0]
        else:
            return startIntervals[dataPosition - 1]
    #Check if there are 3 lists.
    elif((wantedPart is not None) and (startIntervals is not None) and (endIntervals is not None) and (frecuencies is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals) == len(frecuencies)):
            totalData = sum(frecuencies)
            dataPosition = (wantedPart * totalData) / 5
            accumulatedFrecuency = 0
            for i in range(0, len(startIntervals)):
                accumulatedFrecuency += frecuencies[i]
                if(accumulatedFrecuency >= dataPosition):
                    previousAccumulatedFrecuency = accumulatedFrecuency - frecuencies[i]
                    break
            intervals = [startIntervals[i], endIntervals[i]]
            classAmplitude = intervals[1] - intervals[0]
            return intervals[0] + ((dataPosition - previousAccumulatedFrecuency) / frecuencies[i]) * classAmplitude
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")
    
def decile(wantedPart, startIntervals=None, endIntervals=None, frecuencies=None):
    #Check if there is only 1 list.
    if((wantedPart is not None) and (startIntervals is not None) and (endIntervals is None) and (frecuencies is None)):
        dataPosition = int((wantedPart * len(startIntervals)) / 10)
        startIntervals.sort()
        if(dataPosition == 0):
            return startIntervals[0]
        else:
            return startIntervals[dataPosition - 1]
    #Check if there are 3 lists.
    elif((wantedPart is not None) and (startIntervals is not None) and (endIntervals is not None) and (frecuencies is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals) == len(frecuencies)):
            totalData = sum(frecuencies)
            dataPosition = (wantedPart * totalData) / 10
            accumulatedFrecuency = 0
            for i in range(0, len(startIntervals)):
                accumulatedFrecuency += frecuencies[i]
                if(accumulatedFrecuency >= dataPosition):
                    previousAccumulatedFrecuency = accumulatedFrecuency - frecuencies[i]
                    break
            intervals = [startIntervals[i], endIntervals[i]]
            classAmplitude = intervals[1] - intervals[0]
            return intervals[0] + ((dataPosition - previousAccumulatedFrecuency) / frecuencies[i]) * classAmplitude
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")
    
def percentile(wantedPart, startIntervals, endIntervals=None, frecuencies=None):
    #Check if there is only 1 list.
    if((wantedPart is not None) and (startIntervals is not None) and (endIntervals is None) and (frecuencies is None)):
        dataPosition = int((wantedPart * len(startIntervals)) / 100)
        startIntervals.sort()
        if(dataPosition == 0):
            return startIntervals[0]
        else:
            return startIntervals[dataPosition - 1]
    #Check if there are 3 lists.
    elif((wantedPart is not None) and (startIntervals is not None) and (endIntervals is not None) and (frecuencies is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals) == len(frecuencies)):
            totalData = sum(frecuencies)
            dataPosition = (wantedPart * totalData) / 100
            accumulatedFrecuency = 0
            for i in range(0, len(startIntervals)):
                accumulatedFrecuency += frecuencies[i]
                if(accumulatedFrecuency >= dataPosition):
                    previousAccumulatedFrecuency = accumulatedFrecuency - frecuencies[i]
                    break
            intervals = [startIntervals[i], endIntervals[i]]
            classAmplitude = intervals[1] - intervals[0]
            return intervals[0] + ((dataPosition - previousAccumulatedFrecuency) / frecuencies[i]) * classAmplitude
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")

def normalDistribution(mean, deviation, condition):
    #Check if there are 3 values.
    if((mean is not None) and (deviation is not None) and (condition is not None)):
        #Importat la funcion erf desde math
        from math import erf
        #Declare initial variables.
        zScale = (condition - mean) / deviation
        return 0.5 * (1 + erf(zScale / (2 ** (1/2))))
    else:
        raise ValueError("Error: Missing parameters.")

def binomialDistribution(totalExperiments, condition, successProbability):
    #Check if there are 3 values.
    if((totalExperiments is not None) and (condition is not None) and (successProbability is not None)):
        #Declare initial variables.
        failProbability = 1 - successProbability
        return combination(totalExperiments, condition) * (successProbability ** condition) * (failProbability ** (totalExperiments - condition))
    else:
        raise ValueError("Error: Missing parameters.")
    
def geometricDistribution(firstSuccess, successProbability):
    #Check if there are 3 values.
    if((firstSuccess is not None) and (successProbability is not None)):
        #Declare initial variables.
        failProbability = 1 - successProbability
        return successProbability * failProbability ** (firstSuccess - 1)
    else:
        raise ValueError("Error: Missing parameters.")
    
def hypergeometricDistribution(sample, sampleSuccess, population, successPopulation):
    #Check if there are 3 values.
    if((sample is not None) and (sampleSuccess is not None) and (population is not None) and (successPopulation is not None)):
        return (combination(successPopulation, sampleSuccess) * combination(population - successPopulation, sample - sampleSuccess)) / combination(population, sample)
    else:
        raise ValueError("Error: Missing parameters.")

def studentDistribution(sample, sampleMean, popuationMean, deviation):
    #Check if there are 3 values.
    if((sample is not None) and (sampleMean is not None) and (popuationMean is not None) and (deviation is not None)):
        return (sampleMean - popuationMean) / (deviation / (sample ** (1/2)))
    else:
        raise ValueError("Error: Missing parameters.")
    
def symmetry(startIntervals, endIntervals=None, frecuencies=None):
    #Declare initial variables.
    mean = aritmeticMean(startIntervals, endIntervals, frecuencies)
    symmetrySum = 0
    #Check if there is only 1 list.
    if((startIntervals is not None) and (endIntervals is None) and (frecuencies is None)):
        for i in range(0, len(startIntervals)):
            symmetrySum += (startIntervals[i] - mean) ** 3
        return symmetrySum / (len(startIntervals) * (standarDeviation(startIntervals) ** 3))
    #Check if there are 3 lists.
    elif((startIntervals is not None) and (endIntervals is not None) and (frecuencies is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals) == len(frecuencies)):
            for i in range(0, len(startIntervals)):
                symmetrySum += ((classMark(startIntervals[i], endIntervals[i]) - mean) ** 3) * frecuencies[i]
            return symmetrySum / (sum(frecuencies) * (standarDeviation(startIntervals, endIntervals, frecuencies) ** 3))
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")

def kurtosis(startIntervals, endIntervals=None, frecuencies=None):
    #Declare initial variables.
    mean = aritmeticMean(startIntervals, endIntervals, frecuencies)
    sumKurtosis = 0
    #Check if there is only 1 list.
    if((startIntervals is not None) and (endIntervals is None) and (frecuencies is None)):
        for i in range(0, len(startIntervals)):
            sumKurtosis += (startIntervals[i] - mean) ** 4
        return sumKurtosis / (len(startIntervals) * (standarDeviation(startIntervals) ** 4))
    #Check if there are 3 lists.
    elif((startIntervals is not None) and (endIntervals is not None) and (frecuencies is not None)):
        #Check if the lists contain all the data.
        if(len(startIntervals) == len(endIntervals) == len(frecuencies)):
            for i in range(0, len(startIntervals)):
                sumKurtosis += ((classMark(startIntervals[i], endIntervals[i]) - mean) ** 4) * frecuencies[i]
            return sumKurtosis / (sum(frecuencies) * (standarDeviation(startIntervals, endIntervals, frecuencies) ** 4))
        else:
            raise ValueError("Error: Missing parameters.")
    else:
        raise ValueError("Error: Missing parameters.")

while __name__ == "__main__":
    try:
        print()
        print("This is the visual module.")
        print("\n     ######       ######     \n   ##   #           #   ##   \n  #    #             #    #  \n #    ###           ###    # \n #   #                 #   # \n#   #                   #   #\n#   #                   #   #\n#   #                   #   #\n#   #                   #   #\n#   #                   #   #\n#   #                   #   #\n#    #                 #    #\n #    #   #########   #    # \n  #    ###         ###    #  \n  #                       #  \n   #                     #   \n   #                     #   \n   #                     #   \n   #                     #   \n   #    ###       ###    #   \n   #   #####     #####   #   \n   #  #######   #######  #   \n   #  #######   #######  #   \n   #  #######   #######  #   \n   #   #####     #####   #   \n   #    ###       ###    #   \n   #                     #   \n   #                     #   \n   #                     #   \n    #                   #    \n     ##               ##     \n       ###############       \n")
        print("Available modules:")
        print("1. Central tendency measures.")
        print("2. Dispersion measures.")
        print("3. Position measures.")
        print("4. Combinatorics")
        print("5. Distribution.")
        choosenModule = input("Enter the module: ")
        keepModule = True
        if(choosenModule == "1"):
            while keepModule:
                #Declare variables
                data = []
                endIntervals = None
                frecuencies = None
                print()
                print("This module has 2 data types.")
                print("1. Loose data.")
                print("2. Grouped data.")
                typeData = int(input("Enter the data type: "))
                keepData = True
                print()
                if(typeData == 1):
                    amountData = int(input("Enter the amount of data: "))
                    print()
                    for i in range(0, amountData):
                        data.append(float(input(f"Enter the data {i + 1}: ")))
                elif(typeData == 2):
                    endIntervals = []
                    frecuencies = []
                    amountData = int(input("Enter the amount of intervals: "))
                    for i in range(0, amountData):
                        print()
                        data.append(float(input(f"Enter the start of the interval {i + 1}: ")))
                        endIntervals.append(float(input(f"Enter the end of the interval {i + 1}: ")))
                        frecuencies.append(float(input(f"Enter the frecuency of the interval {i + 1}: ")))
                else:
                    print("Wrong data type.")
                    continue
                #Functions, keeping the data
                while keepData:
                    print()
                    print("Available functions:")
                    print("0. Leave module.")
                    print("1. Change data.")
                    print("2. Aritmetic mean.")
                    print("3. Geometric mean.")
                    print("4. Mode.")
                    print("5. median.")
                    choosenFunction = int(input("Enter the choosen function: "))
                    print()
                    if(choosenFunction == 0):
                        keepModule = False
                        keepData = False
                    elif(choosenFunction == 1):
                        keepData = False
                    elif(choosenFunction == 2):
                        print(f"The aritmetic mean is: {aritmeticMean(data, endIntervals, frecuencies)}.")
                    elif(choosenFunction == 3):
                        print(f"The geometric mean is: {geometricMean(data, endIntervals, frecuencies)}.")
                    elif(choosenFunction == 4):
                        print(f"The mode is: {mode(data, endIntervals, frecuencies)}.")
                    elif(choosenFunction == 5):
                        print(f"The median is: {median(data, endIntervals, frecuencies)}.")
                    else:
                        print("Function not available.")
        elif(choosenModule == "2"):
            while keepModule:
                data = []
                endIntervals = None
                frecuencies = None
                print()
                print("This module has 2 data types.")
                print("1. Loose data.")
                print("2. Grouped data.")
                typeData = int(input("Enter the data type: "))
                keepData = True
                print()
                if(typeData == 1):
                    amountData = int(input("Enter the amount of data: "))
                    print()
                    for i in range(0, amountData):
                        data.append(float(input(f"Enter the data {i + 1}: ")))
                elif(typeData == 2):
                    endIntervals = []
                    frecuencies = []
                    amountData = int(input("Enter the amount of intervals: "))
                    print()
                    for i in range(0, amountData):
                        data.append(float(input(f"Enter the start of the interval {i + 1}: ")))
                        endIntervals.append(float(input(f"Enter the end of the interval {i + 1}: ")))
                        frecuencies.append(float(input(f"Enter the frecuency of the interval {i + 1}: ")))
                else:
                    print("Wrong data type.")
                    continue
                #Functions, keeping the data
                while keepData:
                    print()
                    print("Available functions:")
                    print("0. Leave module.")
                    print("1. Change data.")
                    print("2. Amplitude.")
                    print("3. Mean deviation.")
                    print("4. Variance.")
                    print("5. Standar deviation.")
                    print("6. Symmetry")
                    print("7. Kurtosis")
                    choosenFunction = int(input("Enter the choosen function: "))
                    print()
                    if(choosenFunction == 0):
                        keepModule = False
                        keepData = False
                    elif(choosenFunction == 1):
                        keepData = False
                    elif(choosenFunction == 2):
                        print(f"The amplitude is: {amplitude(data, endIntervals)}.")
                    elif(choosenFunction == 3):
                        print(f"The mean deviation is: {meanDeviation(data, endIntervals, frecuencies)}.")
                    elif(choosenFunction == 4):
                        print(f"The variance is: {variance(data, endIntervals, frecuencies)}.")
                    elif(choosenFunction == 5):
                        print(f"The standar deviation is: {standarDeviation(data, endIntervals, frecuencies)}.")
                    elif(choosenFunction == 6):
                        print(f"The symmetry is: {symmetry(data, endIntervals, frecuencies)}")
                    elif(choosenFunction == 7):
                        print(f"The kurtosis is: {kurtosis(data, endIntervals, frecuencies)}")
                    else:
                        print("Function not available.")
        elif(choosenModule == "3"):
            while keepModule:
                data = []
                endIntervals = None
                frecuencies = None
                print()
                print("This module has 2 data types.")
                print("1. Loose data.")
                print("2. Grouped data.")
                typeData = int(input("Enter the data type: "))
                keepData = True
                print()
                if(typeData == 1):
                    amountData = int(input("Enter the amount of data: "))
                    print()
                    for i in range(0, amountData):
                        data.append(float(input(f"Enter the data {i + 1}: ")))
                elif(typeData == 2):
                    endIntervals = []
                    frecuencies = []
                    amountData = int(input("Enter the amount of intervals: "))
                    print()
                    for i in range(0, amountData):
                        data.append(float(input(f"Enter the start of the interval {i + 1}: ")))
                        endIntervals.append(float(input(f"Enter the end of the interval {i + 1}: ")))
                        frecuencies.append(float(input(f"Enter the frecuency of the interval {i + 1}: ")))
                else:
                    print("Wrong data type.")
                    continue
                #Functions, keeping the data
                while keepData:
                    print()
                    print("Available functions:")
                    print("0. Leave module.")
                    print("1. Change data.")
                    print("2. Quartile.")
                    print("3. Quintile.")
                    print("4. Decile.")
                    print("5. Percentile.")
                    choosenFunction = int(input("Enter the choosen function: "))
                    print()
                    if(choosenFunction == 0):
                        keepModule = False
                        keepData = False
                    elif(choosenFunction == 1):
                        keepData = False
                    elif(choosenFunction == 2):
                        wantedPart = int(input("Wanted quatile: "))
                        print(f"The quartile {wantedPart} is: {quartile(wantedPart, data, endIntervals, frecuencies)}.")
                    elif(choosenFunction == 3):
                        wantedPart = int(input("Wanted quintile: "))
                        print(f"The quintile {wantedPart} is: {quintile(wantedPart, data, endIntervals, frecuencies)}.")
                    elif(choosenFunction == 4):
                        wantedPart = int(input("Wanted decile: "))
                        print(f"The decile {wantedPart} is: {decile(wantedPart, data, endIntervals, frecuencies)}.")
                    elif(choosenFunction == 5):
                        wantedPart = int(input("Wanted percentile: "))
                        print(f"The percentile {wantedPart} is: {percentile(wantedPart, data, endIntervals, frecuencies)}.")
                    else:
                        print("Function not available.")
        elif(choosenModule == "4"):
            while keepModule:
                print()
                print("Available functions:")
                print("0. Leave module.")
                print("1. Permutation.")
                print("2. Variation.")
                print("3. Combination.")
                choosenFunction = int(input("Enter the choosen function: "))
                print()
                if(choosenFunction == 0):
                    keepModule = False
                elif(choosenFunction == 1):
                    amountData = int(input("Enter the amount of data: "))
                    repetition = input("With repetition (Y or N)? ").lower()
                    if(repetition == "y"):
                        #Declare variables
                        repetitions = []
                        amountRepetitions = int(input("Enter the amount of data that repeats more than once: "))
                        for i in range(0, amountRepetitions):
                            repetitions.append(int(input(f"Enter the repetitions of the data {i + 1}: ")))
                        print(f"The total permutations are: {permutation(amountData, repetitions)}.")
                    elif(repetition == "n"):
                        print(f"The total permutations are: {permutation(amountData)}.")
                    else:
                        print("Invalid answer.")
                elif(choosenFunction == 2):
                    amountData = int(input("Enter the amount of data: "))
                    choosen = int(input("Amount of data choosen:"))
                    repetition = input("With repetition (Y or N)? ").lower()
                    if(repetition == "y"):
                        print(f"The total variations are: {variation(amountData, choosen, bool(repetition))}.")
                    elif(repetition == "n"):
                        print(f"The total variations are: {variation(amountData, choosen)}.")
                    else:
                        print("Invalid answer.")
                elif(choosenFunction == 3):
                    amountData = int(input("Enter the amount of data: "))
                    choosen = int(input("Amount of data choosen:"))
                    repetition = input("With repetition (Y or N)? ").lower()
                    if(repetition == "y"):
                        print(f"The total combinations are: {combination(amountData, choosen, bool(repetition))}.")
                    elif(repetition == "n"):
                        print(f"The total combinations are: {combination(amountData, choosen)}.")
                    else:
                        print("Invalid answer.")
                else:
                    print("Function not available.")
        elif(choosenModule == "5"):
             while keepModule:
                print()
                print("Available functions:")
                print("0. Leave module.")
                print("1. Normal distribution.")
                print("2. Binomial distribution.")
                print("3. Geometric distribution.")
                print("4. Hypergeometric distribution.")
                print("5. Student distribution.")
                choosenFunction = int(input("Enter the choosen function: "))
                print()
                if(choosenFunction == 0):
                    keepModule = False
                elif(choosenFunction == 1):
                    mean = float(input("Enter the mean: "))
                    deviation = float(input("Enter the standar deviation: "))
                    condition = float(input("Enter the condition: "))
                    print(f"The normal distribution is {normalDistribution(mean, deviation, condition)}.")
                elif(choosenFunction == 2):
                    totalExperiments = int(input("Enter the amount of experiments: "))
                    condition = int(input("Enter the condition: "))
                    successProbability = float(input("Enter the success probability(Decimal): "))
                    print(f"The binomial distribution is {binomialDistribution(totalExperiments, condition, successProbability)}.")
                elif(choosenFunction == 3):
                    firstSuccess = int(input("First successfull experiment(Number): "))
                    successProbability = int(input("Enter the success probability(Decimal): "))
                    print(f"The geometric distribution is {geometricDistribution(firstSuccess, successProbability)}.")
                elif(choosenFunction == 4):
                    sample = int(input("Sample size: "))
                    sampleSuccess = int(input("Number of success from the sample: "))
                    population = int(input("Population size: "))
                    successPopulation = int(input("Number of success from the population: "))
                    print(f"The hypergeometric distribution is {hypergeometricDistribution(sample, sampleSuccess, population, successPopulation)}.")
                elif(choosenFunction == 5):
                    sample = int(input("Sample size: "))
                    sampleMean = float(input("Sample mean: "))
                    popuationMean = float(input("Population mean: "))
                    deviation = float(input("Enter the standar deviation: "))
                    print(f"The Student distribution is {studentDistribution(sample, sampleMean, popuationMean, deviation)}.")
                else:
                    print("Function not available.")
        else:
            print("Module not available.")
    except Exception as e:
        print(f"An error has occurred: {e}.")