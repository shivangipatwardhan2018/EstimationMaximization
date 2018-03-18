import numpy as np

# restrict function
def restrict(factor,variable,value):
    newShape = np.array(factor.shape)
    newShape[variable]=1
    sliceList = [slice(None)]*factor.ndim
    sliceList[variable]=value
    return factor[sliceList].reshape(newShape)

# sumout function
def sumout(factor,variable):
    return np.sum(factor,axis=variable,keepdims=True)

# multiply function
def multiply(factor1,factor2):
    return factor1*factor2

# normalize function
def normalize(factor):
    return factor / np.sum(factor.flatten())

# inference function
def inference(factorList,queryVariables,orderedListOfHiddenVariables,evidenceList):

    # restrict factors
    print "Restricting factors\n"
    for index in np.arange(len(factorList)):
        shape = np.array(factorList[index].shape)
        for evidence in evidenceList:
            if shape[evidence[0]] > 1:
                factorList[index] = restrict(factorList[index],evidence[0],evidence[1])
        shape = np.array(factorList[index].shape)
        print("f{}({})={}\n".format(index,variables[shape>1],np.squeeze(factorList[index])))

    # eliminate each hidden variable
    print "Eliminating hidden variables\n"
    hiddenId = 5
    for variable in orderedListOfHiddenVariables:
        print("Eliminating {}".format(variables[variable]))

        # find factors that contain the variable to be eliminated
        factorsToBeMultiplied = []
        for index in np.arange(len(factorList)-1,-1,-1):
            shape = np.array(factorList[index].shape)
            if shape[variable] > 1:
                factorsToBeMultiplied.append(factorList.pop(index))

        # multiply factors
        product = factorsToBeMultiplied[0]
        for factor in factorsToBeMultiplied[1:]:
            product = multiply(product,factor)

        # sumout variable
        newFactor = sumout(product,variable)
        factorList.append(newFactor)
        shape = np.array(newFactor.shape)
        hiddenId = hiddenId + 1
        print("New factor: f{}({})={}\n".format(hiddenId,variables[shape>1],np.squeeze(newFactor)))

    # multiply remaining factors
    print "Multiplying remaining factors"
    answer = factorList[0]
    for factor in factorList[1:]:
        answer = multiply(answer,factor)
        shape = np.array(answer.shape)
        print("Unnormalized answer: f{}({})={}\n".format(hiddenId+1,variables[shape>1],np.squeeze(answer)))

    # normalize answer
    print "Normalizing the answer"
    answer = normalize(answer)
    shape = np.array(answer.shape)
    print("Normalized answer: f{}({})={}\n".format(hiddenId+2,variables[shape>1],np.squeeze(answer)))
    return answer
#
# setup the Bayes net
# G=0
# D=1
# F=2
# DS=3
# S=4
#
# variables = np.array(['G','D','F','DS','S'])
# values = np.array(['false','true'])
#
# false=0
# true=1
#
# # Pr(G)
# f0 = np.array([0.90,0.1])
# f0 = f0.reshape(2,1,1,1,1)
# print ("Pr(G)={}\n".format(np.squeeze(f0)))
#
# # Pr(D)
# f1 = np.array([0.50, 0.25, 0.25])
# f1 = f1.reshape(1,3,1,1,1)
# print ("Pr(D)={}\n".format(np.squeeze(f1)))
#
# # Pr(D|F)
# f2 = np.array([[0.98,0.02],[0.40,0.60],[0.15, 0.85]])
# f2 = f2.reshape(1,3,2,1,1)
# print ("Pr(D|F)={}\n".format(np.squeeze(f2)))
#
# # Pr(D|DS)
# f3 = np.array([[0.98,0.02],[0.15,0.85],[0.40, 0.60]])
# f3 = f3.reshape(1,3,2,1,1)
# print ("Pr(D|DS)={}\n".format(np.squeeze(f3)))
# #
# # Pr(D|S, G)
# f4 = np.array([[[0.98, 0.02],[0.15, 0.85],[0.15,0.85]],[[0.998,0.002],[0.98,0.02],[0.98,0.02]]])
# f4 = f4.reshape(2,3,1,1,2)
# print ("Pr(D|S,G)={}\n".format(np.squeeze(f4)))
#
# #
# print "2b) Pr(D|DS,F,G, S)\n"
# factorList = [f0, f1, f2, f3, f4]
# f7 = inference(factorList,D,[],[[G,false], [DS,false], [F,true], [S,true]])
# print ("Pr(D|DS,F,G,S)={}\n".format(np.squeeze(f7)))
#
