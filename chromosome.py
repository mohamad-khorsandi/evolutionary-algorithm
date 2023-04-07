from typing import List
from tower import Tower


class Chromosome:

    def __init__(self, towers: List[Tower]):
        self.chromosome = towers
