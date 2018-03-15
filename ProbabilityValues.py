
class ProbabilityValues:
    # sloepnea, foriennditis, degarspots, trimo_gene, dunetts


    # Normal Constructor
    def __init__(self, key, sloepnea=None, foriennditis=None, degarspots=None, gene=None, dunetts=None):
        self.key = key
        self.sloepnea = sloepnea
        self.foriennditis = foriennditis
        self.degarspots = degarspots
        self.gene = gene
        self.dunetts = dunetts

    def __str__(self):
        return "key:" + str(self.key)
