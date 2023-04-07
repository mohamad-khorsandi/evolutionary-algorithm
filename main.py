from random import randrange, uniform
import globals
from chromosome import Chromosome
from tower import Tower

generation = []


def main():
    globals.init_globals()
    init_generation()
    for i in range(globals.iteration):
        parent_pool = []


def mutation():
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
