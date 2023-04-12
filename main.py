from random import randrange, uniform, choices
from globals import *
from chromosome import Chromosome
from tower import Tower


def main():
    init_globals()
    generation = get_rand_generation()
    for i in range(ITERATION):
        parent_pool = select_parent(generation, PARENT_POOL_SIZE)
        remove_offspring(generation, PARENT_POOL_SIZE)


def remove_offspring(generation: list, count):
    prob_list = get_weight_list(generation, reverse=True)
    offspring = choices(generation, prob_list, k=count)
    for chromosome in offspring:
        generation.remove(chromosome)


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


def get_rand_generation():
    generation = []
    for _ in range(globals.generation_size):
        tower_count = randrange(1, globals.max_tower_count + 1)
        tower_list = []
        for _ in range(tower_count):
            x = uniform(0, globals.city_row)
            y = uniform(0, globals.city_col)
            band_width = uniform(1, globals.max_band_width)
            tower_list.append(Tower(x, y, band_width))
        tmp_crm = Chromosome(tower_list)
        generation.append(tmp_crm)
    return generation


if __name__ == '__main__':
    main()
