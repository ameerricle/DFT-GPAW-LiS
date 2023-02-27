import numpy as np
from ase import Atoms
from gpaw import GPAW, PW
from ase.optimize import BFGS
from ase.visualize import view

cell = [[12, 0, 0], [0, 12, 0], [0, 0, 12]]

Li2S6 = Atoms('Li2S6',
              positions=[[6.346369,4.768809, 10.104627],
                         [3.409760,4.900271, 9.929599],
                         [3.995729,5.664730,12.580343],
                         [5.436404,3.987693,12.656598],
                         [4.582386,2.459906,11.567938],
                         [4.967884,7.206634,11.618039],
                         [4.820690,2.925118, 9.552862],
                         [4.984431,6.750833, 9.587484]], 
              cell=cell)
Li2S6.center()
view(Li2S6)

#Set the calculator
calc = GPAW(mode=PW(400),
            h=0.2,
            xc='PBE',
            txt='Li2S6.txt')

Li2S6.set_calculator(calc)

# Optimize the structure
optimizer = BFGS(Li2S6, trajectory = 'Li2S6.traj')
optimizer.run(fmax=0.01)

# Write the optimized structure to a file
Li2S6.write('Li2S6_optimized.xyz')