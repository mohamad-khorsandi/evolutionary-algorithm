from typing import List
from tower import Tower


class Chromosome:

    def __init__(self, gens: List[Tower]):
        self.gens = gens
        self.__fitness = None

    def __objective_function(self):
        total_cost_build_towers = 0
        total_satisfactions = 0
        for i in self.gens:
            total_cost_build_towers += i.total_build_cost()
            total_satisfactions += i.satisfaction()

        return total_satisfactions - total_cost_build_towers

    def get_fittness(self):
        if self.__fitness is None:
            self.__fitness = self.__objective_function()

        return self.__fitness
