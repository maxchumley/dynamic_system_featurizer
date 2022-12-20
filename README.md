# Dynamical System Attractor Featurization

## Description

This library allows for visualizing response features over high dimensional parameter spaces for any input dynamical system in the form of images. The user interface is written in python and the simulations are computed with the Julia programming language. A vectorized parameter mesh is generated for the system and pythons multiprocessing library is used to distribute the individual simulations over any desired number of cores on your computer. Three features are built in to this library (standard deviation, mean, and maximum 1D persistence from topological data analysis). The standard deviation can provide an indication of the stability of the system at a given point because a nonzero standard deviation can suggest that the system is oscillating. The mean response allows for locating different attractors in a system for a multistable nonlinear dynamical system. Finally, the maximum 1D persistence from topological data analysis can provide information about loops in the state space of the system which provides a measure of periodicity and can be used for determining if the response may be chaotic. 

This library is meant to be used for exploratory purposes for a dynamical system as the results are purely numerical. However, the results from this library allow for an initial assessment of the system behavior over the input space and can provide insight into how to approach further analysis of a complicated system.


## Installation

1. To install this library, first make sure that anaconda is installed and running a function such as ```conda list``` provides the expected output.

2. In the terminal, change the directory to the *dynamical_system_attractor_featurizer* folder. 

3. Ensure that the file *environment.yml* is in the current folder.

4. Run ```conda env create --prefix ./envs --file environment.yml``` to install the virtual environment with the necessary libraries.

5. Run ```conda activate ./envs``` to activate the virtual environment. 

6. Finally, the library can be imported in python with ```import ds_featurizer as dsf```.  **Note: The first time this library is imported, the Julia programming language and libraries are installed. This can take several minutes.** 

7. Ensure that the *systems* folder is in the directory and contains the Julia file for your system. To add a new system, a function called  ```trajectory(p, t_start, t_end)``` is written in Julia that takes as input the system parameters, and the simulation start and end time. This function should return an array containing the simulation times, and the system state space trajectories. See ```duffing.jl``` for an example of this function for an ODE system. Other solvers and equation types can be implemented following the [Julia DifferentialEquations.jl](https://diffeq.sciml.ai/stable/) instructions.

After completing the above steps, the user interface functions can be used to generate the desired featurized images. See the file ```example_duffing.ipynb``` for a detailed example of how to use this library on the unforced duffing oscillator dynamical system. The example uses latex for labeling the plot axes. A valid latex installation is required to run this example as is, or simply changing the plot labels and keys variables to not require latex can avoid issues.

## Unit Testing Suite

A unit testing suite is bundled with the ds_featurizer library in the *tests* folder. The notebook titled ```interface_testing.ipynb``` contains the instructions for conducting unit testing on the core functions in this library. Care should be taken to ensure that the correct conda environment is activated to have the proper libraries **and** the directory that *ds_featurizer* is in needs to be added to the python path. Instructions for doing this are contained in the test suite notebook. The test system that is in the tests folder is a copy of the duffing oscillator.

## File Structure (User Interface Functions)

### folder_setup.py

This file is used to generate the necessary folder structure for each system being simulated. It creates a folder for the system containing folders for each desired feature.

**Inputs:** Feature names for folder creation, system name

**Outputs:** N/A 

### parameter_mesh.py

This file is used to generate a list of parameter combinations to simulate the system over. This file is useful for studying system bifurcations due to changes in parameters. 

**Input:** System parameters (Dictionary of key value pairs with keys as the parameters and values as all of the parameter values to be considered.

**Output:** numpy array files containing all combinations of the parameters to vectorize the code with respect to the parameters.

### generate_basin.py

This file is used to loop through the parameter mesh to call the Julia code and obtain the basins of attraction for each set of parameters and plot them nicely using matplotlib. This file will also attempt to run each set of parameters in parallel.

**Inputs:** Simulation parameters - Simulation time, initial condition ranges, time step size, featurizer functions

**Outputs:** Basin of attraction images for the 2D system. 



