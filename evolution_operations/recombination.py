import numpy as np

from chromosome import Chromosome
from tower import Tower


def whole_arithmatic_crossover(parent1: Chromosome, parent2: Chromosome, P_rec):
    if not np.random.binomial(1, P_rec, 1):
        return Chromosome(parent1.gens), Chromosome(parent2.gens)

    shorter_parent = parent1 if len(parent1.gens) < len(parent2.gens) else parent2
    longer_parent = parent2 if len(parent1.gens) < len(parent2.gens) else parent1
    weight = np.random.uniform(0, 1)

    tower_list1 = []
    for i in range(len(shorter_parent.gens)):
        new_x = weight * shorter_parent.gens[i].x + (1 - weight) * longer_parent.gens[i].x
        new_y = weight * shorter_parent.gens[i].y + (1 - weight) * longer_parent.gens[i].y
        new_bw = weight * shorter_parent.gens[i].bandwidth + (1 - weight) * longer_parent.gens[i].bandwidth
        gen = Tower(new_x, new_y, new_bw)
        tower_list1.append(gen)

    tower_list2 = []
    for i in range(len(shorter_parent.gens)):
        new_x = (1 - weight) * shorter_parent.gens[i].x + weight * longer_parent.gens[i].x
        new_y = (1 - weight) * shorter_parent.gens[i].y + weight * longer_parent.gens[i].y
        new_bw = (1 - weight) * shorter_parent.gens[i].bandwidth + weight * longer_parent.gens[i].bandwidth
        gen = Tower(new_x, new_y, new_bw)
        tower_list2.append(gen)

    for i in range(len(shorter_parent.gens), len(longer_parent.gens)):
        new_x = (1 - weight) * longer_parent.gens[i].x
        new_y = (1 - weight) * longer_parent.gens[i].y
        new_bw = (1 - weight) * longer_parent.gens[i].bandwidth
        gen = Tower(new_x, new_y, new_bw)
        tower_list2.append(gen)

    offspring1 = Chromosome(tower_list1)
    offspring2 = Chromosome(tower_list2)

    return offspring1, offspring2


def one_point_crossover(parent1: Chromosome, parent2: Chromosome, P_rec):
    if not np.random.binomial(1, P_rec, 1) or len(parent1.gens) == 1 or len(parent2.gens) == 1:
        return Chromosome(parent1.gens), Chromosome(parent2.gens)

    if len(parent1.gens) == 1 or len(parent2.gens) == 1:
        return parent1, parent2

    shorter_parent = parent1 if len(parent1.gens) < len(parent2.gens) else parent2
    longer_parent = parent2 if len(parent1.gens) < len(parent2.gens) else parent1

    # Choose a random crossover point
    crossover_point = np.random.randint(1, len(shorter_parent.gens))

    # Create the offspring by copying the first part of the shorter parent
    genes1 = shorter_parent.gens
    genes2 = longer_parent.gens

    tower_list1 = combine(genes1, 0, crossover_point,
                          genes2, crossover_point, len(genes2))

    tower_list2 = combine(genes2, 0, crossover_point,
                          genes1, crossover_point, len(genes1))

    offspring1 = Chromosome(tower_list1)
    offspring2 = Chromosome(tower_list2)

    return offspring1, offspring2


def combine(p1: list, x1, y1, p2: list, x2, y2):
    res = []
    for i in range(x1, y1):
        res.append(p1[i])

    for j in range(x2, y2):
        res.append(p2[j])

    return res
