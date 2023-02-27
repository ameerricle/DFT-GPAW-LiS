from ase.optimize import BFGS
from ase.constraints import StrainFilter
from gpaw import GPAW, PW
from ase.build import bulk
from ase.visualize import view
from ase.io import Trajectory, read

#metals = ['Cu', 'Ag', 'Au', 'Ni', 'Pd', 'Pt', 'Al', 'Pb','Al','Rh','Sr','Ca','Ir']
metals = ['Cu','Ag']
lc_file = open('metal_LC.txt', 'w')

for metal in metals:
    atoms = bulk(metal, 'fcc', cubic=True)
    calc = GPAW(mode=PW(400), xc='PBE', kpts=(4, 4, 4), txt=f'{metal}.out')
    atoms.calc = calc
    
    sf = StrainFilter(atoms)
    opt = BFGS(sf)
    traj = Trajectory(f'{metal}.traj', 'w', atoms)
    opt.attach(traj)
    opt.run(0.1)
    
    lc = atoms.get_cell()[0,0]
    print(f'{metal}: {lc}')
    lc_file.write(f'{metal}: {lc} \n')

lc_file.close()
