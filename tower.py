import globals


class Tower:
    def __init__(self, x_value, y_value, bandwidth):
        self.name = id
        self.x_value = x_value
        self.y_value = y_value
        self.bandwidth = bandwidth
        self.serve_neighborhood = None

    def set(self, x_val, y_val):
        if x_val <= globals.CITY_ROW:
            self.x_value = x_val
        if y_val <= globals.CITY_COL:
            self.y_value = y_val

    def total_build_cost(self):
        return globals.TOWER_CONSTRUCTION_COST + (self.bandwidth * globals.tower_maintanance_cost)

    def satisfaction(self):
        total_satisfaction_score = 0
        for neigh in self.serve_neighborhood:
            total_satisfaction_score += neigh.satisfaction(self)

        return total_satisfaction_score  # todo mul by number of people

    def obj_func(self):
        return self.satisfaction() - self.total_build_cost()  # todo change to / to prevent neg obj
