"""
Generate a vectorized mesh of parameter combinations based on the parameters dictionary.
"""

import os.path
import numpy as np
from ds_featurizer import config

def create_mesh(variables):
    """
    Generate a vectorized mesh of parameter combinations based on the parameters dictionary.
    Args:
        parameters -- Dictionary of parameter key value pairs
    """
    if type(variables) != dict:
        raise TypeError("Input should be a dictionary.")
    
    for v in variables:
        if type(v) != str:
            raise TypeError(f"variable {v} should be a string.")
        if (type(variables[v]) != list) and (type(variables[v]) != np.ndarray):
            raise TypeError(f"variable {v} values should be a list or array.")

    iterations = 1
    arr = []
    var_list = []
    # Account for arbitrary number of variables
    for item in variables:
        iterations *= len(variables[item])
        arr.append(variables[item])
        var_list.append(item)
    
    # Create a vectorized grid of parameters
    grid = np.meshgrid(*arr, indexing='xy')
    points = []

    # Flatten grid and create array of points with one index
    for i, item in enumerate(grid):
        points.append(item.flatten())
    points = np.array(points)


    # Store coordinates back in original dictionary
    for i, variable in enumerate(variables):
        variables[variable] = points[i]
    del item, i, arr, grid, variable

    # Store list of parameters
    parameters = np.vstack([var_list, np.transpose(np.round(points,2))])
    
    # Store list of variable names
    variables = parameters[0,:]
    parameters = np.delete(parameters, 0, axis=0)
    parameters = parameters.astype(float)
    
    # Set the row numbers as the first column of the parameters
    iterations = len(parameters)
    row = np.linspace(1, iterations, num=iterations)
    parameters[:,0] = row
    
    # Load the system name
    if os.path.exists(os.path.join(os.getcwd(),'system.npy')):
        system = str(np.load('system.npy'))
    else:
        raise RuntimeError("Run folder_setup before creating the parameter mesh.")
    
    # Save the parameters as a csv and temporary individual numpy arrays
    
    path_np = os.path.join(os.getcwd(),os.path.join('Basin_'+system, 'parameter_arrays'))
    for param in parameters:
        np.save(os.path.join(path_np, str(int(param[0])) + '.npy'), param)
    
    # Return the list of variables and parameters
    return [variables, parameters]
