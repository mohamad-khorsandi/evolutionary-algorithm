import os
import random
import time
from random import randrange, uniform
import matplotlib.pyplot as plt
import numpy as np
import constants
from chromosome import Chromosome
from evolution_operations.mutation import mutation
from evolution_operations.parent_selection import select_parent
from evolution_operations.recombination import whole_arithmatic_crossover
from tower import Tower
from neighborhood import make_city_list
import shutil

fittness_hist = []
best_hist = []
res_dir = "res"


def init():
    assert constants.PARENT_POOL_SIZE <= constants.POPULATION_SIZE
    assert constants.PARENT_POOL_SIZE % 2 == 0
    constants.__read_config()
    make_city_list()

    dir_exists = os.path.exists(res_dir)
    if dir_exists:
        shutil.rmtree(res_dir)

    os.mkdir(res_dir)


def main():
    start = time.time()
    init()
    population = gen_rand_population()
    for i in range(constants.ITERATION):
        parent_pool = select_parent(population, constants.PARENT_POOL_SIZE)
        recode_statistics(population, i)
        children = []
        print(i)
        for j in range(0, constants.PARENT_POOL_SIZE - 1, 2):
            p1, p2 = parent_pool[j], parent_pool[j + 1]
            for c in whole_arithmatic_crossover(p1, p2, constants.P_REC):
                c1 = mutation(c, constants.P_MUT)
                children.append(c1)
        replace_children(population, children)

    end = time.time()
    best_hist[constants.ITERATION - 1].gens_changed()
    best_hist[constants.ITERATION - 1].get_fittness()
    show_statistics(end - start)


def recode_statistics(population: list[Chromosome], iteration: int):
    all_fittness = np.array([c.get_fittness() for c in population])
    fittness_hist.append(np.mean(all_fittness))
    best_hist.append(population[all_fittness.argmax()])
    # population[all_fittness.argmax()].save_plot(res_dir + '/' + str(iteration) + '.png')


def show_statistics(time):
    print("total time of running algorithm: " + str(time))
    plt.clf()
    plt.plot(range(constants.ITERATION), fittness_hist, color='b')
    plt.plot(range(constants.ITERATION), [c.get_fittness() for c in best_hist], color='r')
    plt.savefig(res_dir + '/' + 'total.png')
    print_best_solution()
    best_hist[constants.ITERATION - 1].save_plot(res_dir + '/best.png')


def print_best_solution():
    print('* Best solution:')
    best_solution = best_hist[constants.ITERATION - 1]
    print(f"* Fitness: {best_solution.get_fittness()}")
    print(f"* Number of tower: {len(best_solution.gens)}")
    print("* Information of towers:")
    for i, t in enumerate(best_solution.gens):
        print(f"Tower {i}:")
        print(f"Coordinate: ({t.x}, {t.y}) | Bandwidth: {t.bandwidth} | Building cost: {t.total_build_cost()}")
        print('- The Neighborhood that tower supports them:')
        for n in t.serve_neighborhood:
            print(f"coordinate: ({n.x},{n.y}) | population: {n.population} | satisfaction:{n.satisfaction(t)}", end=" ")
        print()
        print("------------------------------------------------------")


def replace_children(population: list, children):
    for c in children:
        c.gens_changed()

    fittness_list = np.array([c.get_fittness() for c in population])
    assert np.count_nonzero([c.is_gens_changed() for c in population]) == 0
    k_smallest_idx = np.argpartition(fittness_list, len(children))
    for i in range(len(children)):
        population[k_smallest_idx[i]] = children[i]


def gen_rand_population():
    random.seed(42)
    generation = []
    for _ in range(constants.POPULATION_SIZE):
        tower_count = randrange(1, constants.MAX_TOWER_COUNT + 1)
        tower_list = []
        for _ in range(tower_count):
            x = uniform(0, constants.CITY_ROW - 1)
            y = uniform(0, constants.CITY_COL - 1)
            band_width = uniform(1, constants.MAX_BAND_WIDTH)
            tower_list.append(Tower(x, y, band_width))
        tmp_crm = Chromosome(tower_list)
        generation.append(tmp_crm)
    return generation


if __name__ == '__main__':
    main()
