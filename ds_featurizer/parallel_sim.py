"""
Function to distribute simulations over the cores of the cpu in parallel using multiprocessing.
"""

def parallel_sims(parameters, variables, t_range, feat):
    """
    Function to distribute simulations over the cores of the cpu in parallel using multiprocessing.
    Args:
        parameters -- Parameter mesh computed in generate_basin
        t_range -- List containing start and end time for simulations
        feat -- List containing the features to compute from each simulation
    Returns:
        res -- List of computed features for the simulation
    """
    # Load the number of cores and system name
    cores = config.CORES
    system = str(np.load('system.npy'))
    print(f'Simulating the {system} system using {cores} cores...')
    
    # Time the simulations
    start_time = time.time()
    
    # Distribute the parallel processes and print the progress bar
    with Pool(cores) as proc:
        res = list(tqdm.tqdm(proc.imap(sim_star,
                               list(zip(parameters[:,0], repeat(variables), repeat(t_range), repeat(feat[0])))),
                               total=len(parameters)))
    proc.close()
    # Print the simulation time
    end_time = time.time() - start_time
    print(f"Processing {len(parameters)} simulations took {end_time} seconds.")
    return res

def sim_star(row):
    """Unpack the rows for the parallel processes"""
    return simulation.sim(*row)



if __name__ == '__main__':
    pass
else:
    import time
    import numpy as np
    from multiprocessing import Pool
    import tqdm
    from itertools import repeat
    from ds_featurizer import simulation
    from ds_featurizer import config
