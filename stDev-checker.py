import numpy as np
from math import sqrt


class WeightedStandardDeviationCounter:
    sample_sum = 0
    squared_samples_sum = 0
    st_dev = 0
    m = 0

    def __init__(self):
        self.sample_sum = 0
        self.squared_samples_sum = 0
        self.st_dev = 0
        self.m = 0

    def update_standard_deviation(self, weight_modifier, new_sample):
        if self.st_dev == 0:
            self.st_dev = 1
            self.m = 1
            self.sample_sum = new_sample
            self.squared_samples_sum = new_sample ** 2
            return

        self.m = self.m * weight_modifier + 1
        self.squared_samples_sum = self.squared_samples_sum * (weight_modifier ** 2) + new_sample ** 2
        self.sample_sum = self.sample_sum * weight_modifier + new_sample
        self.st_dev = self.squared_samples_sum / (self.m - 1)
        self.st_dev -= (self.sample_sum ** 2) / (self.m * (self.m - 1))
        self.st_dev = sqrt(self.st_dev)



sigma = 1
mean = 0
sample_size = 10000
b = 0.5

seed = 1

np.random.seed(seed)


f = open(str(b) + ".csv", "w+")

s = np.random.normal(mean, sigma, sample_size)
wsdc = WeightedStandardDeviationCounter()

for i in range(0, sample_size):
    wsdc.update_standard_deviation(b, s[i])
    f.write(str(wsdc.st_dev) + ",")