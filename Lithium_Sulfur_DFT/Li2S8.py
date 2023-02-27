import numpy as np
from ase import Atoms
from gpaw import GPAW, PW
from ase.optimize import BFGS
from ase.visualize import view

cell = [[12, 0, 0], [0, 12, 0], [0, 0, 12]]

Li2S8 = Atoms('Li2S8',
              positions=[[6.208576, 4.594446, 8.410428],
                         [3.556629, 5.417495, 8.378384],
                         [4.053565, 5.692344, 12.482087],
                         [5.448478, 4.106555, 12.494457],
                         [4.729330, 2.474685, 11.411665],
                         [4.853181, 7.375244, 11.540382],
                         [5.576021, 2.389911, 9.496103],
                         [4.123749, 7.574200, 9.587539],
                         [4.299488, 3.128296, 8.022188],
                         [5.479856, 6.903697, 8.151800]], 
              cell=cell)
Li2S8.center()
view(Li2S8)

#Set the calculator
calc = GPAW(mode=PW(400),
            h=0.2,
            xc='PBE',
            txt='Li2S8.txt')

Li2S8.set_calculator(calc)

# Optimize the structure
optimizer = BFGS(Li2S8, trajectory = 'Li2S8.traj')
optimizer.run(fmax=0.01)

# Write the optimized structure to a file
Li2S8.write('Li2S8_optimized.xyz')