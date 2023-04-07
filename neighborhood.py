from objective_utilities import user_bandwidth
from tower import Tower
import numpy as np
from numpy.linalg import inv


class Neighborhood:
    def __init__(self, x, y, population):
        self.x = x
        self.y = y
        self.population = population
        self.bandwidth = None

    def neigh_satisfaction(self, tower: Tower):
        return self.population * user_bandwidth(self.population, tower.bandwidth)

    def neigh_nominal_bandwidth(self, tower: Tower):
        total_population = 0
        for neigh in tower.serve_neighborhood:
            total_population += neigh.population

        neigh_nominal_BW = (neigh.population * tower.bandwidth) / total_population
        return neigh_nominal_BW

    def neigh_actual_bandwidth(self, tower: Tower):
        neigh_v = np.array([self.x, self.y])
        tower_v = np.array([tower.x_value, tower.y_value])
        matrix = np.array([[8., 0.], [0., 8.]])
        temp = -0.5 * np.matmul(np.matmul((neigh_v - tower_v), inv(matrix)), np.transpose(neigh_v - tower_v))
        cov = np.exp(temp)
        actual_bandwidth = cov * self.neigh_nominal_bandwidth(tower)
        return actual_bandwidth

    def satisfaction(self, tower: Tower):
        satisfaction_score = 0
        user_bw = user_bandwidth(self.population, self.neigh_actual_bandwidth(tower))
        if user_bw < 0.2:
            satisfaction_score = 0
        elif 0.2 <= user_bw <= 1:
            satisfaction_score = 10
        elif 1 <= user_bw < 3:
            satisfaction_score = 20
        elif user_bw >= 3:
            satisfaction_score = 30

        return satisfaction_score
