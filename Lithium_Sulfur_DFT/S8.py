import numpy as np
from ase import Atoms
from gpaw import GPAW, PW
from ase.optimize import BFGS
from ase.visualize import view

cell = [[12, 0, 0], [0, 12, 0], [0, 0, 12]]

S8 = Atoms('S8',
              positions=[[5.056469, 3.463830, 13.061103],
                        [5.934586, 2.517052, 9.930627],
                        [6.658167, 3.195555, 11.758889],
                        [5.770149, 4.135509, 8.631433],
                        [4.511816, 5.472268, 13.061103],
                        [3.633699, 6.419046, 9.930627],
                        [2.910118, 5.740544, 11.758889],
                        [3.798136, 4.800590, 8.631433]], 
              cell=cell)
S8.center()
view(S8)

#Set the calculator
calc = GPAW(mode=PW(400),
            h=0.2,
            xc='PBE',
            txt='S8.txt')

S8.set_calculator(calc)

# Optimize the structure
optimizer = BFGS(S8, trajectory = 'S8.traj')
optimizer.run(fmax=0.01)

# Write the optimized structure to a file
S8.write('S8_optimized.xyz')