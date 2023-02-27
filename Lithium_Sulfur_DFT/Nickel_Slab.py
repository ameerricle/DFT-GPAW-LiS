from ase.optimize import BFGS
from ase.build import fcc111
from ase.constraints import StrainFilter
from gpaw import GPAW, PW
from ase.build import bulk
from ase.visualize import view

a = 3.52
k = 2

slab = fcc111("Ni", size=(4,4,1), vacuum=10)
#view(slab)

calc = GPAW(mode=PW(400), xc='PBE', kpts={'size':(k,k,1)}, txt = "Ni_slab.out")
slab.set_calculator(calc)


relax = BFGS(slab, trajectory='Ni_slab.traj', logfile='Ni_slab.log')
relax.run(fmax=0.05)

# view the final structure
#view(slab)
