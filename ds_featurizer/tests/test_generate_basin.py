from ds_featurizer import parameter_mesh
from ds_featurizer import config
from ds_featurizer import generate_basin
from ds_featurizer import folder_setup
import pytest
import numpy as np 
import os

"""
Note: Run this file in terminal from the tests folder and add the parent directory to the python path first. Use: pytest -v test_generate_basin.py to test. Make sure that the proper conda environment is activated.

Linux/Unix/macOS: export PYTHONPATH=<path-to-your-directory>:$PYTHONPATH
Windows (in Anaconda Shell or Power Shell): set Pythonpath=<path-to-your-directory>;%Pythonpath%

export PYTHONPATH=/Users/maxchumley/cmse802-chumley/dynamical_system_attractor_featurizer:$PYTHONPATH

"""



def test_basin_creation():
    # test if function creates the csv file of parameters
    # Time span for each simulation and set limits for the image axes
    t_start = 1000
    t_end = 2000
    x_start = -2.0
    x_end = 2.0
    y_start = -2.0
    y_end = 2.0


    # Set number of CPU cores to use
    config.CORES = 1

    # System name
    system = 'test_sys'

    # Basin image size
    pixels = 3

    t_range = [t_start, t_end]
    limits = [x_start, x_end, y_start, y_end, pixels]

    # Specify features and folders to be created (Key is used in the image titles)
    keys = [r'$\bar{x}$']
    folders = ['mean']

    # Set image axes labels
    labels = [r'$x_0$',r'$\dot{x}_0$']

    # Pack the folder names, image title, and axes labels into one list
    feat = [folders, keys, labels]

    # Setup the folder structure for saving the images
    folder_setup.folder_setup(folders, system)

    # Dictionary of parameter values. Use the variable pixels to control basin variables
    # NOTE: The basin plot parameters must be last
    variables = {
        'Row': [1],
        'd': [0.15],
        'alpha': [-1.0],
        'xo': np.linspace(x_start, x_end, pixels),
        'yo': np.linspace(y_start, y_end, pixels),
    }

    # Create the vectorized parameter mesh for the variables
    mesh = parameter_mesh.create_mesh(variables)

    # Extract the list of variables and parameters from the mesh
    variables = mesh[0]
    parameters = mesh[1]
    generate_basin.generatebasin(parameters, t_range, limits, feat, system)

    assert os.path.exists(os.path.join(os.getcwd(),os.path.join('Basin_'+system, os.path.join('mean', str(1)+'.png')))) == True

def test_bad_parameter_type():
    # test if function creates the csv file of parameters
    # Time span for each simulation and set limits for the image axes
    with pytest.raises(TypeError) as excinfo:
        t_start = 1000
        t_end = 2000
        x_start = -2.0
        x_end = 2.0
        y_start = -2.0
        y_end = 2.0


        # Set number of CPU cores to use
        config.CORES = 1

        # System name
        system = 'test_sys'

        # Basin image size
        pixels = 3

        t_range = [t_start, t_end]
        limits = [x_start, x_end, y_start, y_end, pixels]

        # Specify features and folders to be created (Key is used in the image titles)
        keys = [r'$\bar{x}$']
        folders = ['mean']

        # Set image axes labels
        labels = [r'$x_0$',r'$\dot{x}_0$']

        # Pack the folder names, image title, and axes labels into one list
        feat = [folders, keys, labels]

        # Setup the folder structure for saving the images
        folder_setup.folder_setup(folders, system)

        # Dictionary of parameter values. Use the variable pixels to control basin variables
        # NOTE: The basin plot parameters must be last
        variables = {
            'Row': [1],
            'd': [0.15],
            'alpha': [-1.0],
            'xo': np.linspace(x_start, x_end, pixels),
            'yo': np.linspace(y_start, y_end, pixels),
        }

        # Create the vectorized parameter mesh for the variables
        mesh = parameter_mesh.create_mesh(variables)

        # Extract the list of variables and parameters from the mesh
        variables = mesh[0]
        parameters = 10
        generate_basin.generatebasin(parameters, t_range, limits, feat, system)

    assert "parameters needs to be a numpy array." in str(excinfo.value)

def test_bad_t_range_type():
    # test if function creates the csv file of parameters
    # Time span for each simulation and set limits for the image axes
    with pytest.raises(TypeError) as excinfo:
        t_start = 1000
        t_end = 2000
        x_start = -2.0
        x_end = 2.0
        y_start = -2.0
        y_end = 2.0


        # Set number of CPU cores to use
        config.CORES = 1

        # System name
        system = 'test_sys'

        # Basin image size
        pixels = 3

        t_range = np.array([t_start, t_end])
        limits = [x_start, x_end, y_start, y_end, pixels]

        # Specify features and folders to be created (Key is used in the image titles)
        keys = [r'$\bar{x}$']
        folders = ['mean']

        # Set image axes labels
        labels = [r'$x_0$',r'$\dot{x}_0$']

        # Pack the folder names, image title, and axes labels into one list
        feat = [folders, keys, labels]

        # Setup the folder structure for saving the images
        folder_setup.folder_setup(folders, system)

        # Dictionary of parameter values. Use the variable pixels to control basin variables
        # NOTE: The basin plot parameters must be last
        variables = {
            'Row': [1],
            'd': [0.15],
            'alpha': [-1.0],
            'xo': np.linspace(x_start, x_end, pixels),
            'yo': np.linspace(y_start, y_end, pixels),
        }

        # Create the vectorized parameter mesh for the variables
        mesh = parameter_mesh.create_mesh(variables)

        # Extract the list of variables and parameters from the mesh
        variables = mesh[0]
        parameters = mesh[1]
        generate_basin.generatebasin(parameters, t_range, limits, feat, system)

    assert "t_range needs to be a list." in str(excinfo.value)

def test_bad_t_range_length():
    # test if function creates the csv file of parameters
    # Time span for each simulation and set limits for the image axes
    with pytest.raises(ValueError) as excinfo:
        t_start = 1000
        t_end = 2000
        x_start = -2.0
        x_end = 2.0
        y_start = -2.0
        y_end = 2.0


        # Set number of CPU cores to use
        config.CORES = 1

        # System name
        system = 'test_sys'

        # Basin image size
        pixels = 3

        t_range = [t_start, t_end, t_start]
        limits = [x_start, x_end, y_start, y_end, pixels]

        # Specify features and folders to be created (Key is used in the image titles)
        keys = [r'$\bar{x}$']
        folders = ['mean']

        # Set image axes labels
        labels = [r'$x_0$',r'$\dot{x}_0$']

        # Pack the folder names, image title, and axes labels into one list
        feat = [folders, keys, labels]

        # Setup the folder structure for saving the images
        folder_setup.folder_setup(folders, system)

        # Dictionary of parameter values. Use the variable pixels to control basin variables
        # NOTE: The basin plot parameters must be last
        variables = {
            'Row': [1],
            'd': [0.15],
            'alpha': [-1.0],
            'xo': np.linspace(x_start, x_end, pixels),
            'yo': np.linspace(y_start, y_end, pixels),
        }

        # Create the vectorized parameter mesh for the variables
        mesh = parameter_mesh.create_mesh(variables)

        # Extract the list of variables and parameters from the mesh
        variables = mesh[0]
        parameters = mesh[1]
        generate_basin.generatebasin(parameters, t_range, limits, feat, system)

    assert "t_range should contain only t_start and t_end." in str(excinfo.value)

def test_bad_limits_type():
    # test if function creates the csv file of parameters
    # Time span for each simulation and set limits for the image axes
    with pytest.raises(TypeError) as excinfo:
        t_start = 1000
        t_end = 2000
        x_start = -2.0
        x_end = 2.0
        y_start = -2.0
        y_end = 2.0


        # Set number of CPU cores to use
        config.CORES = 1

        # System name
        system = 'test_sys'

        # Basin image size
        pixels = 3

        t_range = [t_start, t_end]
        limits = np.array([x_start, x_end, y_start, y_end, pixels])

        # Specify features and folders to be created (Key is used in the image titles)
        keys = [r'$\bar{x}$']
        folders = ['mean']

        # Set image axes labels
        labels = [r'$x_0$',r'$\dot{x}_0$']

        # Pack the folder names, image title, and axes labels into one list
        feat = [folders, keys, labels]

        # Setup the folder structure for saving the images
        folder_setup.folder_setup(folders, system)

        # Dictionary of parameter values. Use the variable pixels to control basin variables
        # NOTE: The basin plot parameters must be last
        variables = {
            'Row': [1],
            'd': [0.15],
            'alpha': [-1.0],
            'xo': np.linspace(x_start, x_end, pixels),
            'yo': np.linspace(y_start, y_end, pixels),
        }

        # Create the vectorized parameter mesh for the variables
        mesh = parameter_mesh.create_mesh(variables)

        # Extract the list of variables and parameters from the mesh
        variables = mesh[0]
        parameters = mesh[1]
        generate_basin.generatebasin(parameters, t_range, limits, feat, system)

    assert "limits needs to be a list." in str(excinfo.value)

def test_bad_limits_length():
    # test if function creates the csv file of parameters
    # Time span for each simulation and set limits for the image axes
    with pytest.raises(ValueError) as excinfo:
        t_start = 1000
        t_end = 2000
        x_start = -2.0
        x_end = 2.0
        y_start = -2.0
        y_end = 2.0


        # Set number of CPU cores to use
        config.CORES = 1

        # System name
        system = 'test_sys'

        # Basin image size
        pixels = 3

        t_range = [t_start, t_end]
        limits = [x_start, x_end, y_start, y_end]

        # Specify features and folders to be created (Key is used in the image titles)
        keys = [r'$\bar{x}$']
        folders = ['mean']

        # Set image axes labels
        labels = [r'$x_0$',r'$\dot{x}_0$']

        # Pack the folder names, image title, and axes labels into one list
        feat = [folders, keys, labels]

        # Setup the folder structure for saving the images
        folder_setup.folder_setup(folders, system)

        # Dictionary of parameter values. Use the variable pixels to control basin variables
        # NOTE: The basin plot parameters must be last
        variables = {
            'Row': [1],
            'd': [0.15],
            'alpha': [-1.0],
            'xo': np.linspace(x_start, x_end, pixels),
            'yo': np.linspace(y_start, y_end, pixels),
        }

        # Create the vectorized parameter mesh for the variables
        mesh = parameter_mesh.create_mesh(variables)

        # Extract the list of variables and parameters from the mesh
        variables = mesh[0]
        parameters = mesh[1]
        generate_basin.generatebasin(parameters, t_range, limits, feat, system)

    assert "limits should contain x_start, x_end, y_start, y_end, and number of pixels." in str(excinfo.value)

def test_bad_feat_type():
    # test if function creates the csv file of parameters
    # Time span for each simulation and set limits for the image axes
    with pytest.raises(TypeError) as excinfo:
        t_start = 1000
        t_end = 2000
        x_start = -2.0
        x_end = 2.0
        y_start = -2.0
        y_end = 2.0


        # Set number of CPU cores to use
        config.CORES = 1

        # System name
        system = 'test_sys'

        # Basin image size
        pixels = 3

        t_range = [t_start, t_end]
        limits = [x_start, x_end, y_start, y_end, pixels]

        # Specify features and folders to be created (Key is used in the image titles)
        keys = [r'$\bar{x}$']
        folders = ['mean']

        # Set image axes labels
        labels = [r'$x_0$',r'$\dot{x}_0$']

        # Pack the folder names, image title, and axes labels into one list
        feat = 10

        # Setup the folder structure for saving the images
        folder_setup.folder_setup(folders, system)

        # Dictionary of parameter values. Use the variable pixels to control basin variables
        # NOTE: The basin plot parameters must be last
        variables = {
            'Row': [1],
            'd': [0.15],
            'alpha': [-1.0],
            'xo': np.linspace(x_start, x_end, pixels),
            'yo': np.linspace(y_start, y_end, pixels),
        }

        # Create the vectorized parameter mesh for the variables
        mesh = parameter_mesh.create_mesh(variables)

        # Extract the list of variables and parameters from the mesh
        variables = mesh[0]
        parameters = mesh[1]
        generate_basin.generatebasin(parameters, t_range, limits, feat, system)

    assert "feat needs to be a list." in str(excinfo.value)

def test_bad_feat_length():
    # test if function creates the csv file of parameters
    # Time span for each simulation and set limits for the image axes
    with pytest.raises(ValueError) as excinfo:
        t_start = 1000
        t_end = 2000
        x_start = -2.0
        x_end = 2.0
        y_start = -2.0
        y_end = 2.0


        # Set number of CPU cores to use
        config.CORES = 1

        # System name
        system = 'test_sys'

        # Basin image size
        pixels = 3

        t_range = [t_start, t_end]
        limits = [x_start, x_end, y_start, y_end, pixels]

        # Specify features and folders to be created (Key is used in the image titles)
        keys = [r'$\bar{x}$']
        folders = ['mean']

        # Set image axes labels
        labels = [r'$x_0$',r'$\dot{x}_0$']

        # Pack the folder names, image title, and axes labels into one list
        feat = [folders, keys, labels, labels]

        # Setup the folder structure for saving the images
        folder_setup.folder_setup(folders, system)

        # Dictionary of parameter values. Use the variable pixels to control basin variables
        # NOTE: The basin plot parameters must be last
        variables = {
            'Row': [1],
            'd': [0.15],
            'alpha': [-1.0],
            'xo': np.linspace(x_start, x_end, pixels),
            'yo': np.linspace(y_start, y_end, pixels),
        }

        # Create the vectorized parameter mesh for the variables
        mesh = parameter_mesh.create_mesh(variables)

        # Extract the list of variables and parameters from the mesh
        variables = mesh[0]
        parameters = mesh[1]
        generate_basin.generatebasin(parameters, t_range, limits, feat, system)

    assert "feat should contain a folder list, a key list, and axes labels." in str(excinfo.value)

def test_bad_feat_item_type():
    # test if function creates the csv file of parameters
    # Time span for each simulation and set limits for the image axes
    with pytest.raises(TypeError) as excinfo:
        t_start = 1000
        t_end = 2000
        x_start = -2.0
        x_end = 2.0
        y_start = -2.0
        y_end = 2.0


        # Set number of CPU cores to use
        config.CORES = 1

        # System name
        system = 'test_sys'

        # Basin image size
        pixels = 3

        t_range = [t_start, t_end]
        limits = [x_start, x_end, y_start, y_end, pixels]

        # Specify features and folders to be created (Key is used in the image titles)
        keys = [r'$\bar{x}$']
        folders = ['mean']

        # Set image axes labels
        labels = [r'$x_0$',r'$\dot{x}_0$']

        # Pack the folder names, image title, and axes labels into one list
        feat = [1,2,3]

        # Setup the folder structure for saving the images
        folder_setup.folder_setup(folders, system)

        # Dictionary of parameter values. Use the variable pixels to control basin variables
        # NOTE: The basin plot parameters must be last
        variables = {
            'Row': [1],
            'd': [0.15],
            'alpha': [-1.0],
            'xo': np.linspace(x_start, x_end, pixels),
            'yo': np.linspace(y_start, y_end, pixels),
        }

        # Create the vectorized parameter mesh for the variables
        mesh = parameter_mesh.create_mesh(variables)

        # Extract the list of variables and parameters from the mesh
        variables = mesh[0]
        parameters = mesh[1]
        generate_basin.generatebasin(parameters, t_range, limits, feat, system)

    assert "One or more items in feat is/are not of type list." in str(excinfo.value)

def test_bad_labels_length():
    # test if function creates the csv file of parameters
    # Time span for each simulation and set limits for the image axes
    with pytest.raises(ValueError) as excinfo:
        t_start = 1000
        t_end = 2000
        x_start = -2.0
        x_end = 2.0
        y_start = -2.0
        y_end = 2.0


        # Set number of CPU cores to use
        config.CORES = 1

        # System name
        system = 'test_sys'

        # Basin image size
        pixels = 3

        t_range = [t_start, t_end]
        limits = [x_start, x_end, y_start, y_end, pixels]

        # Specify features and folders to be created (Key is used in the image titles)
        keys = [r'$\bar{x}$']
        folders = ['mean']

        # Set image axes labels
        labels = [r'$x_0$',r'$\dot{x}_0$','t']

        # Pack the folder names, image title, and axes labels into one list
        feat = [folders, keys, labels]

        # Setup the folder structure for saving the images
        folder_setup.folder_setup(folders, system)

        # Dictionary of parameter values. Use the variable pixels to control basin variables
        # NOTE: The basin plot parameters must be last
        variables = {
            'Row': [1],
            'd': [0.15],
            'alpha': [-1.0],
            'xo': np.linspace(x_start, x_end, pixels),
            'yo': np.linspace(y_start, y_end, pixels),
        }

        # Create the vectorized parameter mesh for the variables
        mesh = parameter_mesh.create_mesh(variables)

        # Extract the list of variables and parameters from the mesh
        variables = mesh[0]
        parameters = mesh[1]
        generate_basin.generatebasin(parameters, t_range, limits, feat, system)

    assert "labels should contain the x and y labels only." in str(excinfo.value)

def test_bad_system_type():
    # test if function creates the csv file of parameters
    # Time span for each simulation and set limits for the image axes
    with pytest.raises(TypeError) as excinfo:
        t_start = 1000
        t_end = 2000
        x_start = -2.0
        x_end = 2.0
        y_start = -2.0
        y_end = 2.0


        # Set number of CPU cores to use
        config.CORES = 1

        # System name
        system = 'test_sys'

        # Basin image size
        pixels = 3

        t_range = [t_start, t_end]
        limits = [x_start, x_end, y_start, y_end, pixels]

        # Specify features and folders to be created (Key is used in the image titles)
        keys = [r'$\bar{x}$']
        folders = ['mean']

        # Set image axes labels
        labels = [r'$x_0$',r'$\dot{x}_0$']

        # Pack the folder names, image title, and axes labels into one list
        feat = [folders, keys, labels]

        # Setup the folder structure for saving the images
        folder_setup.folder_setup(folders, system)

        # Dictionary of parameter values. Use the variable pixels to control basin variables
        # NOTE: The basin plot parameters must be last
        variables = {
            'Row': [1],
            'd': [0.15],
            'alpha': [-1.0],
            'xo': np.linspace(x_start, x_end, pixels),
            'yo': np.linspace(y_start, y_end, pixels),
        }

        # Create the vectorized parameter mesh for the variables
        mesh = parameter_mesh.create_mesh(variables)

        # Extract the list of variables and parameters from the mesh
        variables = mesh[0]
        parameters = mesh[1]
        system = 20
        generate_basin.generatebasin(parameters, t_range, limits, feat, system)

    assert "system should be a string." in str(excinfo.value)

def test_timeseries_error():
    with pytest.raises(RuntimeError) as excinfo:
        # test if function creates the csv file of parameters
        # Time span for each simulation and set limits for the image axes
        t_start = 1000
        t_end = 2000
        x_start = -2.0
        x_end = 2.0
        y_start = -2.0
        y_end = 2.0


        # Set number of CPU cores to use
        config.CORES = 1

        # System name
        system = 'test_sys'

        # Basin image size
        pixels = 3

        t_range = [t_start, t_end]
        limits = [x_start, x_end, y_start, y_end, pixels]

        # Specify features and folders to be created (Key is used in the image titles)
        keys = [r'$\bar{x}$']
        folders = ['mean']

        # Set image axes labels
        labels = [r'$x_0$',r'$\dot{x}_0$']

        # Pack the folder names, image title, and axes labels into one list
        feat = [folders, keys, labels]

        # Setup the folder structure for saving the images
        folder_setup.folder_setup(folders, system)

        # Dictionary of parameter values. Use the variable pixels to control basin variables
        # NOTE: The basin plot parameters must be last
        variables = {
            'Row': [1],
            'd': [0.15],
            'alpha': [-1.0],
            'xo': np.linspace(x_start, x_end, pixels),
            'yo': np.linspace(y_start, y_end, pixels),
        }

        # Create the vectorized parameter mesh for the variables
        mesh = parameter_mesh.create_mesh(variables)

        # Extract the list of variables and parameters from the mesh
        variables = mesh[0]
        parameters = mesh[1]
        generate_basin.generatebasin(parameters, t_range, limits, feat, system, timeseries=10)

    assert "Experimental timeseries are not supported yet but will be added in a future update." in str(excinfo.value)






  
    

    