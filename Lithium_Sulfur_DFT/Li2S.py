import numpy as np
from ase import Atoms
from gpaw import GPAW, PW
from ase.optimize import BFGS
from ase.visualize import view

cell = [[12, 0, 0], [0, 12, 0], [0, 0, 12]]

Li2S = Atoms('Li2S',
              positions=[[3.553320,3.572933,11.188537],
                         [6.407432,5.883458,12.102454],
                         [4.273244,5.609337,11.625341]], 
              cell=cell)
Li2S.center()
view(Li2S)
#Set the calculator
calc = GPAW(mode=PW(400),
            h=0.2,
            xc='PBE',
            txt='Li2S.txt')

Li2S.set_calculator(calc)

# Optimize the structure
optimizer = BFGS(Li2S, trajectory = 'Li2S.traj')
optimizer.run(fmax=0.01)

# Write the optimized structure to a file
Li2S.write('Li2S_optimized.xyz')