from ase.io import read
from ase.visualize import view
from ase.build import fcc111, add_adsorbate
from ase.optimize import BFGS
from gpaw import GPAW, PW

slab = read('/home/ameerracle/Desktop/Lithium_Sulfur_DFT/Ni_slab.traj')
adsorbate = read('/home/ameerracle/Desktop/Lithium_Sulfur_DFT/Li2S4.traj')

#combi= slab + adsorbate

#print(combo)
#slab.extend(adsorbate)
add_adsorbate(slab,adsorbate,3,'ontop')
#combo=slab
#view(slab)
#view(combi)
#view(combo)
print(slab)
slab.center(vacuum=10)
view(slab)
k=1
""" calc = GPAW(mode=PW(400),
            h=0.2,
            xc='PBE',
            kpts=(k,k,1),
            txt='Ni_slab_Li2S4.txt')

slab.set_calculator(calc)
combo = BFGS(slab, trajectory = 'Ni_slab_Li2S4.traj')
combo.run(fmax=0.1) """