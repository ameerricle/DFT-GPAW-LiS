import numpy as np
from ase import Atoms
from gpaw import GPAW, PW
from ase.optimize import BFGS
from ase.visualize import view

cell = [[12, 0, 0], [0, 12, 0], [0, 0, 12]]

Li2S4 = Atoms('Li2S4',
              positions=[[3.49674, 5.46610, 10.08799],
                         [6.13868,4.01459,10.05193],
                         [4.77598, 5.77867, 12.27283],
                         [4.904359,3.658042,12.250876],
                         [3.950744,3.075341,10.474040],
                         [5.692604,6.395714,10.487742]], 
              cell=cell)
Li2S4.center()
view(Li2S4)
#Set the calculator
calc = GPAW(mode=PW(400),
            h=0.2,
            xc='PBE',
            txt='Li2S4.txt')

Li2S4.set_calculator(calc)

# Optimize the structure
optimizer = BFGS(Li2S4, trajectory = 'Li2S4.traj')
optimizer.run(fmax=0.01)

# Write the optimized structure to a file
Li2S4.write('Li2S4_optimized.xyz')