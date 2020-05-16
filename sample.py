# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:50:40 2020

@author: srava
"""

from ase.build import molecule, bulk
from ase.visualize import view
from ase.calculators.emt import EMT
from ase.optimize import BFGSLineSearch, QuasiNewton

import csv

val = [1.0]
for i in val:
    print(i)
output = []

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

E_rxn = 2*E_H2 + E_O2 - 2*E_H2O
print(E_rxn) # answer is in eV

output.append([E_O2, E_H2, E_H2O, E_rxn])

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(output)
    
    
import csv
from sparc.sparc_core import SPARC
from ase.build import molecule

h_val = [0.2, 0.18, 0.16, 0.14, 0.12, 0.1]
output = []
for i in h_val:
        # make the atoms
        atoms = molecule('H2O')
        atoms.cell = [[6,0,0],[0,6,0],[0,0,6]]
        atoms.center()

        h_atom = molecule('H2')
        h_atom.cell = [[6,0,0],[0,6,0],[0,0,6]]
        h_atom.center()

        o_atom = molecule('O2')
        o_atom.cell = [[6,0,0],[0,6,0],[0,0,6]]
        o_atom.center()

        # set up the calculator
        calc = SPARC(KPOINT_GRID=[1,1,1], h = i, EXCHANGE_CORRELATION = 'GGA', TOL_SCF=1e-5, RELAX_FLAG=1, PRINT_FORCES=1, PRINT_RELAXOUT=1)

        # set the calculator on the atoms and run
        atoms.set_calculator(calc)
        h_atom.set_calculator(calc)
        o_atom.set_calculator(calc)
        E_rxn = atoms.get_potential_energy() - h_atom.get_potential_energy() - 0.5 * o_atom.get_potential_energy()
        print(h_atom.get_potential_energy())
        print(o_atom.get_potential_energy())
        print(E_rxn)
        output.append([h_atom.get_potential_energy(), o_atom.get_potential_energy(), atoms.get_potential_energy(), E_rxn])

with open('reaction_energy.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(output)
