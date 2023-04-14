import constants


class Tower:
    def __init__(self, x_value: float, y_value: float, bandwidth: float):
        self.x = None
        self.y = None
        self.bandwidth = None
        self.set_x(x_value)
        self.set_y(y_value)
        self.set_bw(bandwidth)
        self.serve_neighborhood = []

    def set_x(self, x_val):
        if 0 <= x_val <= constants.CITY_ROW - 1:
            self.x = x_val

        elif x_val < 0:
            self.x = 0

        elif x_val > constants.CITY_ROW - 1:
            self.x = constants.CITY_ROW - 1

    def set_y(self, y_val):
        if 0 <= y_val <= constants.CITY_COL - 1:
            self.y = y_val
        elif y_val < 0:
            self.y = 0
        elif y_val > constants.CITY_COL - 1:
            self.y = constants.CITY_COL - 1

    def set_bw(self, bw):
        if 0 <= bw <= constants.MAX_BAND_WIDTH:
            self.bandwidth = bw
        elif bw < 0:
            self.bandwidth = 0
        elif bw > constants.MAX_BAND_WIDTH:
            self.bandwidth = constants.MAX_BAND_WIDTH

    def total_build_cost(self):
        return constants.TOWER_CONSTRUCTION_COST + (self.bandwidth * constants.TOWER_MAINTENANCE_COST)

    def satisfaction(self):
        total_satisfaction_score = 0
        for neigh in self.serve_neighborhood:
            total_satisfaction_score += neigh.satisfaction(self)

        return total_satisfaction_score

    def obj_func(self):
        return self.satisfaction() - self.total_build_cost()
