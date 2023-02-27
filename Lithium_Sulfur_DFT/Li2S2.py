import numpy as np
from ase import Atoms
from gpaw import GPAW, PW
from ase.optimize import BFGS
from ase.visualize import view

cell = [[12, 0, 0], [0, 12, 0], [0, 0, 12]]

Li2S2 = Atoms('Li2S2',
              positions=[[6.151261,5.770450,12.646746],
                         [4.077019,4.257900,10.486744],
                         [3.847644,5.571856,12.388333],
                         [5.023034,3.739536,12.541049]], 
              cell=cell)
Li2S2.center()
view(Li2S2)

#Set the calculator
calc = GPAW(mode=PW(400),
            h=0.2,
            xc='PBE',
            txt='Li2S2.txt')

Li2S2.set_calculator(calc)

# Optimize the structure
optimizer = BFGS(Li2S2, trajectory = 'Li2S2.traj')
optimizer.run(fmax=0.01)

# Write the optimized structure to a file
Li2S2.write('Li2S2_optimized.xyz')