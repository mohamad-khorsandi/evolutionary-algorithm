import numpy as np

import constants
from chromosome import Chromosome
from tower import Tower


def mutation(chromosome, P_mut):
    tower_list = []
    for gene in chromosome.gens:
        if np.random.binomial(1, P_mut, 1):
            g = Tower(gene.x + np.random.normal(scale=constants.MUT_MOVE_RATE), gene.y + np.random.normal(scale=constants.MUT_MOVE_RATE),
                      gene.bandwidth + np.random.normal(loc=0, scale=constants.MUT_CHANGE_BW_RATE))
        else:
            g = Tower(gene.x, gene.y, gene.bandwidth)
        tower_list.append(g)
    return Chromosome(tower_list)