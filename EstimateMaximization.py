

# Set initial estimates


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



if __name__ == "__main__": main()