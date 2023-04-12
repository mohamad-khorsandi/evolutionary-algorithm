import globals


class Tower:
    def __init__(self, x_value, y_value, bandwidth):
        self.name = id
        self.x_value = x_value
        self.y_value = y_value
        self.bandwidth = bandwidth
        self.serve_neighborhood = None

    def set(self, x_val, y_val):
        if x_val <= globals.city_row:
            self.x_value = x_val
        if y_val <= globals.city_col:
            self.y_value = y_val

    def total_build_cost(self):
        return globals.tower_construction_cost + (self.bandwidth * globals.tower_maintanance_cost)

    def satisfaction(self):
        total_satisfaction_score = 0
        for neigh in self.serve_neighborhood:
            total_satisfaction_score += neigh.satisfaction(self)

        return total_satisfaction_score

    def obj_func(self):
        return self.satisfaction() - self.total_build_cost()

    def set_xANDyANDbw(self, rand1, rand2, rand3):
        x_val = self.x_value + rand1
        y_val = self.y_value + rand2
        band_width = self.bandwidth + rand3
        self.set(self, x_val, y_val, band_width)
        return self
