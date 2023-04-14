import json

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
MAX_TOWER_COUNT = 25  # 25
POPULATION_SIZE = 50  # 50
MAX_BAND_WIDTH = 6000000  # 15000
ITERATION = 10
PARENT_POOL_SIZE = 24
P_MUT = 1
P_REC = 0
MUT_MOVE_RATE = 10  # todo
MUT_CHANGE_BW_RATE = 3000000


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




#todo

# def __calculate_max_bw():
#     global MAX_BAND_WIDTH
#     global MAX_NEIGH_POPULATION
#     avg_pop = np.mean([c.population for c in CITY])
#     MAX_BAND_WIDTH = USER_SATISFACTION_SCORES[2] * avg_pop * len(CITY) - TOWER_CONSTRUCTION_COST
