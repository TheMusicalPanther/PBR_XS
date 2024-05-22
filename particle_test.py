import pandas as pd # type: ignore
import numpy as np
import time
import matplotlib.pyplot as plt # type: ignore
import random
from particle_swarm import Particle #type: ignore

N_G = 12
meshes_per_particle = 3
spec_f = "Fine_Test.txt"

spec = pd.read_csv(spec_f, sep=",", header=None, index_col=None)
spec = spec.to_numpy()

E_vec = spec

user_bounds = np.array([np.max(E_vec), 7*10**5, 2*10**4, np.min(E_vec)]) #eV, descending

particle_test = Particle(N_G, meshes_per_particle, E_vec, user_bounds)
print(particle_test)