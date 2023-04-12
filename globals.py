import csv
import json
import numpy as np
from neighborhood import Neighborhood

# problem config
TOWER_CONSTRUCTION_COST = None
TOWER_MAINTENANCE_COST = None
USER_SATISFACTION_LEVELS = None
USER_SATISFACTION_SCORES = None
CITY_ROW = None
CITY_COL = None
CITY = []

# hyper parameters
MAX_TOWER_COUNT = 5
POPULATION_SIZE = 10
MAX_BAND_WIDTH = 1000# todo
ITERATION = 10
PARENT_POOL_SIZE = 3
P_MUT = 1
P_REC = 1


def init_globals():
    assert PARENT_POOL_SIZE <= POPULATION_SIZE
    __read_config()
    __make_city_list()

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

    with open('pop2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        population = np.array(list(csv_reader)).astype(float)
    CITY_ROW = population.shape[0]
    CITY_COL = population.shape[1]

    for i in range(CITY_ROW):
        for j in range(CITY_COL):
            tmp_nbr = Neighborhood(i, j, population[i][j])
            CITY.append(tmp_nbr)
