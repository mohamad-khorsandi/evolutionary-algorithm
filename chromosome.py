from cmath import inf
from typing import List
import matplotlib.pyplot as plt
import numpy as np
import constants
from constants import CITY
from tower import Tower


class Chromosome:
    def __init__(self, gens: List[Tower]):
        self.gens = gens
        self.__fitness = float()
        self.need_update = True

    def __objective_function(self):
        total_cost_build_towers = 0.0
        total_satisfactions = 0.0
        for tower in self.gens:
            total_cost_build_towers += tower.total_build_cost()
            total_satisfactions += tower.satisfaction()

        assert (total_satisfactions - total_cost_build_towers) != 0

        return total_satisfactions - total_cost_build_towers

    def get_fittness(self):
        if self.need_update:
            for n in self.gens:
                n.serve_neighborhood = []
            self.assign_neigh_to_towers()
            self.__fitness = self.__objective_function()
            self.need_update = False
        return self.__fitness

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
        colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k'] * len(self.gens) #todo
        plt.figure(figsize=(constants.CITY_ROW, constants.CITY_COL))
        for i, tower in enumerate(self.gens):
            plt.scatter(tower.x, tower.y, marker='>', color=colors[i])
            neigh_points = []

            for n in tower.serve_neighborhood:
                neigh_points.append([n.x, n.y])

            if len(tower.serve_neighborhood) > 0:
                x, y = np.array(neigh_points).T
                plt.scatter(x, y, color=colors[i])
        plt.show()

    def save_plot(self, name: str):
        plt.clf()
        colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k'] * len(self.gens) #todo
        plt.figure(figsize=(constants.CITY_ROW, constants.CITY_COL))
        for i, tower in enumerate(self.gens):
            plt.scatter(tower.x, tower.y, marker='>', color=colors[i])
            neigh_points = []

            for n in tower.serve_neighborhood:
                neigh_points.append([n.x, n.y])

            if len(tower.serve_neighborhood) > 0:
                x, y = np.array(neigh_points).T
                plt.scatter(x, y, color=colors[i])

        plt.savefig(name)

    def gens_changed(self):
        self.need_update = True

    def is_gens_changed(self):
        return self.need_update
