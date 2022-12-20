from ds_featurizer import folder_setup
import pytest
import numpy as np 
import os

"""
Note: Run this file in terminal from the tests folder and add the parent directory to the python path first. Use: pytest -v test_simulation.py to test. Make sure that the proper conda environment is activated.

Linux/Unix/macOS: export PYTHONPATH=<path-to-your-directory>:$PYTHONPATH
Windows (in Anaconda Shell or Power Shell): set Pythonpath=<path-to-your-directory>;%Pythonpath%

export PYTHONPATH=/Users/maxchumley/cmse802-chumley/dynamical_system_attractor_featurizer:$PYTHONPATH

"""



def test_system_folder():
    # test if function creates correct system folder
    folders = ['mean']
    system = 'test_sys'
    folder_setup.folder_setup(folders, system)
    assert os.path.exists(os.path.join(os.getcwd(),'Basin_'+system)) == True

def test_feature_folders():
    # test if function creates correct feature folder.
    folders = ['mean']
    system = 'test_sys'
    folder_setup.folder_setup(folders, system)
    assert os.path.exists(os.path.join(os.getcwd(),os.path.join('Basin_'+system, folders[0]))) == True

def test_param_array_folder():
    # test if function creates correct feature folder.
    folders = ['mean']
    system = 'test_sys'
    folder_setup.folder_setup(folders, system)
    assert os.path.exists(os.path.join(os.getcwd(),os.path.join('Basin_'+system, 'parameter_arrays'))) == True

def test_system_name_file():
    folders = ['mean']
    system = 'test_sys'
    folder_setup.folder_setup(folders, system)
    assert os.path.exists(os.path.join(os.getcwd(),'system.npy')) == True

def test_bad_type_folders():
    # Test if function raises type error for incorrect data type inputs
    with pytest.raises(TypeError) as excinfo:
        folders = np.array(['mean','sd'])
        system = 'test_sys'
        folder_setup.folder_setup(folders, system)
    assert "folders needs to be a list." in str(excinfo.value)

def test_bad_type_system():
    # Test if function raises type error for incorrect data type inputs
    with pytest.raises(TypeError) as excinfo:
        folders = ['mean','sd']
        system = 2
        folder_setup.folder_setup(folders, system)
    assert "system needs to be a string." in str(excinfo.value)
    
def test_bad_type_folder_name():
    # Test if function raises type error for incorrect data type inputs
    with pytest.raises(TypeError) as excinfo:
        folders = [True,'sd']
        system = 'test_sys'
        folder_setup.folder_setup(folders, system)
    assert "True in folders is not a string." in str(excinfo.value)   
    
    

    