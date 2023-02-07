import numpy as np
from ase import Atoms
from ase.optimize import BFGS
from gpaw import GPAW, PW
from ase.visualize import view
# Define the S8 crystal structure
s8 = Atoms('S8',
           positions=[[0.0, 0.0, 0.0],
                      [1.0, 0.0, 0.0],
                      [0.0, 1.0, 0.0],
                      [1.0, 1.0, 0.0],
                      [0.0, 0.0, 1.0],
                      [1.0, 0.0, 1.0],
                      [0.0, 1.0, 1.0],
                      [1.0, 1.0, 1.0]],
           cell=np.array([[2.0, 0.0, 0.0],
                          [0.0, 2.0, 0.0],
                          [0.0, 0.0, 2.0]]))
s8.center(vacuum=10)
view(s8)
# Set the calculator
calc = GPAW(mode='lcao',
            h=0.2,
            xc='PBE',
            txt='S8_orthorhombic.txt')

s8.set_calculator(calc)

# Optimize the structure
optimizer = BFGS(s8)
optimizer.run(fmax=0.05)

# Write the optimized structure to a file
s8.write('S8_orthorhombic_optimized.xyz')