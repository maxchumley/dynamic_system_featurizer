"""
Import the parameter mesh, call the simulation functions, and save the basin images
"""
import time
import os
import shutil
import numpy as np
from ds_featurizer.parallel_sim import parallel_sims
from ds_featurizer.save_basins import save_basins

def generatebasin(parameters, variables, t_range, limits, feat, system, timeseries=0):
    """
    Import the parameter mesh, call the simulation functions, and save the basin images
    Args:
        parameters -- One set of system parameters to simulate.
        t_range -- List containing start and end time for simulations
        limits -- List containing x_min, x_max, y_min, y_max, and number of pixels for basins
        feat -- List containing folder names, feature labels, and axis labels
        system -- String containing the system name
        timeseries -- Timeseries data from experiments (optional)
    """
    
    if type(parameters) != np.ndarray:
        raise TypeError("parameters needs to be a numpy array.")
    
    if type(t_range) != list:
        raise TypeError("t_range needs to be a list.")
    if len(t_range) != 2:
        raise ValueError("t_range should contain only t_start and t_end.")
    if type(limits) != list:
        raise TypeError("limits needs to be a list.")
    if len(limits) != 5:
        raise ValueError("limits should contain x_start, x_end, y_start, y_end, and number of pixels.")
    if type(feat) != list:
        raise TypeError("feat needs to be a list.")
    if len(feat) != 3:
            raise ValueError("feat should contain a folder list, a key list, and axes labels.")
    for item in feat:
        if type(item) != list:
            raise TypeError("One or more items in feat is/are not of type list.")
    if len(feat[2]) != 2:
        raise ValueError("labels should contain the x and y labels only.")
    if type(system) != str:
        raise TypeError("system should be a string.")

    init_params = []
    if timeseries == 0:
        for basin_num in range(int(len(parameters)/limits[4]**2)):
            print(f'Generating image {basin_num+1}...')
            init_params.append(np.copy(parameters[0+(basin_num*limits[4]**2):((basin_num+1)*limits[4]**2)][0][0:-2]))
            init_params[basin_num][0] = basin_num + 1
            res = np.array(
                parallel_sims(parameters[0+(basin_num*limits[4]**2):((basin_num+1)*limits[4]**2)], variables,
                    t_range, feat))
            basins = [0]*res.shape[1]

            for c_n, col in enumerate(res.T):
                basins[c_n] = col.reshape(-1, limits[4]**2)

            row=0
            feature=0
            for j, feature in enumerate(basins):
                for row in feature:
                    basin = np.transpose(np.reshape(row, (limits[4], limits[4])))
                    r_num = int(parameters[basin_num * limits[4] ** 2, 0])
                    save_basins(basin, [basin_num, r_num], [feat[0][j], feat[1][j]],
                                limits, feat[2], system)
            del row, res, feature, basins, basin
            time.sleep(5)
            
        path_csv = os.path.join(os.getcwd(),os.path.join('Basin_'+system, 'parameters.csv'))
        np.savetxt(path_csv, np.vstack([variables[0:-2], init_params]), delimiter=",", fmt='%s')
        # Remove the temporary parameter numpy files
        if os.path.exists(os.path.join(os.getcwd(),os.path.join('Basin_'+system, '.parameter_arrays'))):
            shutil.rmtree(os.path.join(os.getcwd(), os.path.join('Basin_'+system,'.parameter_arrays')))
    else:
        raise RuntimeError("Experimental timeseries are not supported yet but will be added in a future update.")
