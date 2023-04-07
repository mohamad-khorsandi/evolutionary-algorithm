import globals


class Tower:
    def __init__(self, x_value, y_value, bandwidth):
        self.name = id
        self.x_value = x_value
        self.y_value = y_value
        self.bandwidth = bandwidth

    def set(self, x_val, y_val):
        if x_val <= globals.city_row:
            self.x_value = x_val
        if y_val <= globals.city_col:
            self.y_value = y_val
