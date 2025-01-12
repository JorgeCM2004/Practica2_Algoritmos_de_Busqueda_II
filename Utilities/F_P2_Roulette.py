import random as rn
from Utilities.F_P2_Colony import P2_Colony as Colony

class P2_Roulette:
    def spin(self, nodes: list[Colony], probabilities: list[float]) -> Colony:
        rnd = rn.random()
        for i in range(len(probabilities)):
            rnd -= probabilities[i]
            if rnd <= 0:
                return nodes[i]
        return nodes[-1]
