import csv
import json

import numpy as np

from neighborhood import Neighborhood

# problem config
TOWER_CONSTRUCTION_COST = None
TOWER_MAINTENANCE_COST = None
USER_SATISFACTION_LEVELS = None
USER_SATISFACTION_SCORES = []
CITY_ROW = None
CITY_COL = None
CITY = []
MAX_NEIGH_POPULATION = None

# hyper parameters
MAX_TOWER_COUNT = 40  # 25
POPULATION_SIZE = 50  # 50
MAX_BAND_WIDTH = None  # 15000
ITERATION = 50
PARENT_POOL_SIZE = 25
P_MUT = .1
P_REC = .9
MUT_MOVE_RATE = 10  # todo
MUT_CHANGE_BW_RATE = 10


def init_globals():
    assert PARENT_POOL_SIZE <= POPULATION_SIZE
    __read_config()
    __make_city_list()
    __calculate_max_bw()


def __read_config():
    with open('problem_config.json') as user_file:
        file_contents = user_file.read()

    parsed_json = json.loads(file_contents)
    global TOWER_CONSTRUCTION_COST
    global TOWER_MAINTENANCE_COST
    global USER_SATISFACTION_LEVELS
    global USER_SATISFACTION_SCORES

    TOWER_CONSTRUCTION_COST = parsed_json['tower_construction_cost']
    TOWER_MAINTENANCE_COST = parsed_json['tower_maintanance_cost']
    USER_SATISFACTION_LEVELS = parsed_json['user_satisfaction_levels']
    USER_SATISFACTION_SCORES = parsed_json['user_satisfaction_scores']


def __make_city_list():
    global CITY_ROW
    global CITY_COL
    global CITY
    global MAX_NEIGH_POPULATION

    with open('blocks_population.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        population = np.array(list(csv_reader)).astype(float)
    CITY_ROW = population.shape[0]
    CITY_COL = population.shape[1]

    for i in range(CITY_ROW):
        for j in range(CITY_COL):
            tmp_nbr = Neighborhood(i, j, population[i][j])
            CITY.append(tmp_nbr)

    MAX_NEIGH_POPULATION = max([c.population for c in CITY])


def __calculate_max_bw():
    global MAX_BAND_WIDTH
    global MAX_NEIGH_POPULATION

    avg_pop = np.mean([c.population for c in CITY])
    MAX_BAND_WIDTH = USER_SATISFACTION_SCORES[2] * avg_pop * len(CITY) - TOWER_CONSTRUCTION_COST
    print(MAX_BAND_WIDTH)
