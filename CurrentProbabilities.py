
class CurrentProbabilities:
    # sloepnea, foriennditis, degarspots, trimo_gene, dunetts
    class __CurrentProbabilities:
        def __init__(self, foriennditis=None, sloepnea=None, degarspots=None, gene=None, dunetts=None):
            self.sloepnea = sloepnea
            self.foriennditis = foriennditis
            self.degarspots = degarspots
            self.gene = gene
            self.dunetts = dunetts

        def __str__(self):
            return " S: " + str(self.sloepnea)+ "F: " + str(self.foriennditis) + "DS: " + str(self.degarspots) + " G: " + str(self.gene) + " D: " + str(self.dunetts)

    instance = None

    def __init__(self, sloepnea=None, foriennditis=None, degarspots=None, gene=None, dunetts=None):
        if not CurrentProbabilities.instance:
            CurrentProbabilities.instance = CurrentProbabilities.__CurrentProbabilities(sloepnea,
                                                                                        foriennditis,
                                                                                        degarspots,
                                                                                        gene,
                                                                                        dunetts)
        else:
            CurrentProbabilities.instance.val = foriennditis, sloepnea, degarspots, gene, dunetts

    def __getattr__(self, name):
        return getattr(self.instance, name)
