import ProbPy as ProbPy

from CurrentProbabilities import CurrentProbabilities
from LocationEnum import Category


def populateTruthTable(estimates, truthtable):
    pass
    # for element in truthtable:
    #     sloepneavalue = element.key[Category.SLOEPNEA]
    #     foriennditisvalue = element.key[Category.FORIENNDITIS]
    #     degarspotsvalue = element.key[Category.DEGARSPOTS]
    #     genevalue = element.key[Category.GENE]
    #     dunettsvalue = element.key[Category.DUNETTS]
    #     SgivenDprob = estimates.sloepnea[sloepneavalue]



def initializeVariableProabilityTables():
    truthtable = list()
    for f in range(0, 2):
        for s in range (0, 2):
            for ds in range (0, 2):
                for g in range (0, 2):
                    for d in range (0, 3):
                        truthtable.append([f, s, ds, g, d])
    return truthtable


# Set initial estimates
def setInitialEstimates():
    # sloepnea, foriennditis, degarspots, trimo_gene, dunetts
    return CurrentProbabilities([0.01, 0.19, 0.80], [0.01, 0.19, 0.80], [0.02, 0.49, 0.49], [0.10], [0.50, 0.25, 0.25])

# Read the Training or Testing Data based on the file name provided
def readData(fileName):
    inputdata = list()
    with open('dataset/'+fileName) as trainingData:
        testdata = trainingData.readlines()
        for pair in testdata:
            element = pair.lstrip().rstrip().split(" ")
            indexPairs = [int(index) for index in element]
            sloepnea, foriennditis, dengerspots, trimo_gene, dunetts = indexPairs
            diagnosis = [int(sloepnea), int(foriennditis), int(dengerspots), int(trimo_gene), int(dunetts)]
            inputdata.append(diagnosis)
        trainingData.close()
    return inputdata


def printList(trainingDiagnosis):
    for element in trainingDiagnosis:
        print(element)


def main():
    #     TRAINING
    trainingDiagnosis = readData('traindata.txt')
    printList(trainingDiagnosis)
    estimates = setInitialEstimates()
    truthtable = initializeVariableProabilityTables()
    truthtable = populateTruthTable(estimates, truthtable)



if __name__ == "__main__": main()