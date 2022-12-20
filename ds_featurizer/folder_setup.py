"""
Create the folder structure required to save the basin images.
"""
import os
import shutil
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from ds_featurizer import config


def folder_setup(folders, system):
    """
    Create the folder structure for saving the basins.
    Args:
        folders -- List containing folder names to be created. 
        system -- String containing the system name.
    """
    if type(folders) != list:
        raise TypeError("folders needs to be a list.")
    if type(system) != str:
        raise TypeError("system needs to be a string.")
    for fol in folders:
        if type(fol) != str:
            raise TypeError(f"{fol} in folders is not a string.")

    if not os.path.exists(os.path.join(os.getcwd(), 'systems')):
        os.mkdir('systems')


    # Create a folder for the specific system
    if not os.path.exists(os.path.join(os.getcwd(), 'Basin_'+system)):
        os.mkdir('Basin_'+system)

    # Create folders for the features being computed
    for folder in folders:
        if not os.path.exists(os.path.join(os.getcwd(), os.path.join('Basin_'+system,folder))):
            os.mkdir(os.path.join(os.getcwd(), os.path.join('Basin_'+system,folder)))
    
    # Create a temporary folder to store the individual parameter numpy arrays and remove it first if one exists already.
    if not os.path.exists(os.path.join(os.getcwd(), os.path.join('Basin_'+system, 'parameter_arrays'))):
        os.mkdir(os.path.join(os.getcwd(), os.path.join('Basin_'+system,'parameter_arrays')))
    else:
        shutil.rmtree(os.path.join(os.getcwd(), os.path.join('Basin_'+system,'parameter_arrays')))
        os.mkdir(os.path.join(os.getcwd(), os.path.join('Basin_'+system,'parameter_arrays')))
    
    # Save the system name as a numpy array for the simulation functions to access 
    if os.path.exists('system.npy'):
        os.remove('system.npy')
    np.save('system.npy', system)