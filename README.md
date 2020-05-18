# DFTSimulation

![Reaction Energy Graph](reactionenergy.PNG)

## Author
Sravan Jayanthi

## Density Functional Theory Simulation
The simulation is designed to study the quantum mechanical phenomenon of atomic interactions and the forces experienced within multi-body system. Density Functional Theory relies on electronic configurations being in the most optimal geometry such that atom centered basis sets represent a relaxed state of the atom. Then the model calculates minimal adaptive basis sets to represent polarized atomic orbitals
The goal was to design a machin{\displaystyle V_{\text{s}}(\mathbf {r} )=V(\mathbf {r} )+\int {\frac {e^{2}n_{\text{s}}(\mathbf {r} ')}{|\mathbf {r} -\mathbf {r} '|}}\,\mathrm {d} ^{3}\mathbf {r} '+V_{\text{XC}}[n_{\text{s}}(\mathbf {r} )],}e learning model utilized polarized atomic orbitals to transform traditional
atom centered basis sets used in molecular dynamic simulations to minimal adaptive basis sets that would utilize
their small size and conditioned qualities to perform computations more efficiently. The study analyzed the 
mathematical techniques required to transform such basis sets so that important properties of atoms are included
in the simulations. The machine learning model was designed to approximate the complex features being removed
during the transformation. Then, the model would be validated through molecular dynamics simulations using liquid
water that would showcase how consistent and accurate the resulting basis would be. The performance of such
simulations would be optimized and perform faster and require less memory to compute.

## Description
This project contains the three scripts, outputted csv, reaction spreadsheet, graphs, and the bash script configuration for the Density Functional Theory simulation. The main library utilized is the ASE (Atomic Simulation Environment).

*project.py- script for sodium chloride reaction*

*sample.py- script utilizing SPARC calculator*

*trial.py- script simulating dihydrogen monoxide reaction*

*output.csv- outputted values from simulation*

*Reaction.xlsx- calculations displaying reaction energies*

*bash.sh- configuration for training on supercomputer*


### Code
Sample code of simulating the potential energy of dihydrogen monoxide

            H2O.set_calculator(EMT())
            dyn = QuasiNewton(H2O)
            dyn.run(fmax=0.05)
            E_H2O = H2O.get_potential_energy()


## License
[MIT](LICENSE)
