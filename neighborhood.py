import numpy as np
from numpy.linalg import inv
from objective_utilities import user_bandwidth
from tower import Tower
from globals import *


class Neighborhood:
    def __init__(self, x, y, population):
        self.x = x
        self.y = y
        self.population = population  # Todo

    def neigh_satisfaction(self, tower: Tower):
        return self.population * user_bandwidth(self.population, tower.bandwidth)

    def neigh_nominal_bandwidth(self, tower: Tower):
        total_population = 0
        for neigh in tower.serve_neighborhood:
            total_population += neigh.population

        neigh_nominal_BW = (self.population * tower.bandwidth) / total_population
        return neigh_nominal_BW

    def neigh_actual_bandwidth(self, tower: Tower):
        neigh_v = np.array([self.x, self.y])
        tower_v = np.array([tower.x, tower.y])
        matrix = np.array([[8., 0.], [0., 8.]])
        temp = -0.5 * np.matmul(np.matmul((neigh_v - tower_v), inv(matrix)), np.transpose(neigh_v - tower_v))
        cov = np.exp(temp)
        actual_bandwidth = cov * self.neigh_nominal_bandwidth(tower)
        return actual_bandwidth

    def satisfaction(self, tower: Tower):
        satisfaction_score = 0
        user_bw = user_bandwidth(self.population, self.neigh_actual_bandwidth(tower))
        if user_bw < USER_SATISFACTION_LEVELS[0]:
            satisfaction_score = 0

        elif USER_SATISFACTION_LEVELS[0] <= user_bw <= USER_SATISFACTION_LEVELS[1]:
            satisfaction_score = USER_SATISFACTION_SCORES[0]

        elif USER_SATISFACTION_LEVELS[1] <= user_bw < USER_SATISFACTION_LEVELS[2]:
            satisfaction_score = USER_SATISFACTION_SCORES[1]

        elif user_bw >= USER_SATISFACTION_LEVELS[2]:
            satisfaction_score = USER_SATISFACTION_SCORES[2]

        return satisfaction_score * self.population

    def dis(self, x, y):
        return np.sqrt(((self.x - x) ** 2) + ((self.y - y) ** 2))


