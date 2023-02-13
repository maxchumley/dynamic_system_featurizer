"""
Module used to simulation julia system and compute response features.
"""
import numpy as np
from ripser import ripser
import os
from teaspoon.parameter_selection.delay_LMS import LMSforDelay


def features(data, times, feat='sd'):
    """
    Compute the data features.
    Args:
        data -- State space data from the simulations or experiments
        times -- Array of time values for the data points
        feat -- List of features to be computed and returned
    Returns:
        basin -- Array containing arrays for each basin computed to be saved as an image
    """
    if (type(data) != list) or (type(times) != np.ndarray) or (type(feat) != list):
        raise TypeError('One or more inputs to features is an incorrect type.')
    if (len(feat) <= 0) or (len(data) <= 0) or (len(times) <= 0):
        raise ValueError("One or more empty inputs to features.")
    if np.shape(times) != (len(times),):
        raise ValueError("Time array does not have the correct shape.")
    if np.shape(data) != (2, len(times)):
        raise ValueError("The simulation data is not the correct shape. Did you mean to transpose?")
    basin = []
    
    # Compute the requested features and append to the basin list
    if 'sd' in feat:
        stdev = np.sum(np.std(data, axis=1))
        basin.append(stdev)
    if 'mean' in feat:
        mean = np.sum(np.mean(data, axis=1))
        basin.append(mean)
    if 'maxh1' in feat:
        if len(data[0])>400:
            sample = int(len(data[0])/400)
        else:
            sample = 1
        subsampled = np.transpose(np.array(data))[::sample]
        diagrams = ripser(subsampled)['dgms']
        pairs = diagrams[1]
        if len(pairs) > 0:
            lifetimes = pairs[:, 1] - pairs[:, 0]
            basin_pers = np.max(lifetimes)
        else:
            basin_pers = 0
        basin.append(basin_pers) 
    return basin


def sim(p_num, variables, t_range, feat):
    """
    Run the julia simulation code from python and obtain the features of the data.
    Args:
        parameter -- List containing one set of parameters for a single simulation.
        t_range -- List containing start and end time for the simulation
    Returns:
        basin -- Output of features function
    """
    path = os.path.join(os.getcwd(), os.path.join('Basin_'+sys,'.parameter_arrays'))
    path = os.path.join(path, str(int(p_num))+'.npy')
    parameter = np.load(path)
    parameter = [float(i) for i in parameter]
    variables = [str(i) for i in variables]
    t_start = t_range[0]
    t_end = t_range[1]
    parameter = dict(zip(variables,parameter))
    sol = Main.trajectory(jl.convert(jl.PythonCall.Dict, parameter), t_start, t_end)
    sol = [sol[1], sol[2]]
    basin = features(sol, np.linspace(t_start, t_end, len(sol[0])), feat)
    return basin

if __name__ == '__main__':
    pass
else:
    from juliacall import Main
    import juliacall as jl
    if os.path.exists('system.npy'):
        sys = str(np.load('system.npy'))
        path = os.path.join(os.getcwd(), os.path.join('systems', sys+'.jl'))
        Main.include(path)
