import pandas as pd # type: ignore
import numpy as np
import time
import matplotlib.pyplot as plt # type: ignore
import mesh_gen as mg # type: ignore

spec_f_name = "sample_spec.csv"
nuclide_data_f = "sample_data.txt"
tolerance = 0.9
user_bounds = [7*10**5, 2*10**4] #eV; descending

hyperfine, flux, fine, fine_flux = mg.comp_fine_mesh(tolerance, user_bounds, spec_f_name, nuclide_data_f)

pd.DataFrame(fine).to_csv("Fine_Test.txt", header=None, index=None)

print("Number of groups: " +str(len(fine)-1))

fig, ax = plt.subplots(2, layout='constrained')
plt.yscale('linear')
ax[0].set_xscale('log')
ax[1].set_xscale('log')
ax[0].grid()
ax[0].plot(hyperfine, flux, zorder=1, linewidth=0.5)


ax[1].plot(hyperfine, flux, zorder=1, linewidth=0.25)
ax[1].stairs(fine_flux, edges=fine, zorder=2)

ax[1].legend(["Hyperfine Flux", "Fine Group Flux"])

plt.grid()

ax[0].set_ylabel(r'$\phi(E)$')

ax[1].set_xlabel('Energy (ev)')
ax[1].set_ylabel(r'$\phi(E)$')
#plt.xscale('log')

ax[0].set_title('Tolerance: '+str(tolerance))

plt.show()