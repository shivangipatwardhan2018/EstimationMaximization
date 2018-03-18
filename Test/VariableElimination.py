from collections import deque

from Factor import *
import math



def initializedTuple(length):
    tupleList = []
    if length == 1:
        tupleList.append(1)
        return tuple(tupleList)
    elif length == 2:
        tupleList.append(2)
        return tuple(tupleList)
    else:
        for i in range(0, int(math.sqrt(length))):
            tupleList.append(2)
        return tuple(tupleList)

def restrict(factorInput, variableInput, valueInput):
    print "Restricting Factors Based On Variable: " + str(variableInput)
    varIndex = factorInput.variables.index(variableInput)
    factorInput.variables.remove(variableInput)

    it = np.nditer(factorInput.array, flags=['multi_index'], op_flags=['readonly'])
    filteredList = []
    while not it.finished:
        coordinateList = list(it.multi_index)
        if(coordinateList[varIndex] == valueInput):
            del coordinateList[varIndex]
            filteredList.append(factorInput.array[it.multi_index])
        it.iternext()
    newDimensions = initializedTuple(len(filteredList))
    factorInput.array = np.asarray(filteredList).reshape(newDimensions)
    return factorInput


def findCommonVariable(variables, variables1):
    commonList =  list(set(variables).intersection(variables1))
    return commonList


def getVariableIndex(var):
    if var == 'G':
       return 0
    elif var == 'D':
        return 1
    elif var == 'F':
        return 2
    elif var == 'DS':
        return 3
    elif var == 'S':
        return 4

def multiply(factor1, factor2):
    largeFactor = factor1 if factor1.array.ndim >= factor2.array.ndim else factor2
    smallFactor = factor1 if factor1.array.ndim < factor2.array.ndim else factor2

    variableListFactor1 = factor1.variables
    coordList1 = [1] * 5
    for var in variableListFactor1:
        index = getVariableIndex(var)
        if (index == 1):
            coordList1[index] = 3
        else:
            coordList1[index] = 2
    coordTuple1 = tuple(coordList1)
    factor1Temp = factor1.array.reshape(coordTuple1)

    variableListFactor2 = factor2.variables
    coordList2 = [1] * 5
    for var in variableListFactor2:
        index = getVariableIndex(var)
        if(index == 1):
            coordList2[index] = 3
        else:
            coordList2[index] = 2

    coordTuple2 = tuple(coordList2)
    factor2Temp = factor2.array.reshape(coordTuple2)

    soln = np.squeeze(factor1Temp * factor2Temp)
    variables = largeFactor.variables + list(set(smallFactor.variables) - set(largeFactor.variables))
    return Factor(variables, soln)


def sumout(factor,variable):
    var = factor.variables[variable]
    factor.variables.remove(var)
    factor.array = np.sum(factor.array, axis=variable, keepdims=False)
    return factor


def getFactorsWhichContainVariable(factorList, commonVariable):
    filteredFactorList = []
    for index in range(0, len(factorList)):
        if commonVariable in factorList[index].variables:
            filteredFactorList.append(factorList[index])
    return filteredFactorList


def normalize(factor):
    return factor.array / np.sum(factor.array.flatten())


def inference(factorList, queryVariables, listOfHiddenVariables, evidenceList):
    print "RESTRICT VARIABLES"
    for evidence, value in evidenceList.iteritems():
        for index in range(0, len(factorList)):
            variablesList = factorList[index].variables
            if(evidence in variablesList):
                factorList[index] = restrict(factorList[index], evidence, value)
                # print "Restricted {0} to {1} within: \n {2}".format(evidence, value, factorList[index])
    printfactorList(factorList)

    for element in listOfHiddenVariables:

        print "\nEliminating: " + str(element)

        listOfFactorsToMultiply = getFactorsWhichContainVariable(factorList, element)
        numElementsFound = len(listOfFactorsToMultiply)
        if(numElementsFound > 1):
            print "MULTIPLY FACTORS"
            while(len(listOfFactorsToMultiply) > 1):
                productArray = multiply(listOfFactorsToMultiply[0], listOfFactorsToMultiply[1])
                factorList.remove(listOfFactorsToMultiply[0])
                factorList.remove(listOfFactorsToMultiply[1])
                factorList.append(productArray)
                print "Factor Added: f{} and array \n \t {} \n ".format(productArray.variables, productArray.array)
                listOfFactorsToMultiply = getFactorsWhichContainVariable(factorList, element)
        elif (numElementsFound == 1):
            productArray = listOfFactorsToMultiply[0]
        elif (numElementsFound == 0):
            continue

        if(productArray.array.ndim > 1):
            print "SUMOUT VARIABLE"
            if(element in productArray.variables):
                indexOfVariable = productArray.variables.index(element)
                productArray = sumout(productArray, indexOfVariable)
                print productArray

    print "\n Remaining factors:"
    printfactorList(factorList)
    answer = factorList[0]
    for factor in factorList[1:]:
        answer = multiply(answer, factor)

    print "\n ** FINAL NORMALIZED SOLUTION ** "
    answer = normalize(answer)
    print answer


def printfactorList(factorList):
    print " *** FACTOR LIST *** "
    for factor in factorList:
        print factor
    print " *** *********** *** "


#  FACTORS
# Pr(G)
f0 = Factor(['G'], np.array([0.90,0.1]))

# Pr(D)
f1 = Factor(['D'], np.array([0.50, 0.25, 0.25]))

# Pr(D|F)
f2 = Factor(['D', 'F'], np.array([[0.98,0.02],[0.40,0.60],[0.15, 0.85]]))

# Pr(D|DS)
f3 = Factor(['D', 'DS'], np.array([[0.98,0.02],[0.15,0.85],[0.40, 0.60]]))

# Pr(D|S, G)
f4 = Factor(['D', 'S', 'G'], np.array([[[0.98, 0.02],[0.15, 0.85],[0.15,0.85]],[[0.998,0.002],[0.98,0.02],[0.98,0.02]]]))


print " ========     Pr(D|DS,F,G, S)    ========"
factorList = [f0, f1, f2, f3, f4]
queryVariables = {'D'}
listOfHiddenVariables = []
evidenceList = {'G':1, 'DS':1, 'F':1, 'S':1}
inference(factorList, queryVariables, listOfHiddenVariables, evidenceList)
