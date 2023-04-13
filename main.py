from random import randrange, uniform, choices

import matplotlib.pyplot as plt

import globals
from chromosome import Chromosome
from globals import *
from tower import Tower


def main():
    init_globals()
    population = gen_rand_population()
    fittness_hist = []
    for _ in range(globals.ITERATION):
        fittness_hist.append(np.mean([c.get_fittness() for c in population]))
        parent_pool = select_parent(population, PARENT_POOL_SIZE)
        children = []
        for i in range(0, PARENT_POOL_SIZE - 1, 2):
            p1, p2 = parent_pool[i], parent_pool[i + 1]
            for c in recombination(p1, p2, globals.P_REC):
                mutation(c, globals.P_MUT)
                children.append(c)
        replace_children(population, children)

    plt.plot(range(globals.ITERATION), fittness_hist)
    plt.show()


def replace_children(population: list, children):
    for _ in range(len(children)):
        prob_list = get_weight_list(population, reverse=True)
        idx_tobe_removed = choices(range(len(population)), prob_list)[0]
        del population[idx_tobe_removed]

    population.extend(children)


def select_parent(generation, count):
    prob_list = get_weight_list(generation)
    return choices(generation, prob_list, k=count)


def get_weight_list(chromosome_list: list, reverse=False):
    fittness_list = [c.get_fittness() for c in chromosome_list]
    min_fittness = min(fittness_list)
    if min_fittness < 0:
        fittness_list = [fittness - min_fittness for fittness in fittness_list]

    fittness_sum = sum(fittness_list)
    weight_list = [p / fittness_sum for p in fittness_list]

    assert any([0 <= p <= 1 for p in weight_list])
    if reverse:
        return [1 - p for p in weight_list]
    else:
        return weight_list


def mutation(chromosome, P_mut):
    for gene in chromosome.gens:
        if np.random.binomial(1, P_mut, 1):
            gene.set_xANDyANDbw(np.random.normal(scale=CONVERGE_RATE),
                                np.random.normal(scale=CONVERGE_RATE),
                                np.random.normal(loc=0, scale=CONVERGE_RATE))

    chromosome.assign_neigh_to_towers()
    chromosome.update_fittness()
    return chromosome


def recombination(parent1: Chromosome, parent2: Chromosome, P_rec):
    if not np.random.binomial(1, P_rec, 1):
        return parent1, parent2

    # Determine the shorter parent
    shorter_parent = parent1 if len(parent1.gens) < len(parent2.gens) else parent2
    longer_parent = parent2 if len(parent1.gens) < len(parent2.gens) else parent1

    # Calculate the crossover rate
    weight = np.random.uniform(0, 1)

    # Create the first offspring by performing Whole Arithmetic Crossover
    tower_list1 = []
    for i in range(len(shorter_parent.gens)):
        new_x = weight * parent1.gens[i].x + (1 - weight) * parent2.gens[i].x
        new_y = weight * parent1.gens[i].y + (1 - weight) * parent2.gens[i].y
        new_bw = weight * parent1.gens[i].bandwidth + (1 - weight) * parent2.gens[i].bandwidth
        gen = Tower(new_x, new_y, new_bw)
        tower_list1.append(gen)

    # Add any remaining genes from the longer parent to the first offspring
    for i in range(len(shorter_parent.gens), len(longer_parent.gens)):
        new_x = weight * longer_parent.gens[i].x
        new_y = weight * longer_parent.gens[i].y
        new_bw = weight * longer_parent.gens[i].bandwidth
        gen = Tower(new_x, new_y, new_bw)
        tower_list1.append(gen)

    # Create the second offspring by performing Whole Arithmetic Crossover (swapping parents)
    tower_list2 = []
    for i in range(len(shorter_parent.gens)):
        new_x = (1 - weight) * parent1.gens[i].x + weight * parent2.gens[i].x
        new_y = (1 - weight) * parent1.gens[i].y + weight * parent2.gens[i].y
        new_bw = (1 - weight) * parent1.gens[i].bandwidth + weight * parent2.gens[i].bandwidth
        gen = Tower(new_x, new_y, new_bw)
        tower_list2.append(gen)

    # Add any remaining genes from the longer parent to the second offspring
    for i in range(len(shorter_parent.gens), len(longer_parent.gens)):
        new_x = (1 - weight) * longer_parent.gens[i].x
        new_y = (1 - weight) * longer_parent.gens[i].y
        new_bw = (1 - weight) * longer_parent.gens[i].bandwidth
        gen = Tower(new_x, new_y, new_bw)
        tower_list2.append(gen)
    offspring1 = Chromosome(tower_list1)
    offspring2 = Chromosome(tower_list2)
    offspring1.assign_neigh_to_towers()
    offspring2.assign_neigh_to_towers()
    return offspring1, offspring2


def cut_and_crossfill(parent1: Chromosome, parent2: Chromosome):
    shorter_parent = parent1 if len(parent1.gens) < len(parent2.gens) else parent2
    longer_parent = parent2 if len(parent1.gens) < len(parent2.gens) else parent1

    # Choose a random crossover point
    crossover_point = np.random.randint(1, len(shorter_parent.gens) - 1)

    # Create the offspring by copying the first part of the shorter parent
    offspring1 = shorter_parent.gens[:crossover_point]

    offspring2 = longer_parent.gens[:crossover_point]

    # Fill in the second part of the offspring with values from the longer parent that are not already in the offspring
    start = crossover_point
    end = len(longer_parent.gens)
    repeat = 0
    for i in range(start, end):
        find = 0
        for g in offspring1:
            if longer_parent.gens[i].x == g.x and longer_parent.gens[i].y == g.y:
                find = 1
                break
        if find == 0:
            if repeat == 0:
                offspring1.append(longer_parent.gens[i])
        if repeat == 0 and i == end - 1:
            repeat = 1
            start = 0
            end = crossover_point

    start = crossover_point
    end = len(shorter_parent.gens)
    repeat = 0
    for i in range(start, end):
        find = 0
        for g in offspring2:
            if longer_parent.gens[i].x == g.x and longer_parent.gens[i].y == g.y:
                find = 1
                break
        if find == 0:
            if repeat == 0:
                offspring2.append(shorter_parent.gens[i])
        if repeat == 0 and i == end - 1:
            repeat = 1
            start = 0
            end = crossover_point

    return offspring1, offspring2


def gen_rand_population():
    generation = []
    for _ in range(globals.POPULATION_SIZE):
        tower_count = randrange(1, globals.MAX_TOWER_COUNT + 1)
        tower_list = []
        for _ in range(tower_count):
            x = uniform(0, globals.CITY_ROW - 1)
            y = uniform(0, globals.CITY_COL - 1)
            band_width = uniform(1, globals.MAX_BAND_WIDTH)
            tower_list.append(Tower(x, y, band_width))
        tmp_crm = Chromosome(tower_list)
        generation.append(tmp_crm)
    return generation


if __name__ == '__main__':
    main()
