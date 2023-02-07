import numpy as np
from ase import Atoms
from ase.build import fcc111
from gpaw import GPAW, PW
from ase.optimize import BFGS

a = 4.05
slab = fcc111('Al', (4, 4, 1), a=a, vacuum=10.0)

calc = GPAW(mode=PW(400),
            xc='PBE',
            kpts=(8, 8, 1),
            parallel={'band': 1},
            txt='Al_gs.txt')
slab.set_calculator(calc)
from ase.optimize import BFGS
opt = BFGS(slab, trajectory='Al_opt.traj')
opt.run(fmax=0.05)