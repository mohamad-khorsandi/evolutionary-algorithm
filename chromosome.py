from cmath import inf
from typing import List

import matplotlib.pyplot as plt
import numpy as np

import globals
from globals import CITY
from tower import Tower


class Chromosome:
    def __init__(self, gens: List[Tower]):
        self.gens = gens
        self.__fitness = float()
        self.assign_neigh_to_towers()
        self.update_fittness()

    def __objective_function(self):
        total_cost_build_towers = 0
        total_satisfactions = 0
        for tower in self.gens:
            total_cost_build_towers += tower.total_build_cost()
            total_satisfactions += tower.satisfaction()

        return total_satisfactions - total_cost_build_towers

    def get_fittness(self):
        return self.__fitness

    def update_fittness(self):
        self.__fitness = self.__objective_function()

    def assign_neigh_to_towers(self):
        for neigh in CITY:
            min_dist = inf
            min_tower = None
            for tower in self.gens:
                distance = neigh.dis(tower.x, tower.y)
                if distance < min_dist:
                    min_dist = distance
                    min_tower = tower
            min_tower.serve_neighborhood.append(neigh)

    def plot(self):
        colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
        plt.figure(figsize=(globals.CITY_ROW, globals.CITY_COL))
        for i, tower in enumerate(self.gens):
            plt.scatter(tower.x, tower.y, marker='>', color=colors[i])
            neigh_points = []

            for n in tower.serve_neighborhood:
                neigh_points.append([n.x, n.y])

            if len(tower.serve_neighborhood) > 0:
                x, y = np.array(neigh_points).T
                plt.scatter(x, y, color=colors[i])

        plt.show()

    def clone(self, gens: List[Tower]):
        new_chromosome = Chromosome(gens)
        return new_chromosome
