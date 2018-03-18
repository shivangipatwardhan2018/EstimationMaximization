import numpy as np


class CurrentProbabilities:

    # sloepnea, foriennditis, degarspots, trimo_gene, dunetts
    class __CurrentProbabilities:

        def __init__(self, sloepnea=None, foriennditis=None, degarspots=None, gene=None, dunetts=None):
            self.sloepnea = sloepnea
            self.foriennditis = foriennditis
            self.degarspots = degarspots
            self.gene = gene
            self.dunetts = dunetts

        def __str__(self):
            return " S: " + str(self.sloepnea)+ " \n \n  F: " + str(self.foriennditis) + "  \n  \n DS: " + str(self.degarspots) + " \n  \n  G: " + str(self.gene) + "  \n   \n D: " + str(self.dunetts)

    instance = None

    def __init__(self, sloepnea=None, foriennditis=None, degarspots=None, gene=None, dunetts=None):
        if not CurrentProbabilities.instance:
            CurrentProbabilities.instance = CurrentProbabilities.__CurrentProbabilities(self.generateSleopneaCpt(sloepnea),
                                                                                        self.generateForiennditisCpt(foriennditis),
                                                                                        self.generateDegarspotsCpt(degarspots),
                                                                                        self.generateGeneCpt(gene),
                                                                                        self.generateDunettsCpt(dunetts))
        else:
            CurrentProbabilities.instance.val = foriennditis, sloepnea, degarspots, gene, dunetts

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def generateGeneCpt(self, gene):
        return np.array([1.0 - gene[0], gene[0]])

    def generateDunettsCpt(self, dunetts):
        return np.array([[1.0 - dunetts[0], dunetts[0]],[1.0 - dunetts[1], dunetts[1]],[1.0 - dunetts[2], dunetts[2]]])

    def generateForiennditisCpt(self, foriennditis):
        # foriennditis[0.02, 0.60, 0.85]
        return np.array([[1.0 - foriennditis[0], foriennditis[0]],
                                          [1.0-foriennditis[1], foriennditis[1]],
                                          [1.0-foriennditis[2], foriennditis[2]]])

    def generateDegarspotsCpt(self, degarspots):
        # degarspots[0.02, 0.85, 0.60]
        return np.array([[1.0 - degarspots[0], degarspots[0]],
                                          [1.0 - degarspots[1], degarspots[1]],
                                          [1.0 - degarspots[2], degarspots[2]]])

    def generateSleopneaCpt(self, sloepnea):
        # degarspots[[0.02, 0.85, 0.60],
        #            [0.02, 0.85, 0.02]]
        return np.array([[[1.0 - sloepnea[0][0], sloepnea[0][0]],
                                       [1.0 - sloepnea[0][1], sloepnea[0][1]],
                                       [1.0 - sloepnea[0][2], sloepnea[0][2]]],
                                      [[1.0 - sloepnea[1][0], sloepnea[1][0]],
                                       [1.0 - sloepnea[1][1], sloepnea[1][1]],
                                       [1.0 - sloepnea[1][2], sloepnea[1][2]]]])