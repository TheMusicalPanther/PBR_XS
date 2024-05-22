import pandas as pd # type: ignore
import numpy as np
import time
import matplotlib.pyplot as plt # type: ignore
import random

class Particle:


    def __init__(self, num_groups, num_meshes, fine_energy_bounds, user_energy_bounds):
        self.num_groups = num_groups
        self.fine_energy_bounds = fine_energy_bounds
        self.user_energy_bounds = user_energy_bounds
        self.fine_to_sample = np.array([i for i in self.fine_energy_bounds if i not in self.user_energy_bounds])

        coarse_g = self.num_groups
        user_g = np.size(self.user_energy_bounds)-1
        fine_g = np.size(self.fine_to_sample)-1

        # Pick N_G-N_B+1 random bounds from fine_g for each mesh
        self.coarse_energy_bounds = np.empty([num_meshes, num_groups])
        for i in range(num_meshes):
            random_vals = random.sample(range(fine_g+1), coarse_g-user_g-1)
            coarse = np.append(self.fine_to_sample[random_vals], self.user_energy_bounds)
            coarse[::-1].sort()
            self.coarse_energy_bounds[i, :] = coarse

    def __str__(self):
        return str(self.coarse_energy_bounds)
    
    

