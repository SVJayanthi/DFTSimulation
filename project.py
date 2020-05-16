# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:28:02 2020

@author: srava
"""
from ase.build import molecule, bulk
from ase.visualize import view
from ase.optimize import BFGSLineSearch, QuasiNewton
from ase.calculators.espresso import Espresso
from ase.constraints import UnitCellFilter
from ase.optimize import LBFGS

"""
pseudopotentials = {'Na': 'Na_pbe_v1.uspp.F.UPF',
                    'Cl': 'Cl.pbe-n-rrkjus_psl.1.0.0.UPF'}
rocksalt = bulk('NaCl', crystalstructure='rocksalt', a=6.0)
calc = Espresso(pseudopotentials=pseudopotentials,
                tstress=True, tprnfor=True, kpts=(3, 3, 3))
rocksalt.calc = calc

ucf = UnitCellFilter(rocksalt)
opt = LBFGS(ucf)
opt.run(fmax=0.005)


# cubic lattic constant
print((8*rocksalt.get_volume()/len(rocksalt))**(1.0/3.0))
"""

H2O = molecule('H2O')

H2O.set_calculator(Espresso())
dyn = QuasiNewton(H2O)
dyn.run(fmax=0.05)

E_H2O = H2O.get_potential_energy()



E_rxn = 2*E_H2 + E_O2 - 2E_H2O
print(E_rxn) # answer is in eV
"""