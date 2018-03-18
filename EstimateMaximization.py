import numpy as np
from CurrentProbabilities import CurrentProbabilities
from LocationEnum import Category
from ProbabilityValues import ProbabilityValues
from VariableElimination import inference


G=0
D=1
F=2
DS=3
S=4

variables = np.array(['G','D','F','DS','S'])
values = np.array(['false','true'])

false=0
true=1

def countD1(truthtable):
    pass


def generateFactors(estimates):
    factors = []
    cpt_s = estimates.sloepnea
    cpt_f = estimates.foriennditis
    cpt_ds = estimates.degarspots
    cpt_g = estimates.gene
    cpt_d = estimates.dunetts

    # Pr(G)
    f0 = cpt_g.reshape(2, 1, 1, 1, 1)
    factors.append(f0)

    # Pr(D)
    f1 = cpt_d.reshape(1, 6, 1, 1, 1)
    factors.append(f1)

    # Pr(D|F)
    f2 = cpt_s.reshape(1, 6, 2, 1, 1)
    factors.append(f2)

    # Pr(D|DS)
    f3 = cpt_ds.reshape(1, 3, 2, 1, 1)
    factors.append(f3)

    # Pr(D|S, G)
    f4 = cpt_f.reshape(2, 3, 1, 1, 2)
    factors.append(f4)

    return factors


def generateEvidenceList(truthTableKey):
    evidence = {}
    evidence["S"] = 1 if(truthTableKey[Category.SLOEPNEA] == 1) else 0
    evidence["F"] = 1 if (truthTableKey[Category.FORIENNDITIS] == 1) else 0
    evidence["DS"] = 1 if (truthTableKey[Category.DEGARSPOTS] == 1) else 0
    evidence["G"] = 1 if (truthTableKey[Category.GENE] == 1) else 0
    return map(list, evidence.items())


def populateTruthTableByCalculatingProbabilities(estimates, truthtable):
    factorList = generateFactors(estimates)
    for row in truthtable:
        evidenceList = generateEvidenceList(row.key)
        soln = inference(factorList, D, [], evidenceList)
        print soln


def initializeVariableProabilityTables():
    truthtable = list()
    for f in range(0, 2):
        for s in range (0, 2):
            for ds in range (0, 2):
                for g in range (0, 2):
                    for d in range (0, 3):
                        truthtable.append(ProbabilityValues([f, s, ds, g, d]))
    return truthtable


# Generate CPT Estimates
def generatedFactorValues(estimated):
    estimated.populateFactors()
    pass


def setInitialEstimates(cpt_sdg, cpt_dsd, cpt_fd, cpt_g, cpt_d ):
    # foriennditis, degarspots, sloepnea, trimo_gene, dunetts
    # Explore possible use of 5-D arrays to store probabilities
    # sloepnea, foriennditis, degarspots, trimo_gene, dunetts
    estimated = CurrentProbabilities(cpt_sdg, cpt_dsd, cpt_fd, cpt_g, cpt_d)
    return estimated

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

    # sloepnea, foriennditis, degarspots, trimo_gene, dunetts
    cpt_s = [[0.01, 0.19, 0.80],[0.01, 0.19, 0.80]]
    cpt_f = [0.01, 0.19, 0.80]
    cpt_ds = [0.02, 0.49, 0.49]
    cpt_g = [0.10]
    cpt_d = [0.50, 0.25, 0.25]

    estimates = setInitialEstimates(cpt_s,cpt_f, cpt_ds, cpt_g, cpt_d)
    truthtable = initializeVariableProabilityTables()
    populateTruthTableByCalculatingProbabilities(estimates, truthtable)


#     Variable Elimination Example
#     model = BayesianModel([('D', 'S'), ('D', 'DS'), ('D', 'S'), ('G', 'S')])
#     # P(D)
#     cpd_d = TabularCPD(variable='D', variable_card=3, values=[[0.50, 0.25, 0.25]])
#     # P(G)
#     cpd_g = TabularCPD(variable='G', variable_card=2, values=[[0.90, 0.10]])
#     # P(F|D)
#     cpd_g = TabularCPD(variable='F', variable_card=2,
#                        values=[[0.98, 0.15, 0.40],
#                                [0.02, 0.85, 0.60]],
#                        evidence=['D'],
#                        evidence_card=[3])
#     print(cpd_g)



if __name__ == "__main__": main()