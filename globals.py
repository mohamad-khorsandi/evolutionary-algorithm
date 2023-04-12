import csv
import json
import numpy as np
from neighborhood import Neighborhood

tower_construction_cost = None
tower_maintenance_cost = None
user_satisfaction_levels = None
user_satisfaction_scores = None
population = None
city_row = None
city_col = None
neighborhood_list = []
max_tower_count = 25
generation_size = 400
max_band_width = 1000
iteration = 200
parent_pool_size = 50

def init_globals():
    assert parent_pool_size <= generation_size
    __read_config()
    __make_city_list()

def __read_config():
    with open('problem_config.json') as user_file:
        file_contents = user_file.read()

    print(file_contents)

    parsed_json = json.loads(file_contents)
    global tower_construction_cost
    global tower_maintenance_cost
    global user_satisfaction_levels
    global user_satisfaction_scores

    tower_construction_cost = parsed_json['tower_construction_cost']
    tower_maintenance_cost = parsed_json['tower_maintanance_cost']
    user_satisfaction_levels = parsed_json['user_satisfaction_levels']
    user_satisfaction_scores = parsed_json['user_satisfaction_scores']


def __make_city_list():
    global city_row
    global city_col
    global neighborhood_list

    with open('blocks_population.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        population = np.array(list(csv_reader)).astype(float)
    city_row = population.shape[0]
    city_col = population.shape[1]

    for i in range(city_row):
        for j in range(city_col):
            tmp_nbr = Neighborhood(i, j, population[i][j])
            neighborhood_list.append(tmp_nbr)
