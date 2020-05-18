# DFTSimulation

![Reaction Energy Graph](reactionenergy.PNG)

## Author
Sravan Jayanthi

## Density Functional Theory Simulation
The simulation is designed to study the nuclear structure of atoms 
Density-functional theory (DFT) is a computational quantum mechanical modelling method used in physics, chemistry and materials science to investigate the electronic structure (or nuclear structure) (principally the ground state) of many-body systems, in particular atoms, molecules, and the condensed phases. Using this theory, the properties of a many-electron system can be determined by using functionals, i.e. functions of another function. In the case of DFT, these are functionals of the spatially dependent electron density. 

## Description
This project contains the three scripts, outputted csv, reaction spreadsheet, graphs, and the silicon configuration for the Density Functional Theory simulation. The main library utilized is the ASE (Atomic Simulation Environment).

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
