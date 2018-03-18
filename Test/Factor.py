import copy
import numpy as np

class Factor:

    def setArray(self, newArray):
        self.array = newArray

    def setVariables(self, variableList):
        self.variables = variableList

    def getArray(self):
        return self.array

    def getVariables(self):
        return self.variables

    def __str__(self):
        return "Factor\n \t Variables: {0} \n \t Array: \n {1}  \n".format(self.variables, self.array, )

    # Copy Constructor
    def copy(self):
        return copy.deepcopy(self)

    # Normal Constructor
    def __init__(self, variables, array=None):

        self.variables = variables
        dimension = len(self.variables)
        if array is not None:
            self.array = array


        # Iterate though the array and set correct probabilities




