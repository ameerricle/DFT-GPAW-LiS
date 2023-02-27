from ase import Atoms
from ase.build import bulk
from ase.optimize import BFGS
from ase.constraints import UnitCellFilter
from gpaw import GPAW, PW
from ase.visualize import view


atoms = bulk('Al','fcc')
calc = GPAW(mode=PW(450), xc='PBE',kpts=(8,8,8))
atoms.set_calculator(calc)

opt = BFGS(atoms, logfile = 'Pt.log')
opt.run(fmax=0.01)


a=atoms.get_cell()
print(atoms.get_cell)()
print('Optimized LC:',a)