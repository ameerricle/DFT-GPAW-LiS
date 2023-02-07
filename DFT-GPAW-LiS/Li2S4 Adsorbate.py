import numpy as np
from ase import Atoms
from gpaw import GPAW, PW
from ase.optimize import BFGS
from ase.visualize import view
# Define the Li2S8 adsorbate
li2s4 = Atoms('Li2S4',
              positions=[[0, 0, 0],
                         [2.5, 0, 0],
                         [1, 0, 0],
                         [1.5, 0, 0],
                         [2.0,0,0],
                         [0.5,0,0]], 
              cell=np.eye(3) * 4)
li2s4.center(vacuum=10)
view(li2s4)
# Set the calculator
calc = GPAW(mode='lcao',
            h=0.2,
            xc='PBE',
            txt='Li2S8.txt')

li2s4.set_calculator(calc)

# Optimize the structure
optimizer = BFGS(li2s4)
optimizer.run(fmax=0.05)

# Write the optimized structure to a file
li2s4.write('Li2S4_optimized.xyz')