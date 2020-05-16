# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:29:38 2020

@author: srava
"""

from ase.build import molecule, bulk
from ase.visualize import view
from ase.calculators.emt import EMT
from ase.optimize import BFGSLineSearch, QuasiNewton

water = molecule('H2O')
print(water)
print(water.positions)

#iron = bulk('Fe', cubic = True)
#view(iron)


calc = EMT()
water.set_calculator(calc)
energy = water.get_potential_energy()
forces = water.get_forces()

print(energy)
print(forces)

relax = BFGSLineSearch(atoms = water)
relax.run(fmax = 0.05) # relax the structure until the maximum force is 0.05 eV/A

print(water.positions)
#view(water)

O2 = molecule('O2')
O2.set_calculator(EMT())

dyn = QuasiNewton(O2)
dyn.run()
E_O2 = O2.get_potential_energy()


H2 = molecule('H2')
H2.set_calculator(EMT())
dyn = QuasiNewton(H2)
dyn.run()
E_H2= H2.get_potential_energy()


H2O = molecule('H2O')


H2O.set_calculator(EMT())
dyn = QuasiNewton(H2O)
dyn.run(fmax=0.05)

E_H2O = H2O.get_potential_energy()

E_rxn = E_H2O - E_H2 - 0.5*E_O2
print(E_rxn) # answer is in eV