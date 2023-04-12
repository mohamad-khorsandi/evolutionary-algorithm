import globals


class Tower:
    def __init__(self, x_value, y_value, bandwidth):
        self.x_value = x_value
        self.y_value = y_value
        self.bandwidth = bandwidth
        self.serve_neighborhood = []

    def set(self, x_val, y_val, band_width):
        if x_val <= globals.CITY_ROW:
            self.x_value = x_val

        if y_val <= globals.CITY_COL:
            self.y_value = y_val

        if 0 < band_width < globals.MAX_BAND_WIDTH:
            self.bandwidth = band_width

    def total_build_cost(self):
        return globals.TOWER_CONSTRUCTION_COST + (self.bandwidth * globals.TOWER_MAINTENANCE_COST)

    def satisfaction(self):
        total_satisfaction_score = 0
        for neigh in self.serve_neighborhood:
            total_satisfaction_score += neigh.satisfaction(self)

        return total_satisfaction_score

    def obj_func(self):
        return self.satisfaction() - self.total_build_cost()  # todo change to / to prevent neg obj

    def set_xANDyANDbw(self, rand1, rand2, rand3):
        x_val = self.x_value + rand1
        y_val = self.y_value + rand2
        band_width = self.bandwidth + rand3
        self.set(x_val, y_val, band_width)
        return self
