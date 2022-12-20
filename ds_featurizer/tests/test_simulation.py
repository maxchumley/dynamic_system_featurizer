from ds_featurizer import simulation
import pytest
import numpy as np 

"""
Note: Run this file in terminal from the tests folder and add the parent directory to the python path first. Use: pytest -v test_simulation.py to test. Make sure that the proper conda environment is activated.

Linux/Unix/macOS: export PYTHONPATH=<path-to-your-directory>:$PYTHONPATH
Windows (in Anaconda Shell or Power Shell): set Pythonpath=<path-to-your-directory>;%Pythonpath%

export PYTHONPATH=/Users/maxchumley/cmse802-chumley/dynamical_system_attractor_featurizer:$PYTHONPATH

"""



def test_features_good():
    # test if function returns correct features for test data
    data = [[0,2,0,2],[10,10,10,10]]
    ts = np.array([0,1,2,3])
    feat = ['sd','mean', 'maxh1']
    assert simulation.features(data,ts, feat) == [1.0,11.0,0] 


def test_bad_type():
    # Test if function raises type error for incorrect data type inputs
    with pytest.raises(TypeError) as excinfo:
        data = [1,2,3]
        ts = [4,5,6]
        feat = 2
        simulation.features(data,ts,feat)
    assert 'One or more inputs to features is an incorrect type.' in str(excinfo.value)
    
    
def test_empty():
    # Test if error is raised for one or more empty inputs
    with pytest.raises(ValueError) as excinfo:
        data = [[],[]]
        ts = np.array([])
        feat = []
        simulation.features(data,ts,feat)
    assert 'One or more empty inputs to features.' in str(excinfo.value)
    
def test_shape_data():
    # Test if error is raised for incorrect shape input data array
    with pytest.raises(ValueError) as excinfo:
        data = [1,2]
        ts = np.array([1,2])
        feat = ['sd']
        simulation.features(data,ts,feat)
    assert "The simulation data is not the correct shape. Did you mean to transpose?" in str(excinfo.value)
    
def test_shape_ts():
    # Test if error is raised for incorrect shape input time array
    with pytest.raises(ValueError) as excinfo:
        data = [[1,2,3],[4,5,6]]
        ts = np.array([[1,2],[3,4]])
        feat = ['sd']
        simulation.features(data,ts,feat)
    assert "Time array does not have the correct shape." in str(excinfo.value)
    
    

    