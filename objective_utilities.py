from neighborhood import Neighborhood
from tower import Tower
import numpy as np
from numpy.linalg import inv


def user_bandwidth(neigh_population, tower_bandwidth):
    user_BW = tower_bandwidth / neigh_population
    return user_BW


def neigh_nominal_bandwidth(neigh: Neighborhood, tower: Tower):
    total_population = 0
    for neigh in tower.serve_neighborhood:
        total_population += neigh.population

    neigh_nominal_BW = (neigh.population * tower.bandwidth) / total_population
    return neigh_nominal_BW


def neigh_actual_bandwidth(neigh: Neighborhood, tower: Tower, neigh_nominal_bandwidth):
    neigh_v = np.array([neigh.x, neigh.y])
    tower_v = np.array([tower.x_value, tower.y_value])
    matrix = np.array([[0., 8.], [8., 0.]])
    temp = -0.5 * np.matmul((neigh_v - tower_v), inv(matrix), np.transpose(neigh_v - tower_v))
    cov = np.exp(temp)
    actual_bandwidth = cov * neigh_nominal_bandwidth
    return actual_bandwidth

