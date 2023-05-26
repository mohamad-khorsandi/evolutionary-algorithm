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
MAX_TOWER_COUNT = 30
POPULATION_SIZE = 50
MAX_BAND_WIDTH = 150000
ITERATION = 10
PARENT_POOL_SIZE = 24
P_MUT = .9
P_REC = .9
MUT_MOVE_RATE = 2
MUT_CHANGE_BW_RATE = 10000


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

