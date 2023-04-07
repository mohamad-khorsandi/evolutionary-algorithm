from typing import List
import globals
from neighborhood import Neighborhood


class Tower:

    def __init__(self, x_value, y_value, bandwidth, serve_neighborhood: List[Neighborhood]):
        self.name = id
        self.x_value = x_value
        self.y_value = y_value
        self.bandwidth = bandwidth
        self.serve_neighborhood = serve_neighborhood

    def set(self, x_val, y_val):
        if x_val <= globals.city_row:
            self.x_value = x_val
        if y_val <= globals.city_col:
            self.y_value = y_val
