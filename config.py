import json

tower_construction_cost = None
tower_maintanance_cost = None
user_satisfaction_levels = []
user_satisfaction_scores = []


def read_config():
    with open('problem_config.json') as user_file:
        file_contents = user_file.read()

    print(file_contents)

    parsed_json = json.loads(file_contents)
    global tower_construction_cost
    global tower_maintanance_cost
    global user_satisfaction_levels
    global user_satisfaction_scores

    tower_construction_cost = parsed_json['tower_construction_cost']
    tower_maintanance_cost = parsed_json['tower_maintanance_cost']
    user_satisfaction_levels = parsed_json['user_satisfaction_levels']
    user_satisfaction_scores = parsed_json['user_satisfaction_scores']