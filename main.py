from random import randrange, uniform, random
from typing import List

import numpy as np
import pandas as pd

import globals
from chromosome import Chromosome
from neighborhood import Neighborhood
from tower import Tower

generation = []


def main():
    globals.init_globals()
    init_generation()
    for i in range(globals.iteration):
        parent_pool = []


def mutation():
    pass


def whole_arithmetic_crossover(parent1: Chromosome, parent2: Chromosome):
    # Determine the shorter parent
    shorter_parent = parent1 if len(parent1.gens) < len(parent2.gens) else parent2
    longer_parent = parent2 if len(parent1.gens) < len(parent2.gens) else parent1

    # Calculate the crossover rate
    weight = random.uniform(0, 1)

    # Create the first offspring by performing Whole Arithmetic Crossover
    offspring1 = []
    for i in range(len(shorter_parent.gens)):
        new_x = weight * parent1.gens[i].x_value + (1 - weight) * parent2.gens[i].x_value
        new_y = weight * parent1.gens[i].y_value + (1 - weight) * parent2.gens[i].y_value
        new_bw = weight * parent1.gens[i].bandwidth + (1 - weight) * parent2.gens[i].bandwidth
        gen = Tower(new_x, new_y, new_bw)
        offspring1.append(gen)

    # Add any remaining genes from the longer parent to the first offspring
    for i in range(len(shorter_parent.gens), len(longer_parent.gens)):
        new_x = weight * longer_parent.gens[i].x_value
        new_y = weight * longer_parent.gens[i].y_value
        new_bw = weight * longer_parent.gens[i].bandwidth
        gen = Tower(new_x, new_y, new_bw)
        offspring1.append(gen)

    # Create the second offspring by performing Whole Arithmetic Crossover (swapping parents)
    offspring2 = []
    for i in range(len(shorter_parent.gens)):
        new_x = (1 - weight) * parent1.gens[i].x_value + weight * parent2.gens[i].x_value
        new_y = (1 - weight) * parent1.gens[i].y_value + weight * parent2.gens[i].y_value
        new_bw = (1 - weight) * parent1.gens[i].bandwidth + weight * parent2.gens[i].bandwidth
        gen = Tower(new_x, new_y, new_bw)
        offspring2.append(gen)

    # Add any remaining genes from the longer parent to the second offspring
    for i in range(len(shorter_parent.gens), len(longer_parent.gens)):
        new_x = (1 - weight) * longer_parent.gens[i].x_value
        new_y = (1 - weight) * longer_parent.gens[i].y_value
        new_bw = (1 - weight) * longer_parent.gens[i].bandwidth
        gen = Tower(new_x, new_y, new_bw)
        offspring2.append(gen)

    return offspring1, offspring2


def cut_and_crossfill(parent1: Chromosome, parent2: Chromosome):
    shorter_parent = parent1 if len(parent1.gens) < len(parent2.gens) else parent2
    longer_parent = parent2 if len(parent1.gens) < len(parent2.gens) else parent1

    # Choose a random crossover point
    crossover_point = random.randint(1, len(shorter_parent.gens) - 1)

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
            if longer_parent.gens[i].x_value == g.x_value and longer_parent.gens[i].y_value == g.y_value:
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
            if longer_parent.gens[i].x_value == g.x_value and longer_parent.gens[i].y_value == g.y_value:
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


def assign_neighborhood_to_toweer(city: List[Neighborhood], centroids: List[Tower]):
    diff = 1
    # Store the cluster number of each digit in this array
    region = np.zeros(len(city))

    while diff:
        # for each observation
        for i, neigh in enumerate(city):
            mn_dist = float('inf')
            # dist of the point from all centroids
            for idx, centroid in enumerate(centroids):
                distance = np.sqrt(((centroid.x_value - neigh.x) ** 2) + ((centroid.y_value - neigh.y) ** 2))
                # store closest centroid
                if mn_dist > distance:
                    mn_dist = distance
                region[i] = idx

            new_centroids = pd.DataFrame(city).groupby(by=region).mean().values

            # if centroids are same then leave
            if np.count_nonzero(centroids - new_centroids) == 0:
                diff = 0
            else:
                centroids = new_centroids

    return centroids, region


def recombination():
    pass


def init_generation():
    global generation

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


if __name__ == '__main__':
    main()
