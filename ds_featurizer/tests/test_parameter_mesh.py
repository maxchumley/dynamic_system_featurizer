from ds_featurizer import parameter_mesh
import pytest
import numpy as np 
import os

"""
Note: Run this file in terminal from the tests folder and add the parent directory to the python path first. Use: pytest -v test_parameter_mesh.py to test. Make sure that the proper conda environment is activated.

Linux/Unix/macOS: export PYTHONPATH=<path-to-your-directory>:$PYTHONPATH
Windows (in Anaconda Shell or Power Shell): set Pythonpath=<path-to-your-directory>;%Pythonpath%

export PYTHONPATH=/Users/maxchumley/cmse802-chumley/dynamical_system_attractor_featurizer:$PYTHONPATH

"""



def test_parameters_file():
    # test if function creates the csv file of parameters
    variables = {'x':[1,2,3],
                 'y':[4,5,6]}
    parameter_mesh.create_mesh(variables)
    if os.path.exists(os.path.join(os.getcwd(),'system.npy')):
        system = str(np.load('system.npy'))
    else:
        raise RuntimeError("Run folder_setup before creating the parameter mesh.")
    assert os.path.exists(os.path.join(os.getcwd(),os.path.join('Basin_'+system, 'parameters.csv'))) == True

def test_array_files():
    # test if function creates the individual parameter arrays
    variables = {'x':[1,2,3],
                 'y':[4,5,6]}
    iterations = 1
    for item in variables:
        iterations *= len(variables[item])
    parameter_mesh.create_mesh(variables)
    
    if os.path.exists(os.path.join(os.getcwd(),'system.npy')):
        system = str(np.load('system.npy'))
    else:
        raise RuntimeError("Run folder_setup before creating the parameter mesh.")
    print(f"ITERATIONS:{iterations}")
    for i in range(1,iterations):
        assert os.path.exists(os.path.join(os.getcwd(),os.path.join('Basin_'+system, os.path.join('parameter_arrays', str(i)+'.npy')))) == True


def test_bad_type_variables():
    # Test if function raises type error for incorrect data type inputs
    with pytest.raises(TypeError) as excinfo:
        variables = 10
        parameter_mesh.create_mesh(variables)
    assert "Input should be a dictionary." in str(excinfo.value)

def test_bad_variable():
    # Test if function raises type error for incorrect data type inputs
    with pytest.raises(TypeError) as excinfo:
        variables = {10:[1,2,3],
                     20:[4,5,6]}
        parameter_mesh.create_mesh(variables)
    assert "variable 10 should be a string." in str(excinfo.value)

def test_bad_value():
    # Test if function raises type error for incorrect data type inputs
    with pytest.raises(TypeError) as excinfo:
        variables = {'x':[1,2,3],
                     'y':2}
        parameter_mesh.create_mesh(variables)
    assert "variable y values should be a list or array." in str(excinfo.value)   
    

    