from typing import List

from Gen import Gen


class Chromosome:
    chromosome = [Gen]

    def __init__(self, gens : List[Gen]):
        self.chromosome = gens

    # def objective_function:
