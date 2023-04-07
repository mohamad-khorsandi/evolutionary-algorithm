from typing import List
from tower import Tower


class Chromosome:

    def __init__(self, gens: List[Tower]):
        self.gens = gens

    def objective_function(self):
        total_cost_build_towers = 0
        total_satisfactions = 0
        for i in self.gens:
            total_cost_build_towers += i.total_build_cost()
            total_satisfactions += i.satisfaction()

        return total_satisfactions - total_cost_build_towers
