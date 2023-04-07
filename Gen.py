from typing import List

from neighborhood import Neighborhood

X = 20
Y = 20


class Gen:

    def __init__(self, x_value, y_value, bandwidth, serve_neighborhood: List[Neighborhood]):
        self.name = id
        self.x_value = x_value
        self.y_value = y_value
        self.bandwidth = bandwidth
        self.serve_neighborhood = serve_neighborhood

    def set(self, x_val, y_val):
        if x_val <= X:
            self.x_value = x_val
        if y_val <= Y:
            self.y_value = y_val
