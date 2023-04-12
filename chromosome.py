from cmath import inf
from typing import List
import numpy as np
import globals
from globals import CITY
from tower import Tower
import matplotlib.pyplot as plt


class Chromosome:
    def __init__(self, gens: List[Tower]):
        self.gens = gens
        self.assign_neighborhoods()
        self.__fitness = self.update_fittness()

    def __objective_function(self):
        total_cost_build_towers = 0
        total_satisfactions = 0
        for i in self.gens:
            total_cost_build_towers += i.total_build_cost()
            total_satisfactions += i.satisfaction()

        return total_satisfactions - total_cost_build_towers

    def get_fittness(self):
        return self.__fitness

    def update_fittness(self):
        self.__fitness = self.__objective_function()
        return self.__fitness

    def assign_neighborhoods(self):
        for neigh in CITY:
            min_dist = inf
            min_tower = None
            for tower in self.gens:
                distance = neigh.dis(tower.x_value, tower.y_value)
                if distance < min_dist:
                    min_dist = distance
                    min_tower = tower
            min_tower.serve_neighborhood.append(neigh)

    def plot(self):
        colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
        plt.figure(figsize=(globals.CITY_ROW, globals.CITY_COL))
        for i, tower in enumerate(self.gens):
            plt.scatter(tower.x_value, tower.y_value, marker='>', color=colors[i])
            neigh_points = []

            for n in tower.serve_neighborhood:
                neigh_points.append([n.x, n.y])

            if len(tower.serve_neighborhood) > 0:
                x, y = np.array(neigh_points).T
                plt.scatter(x, y, color=colors[i])

        plt.show()