"""
Import all functions needed in ds_featurizer
"""

import os
import warnings
# Create systems folder if it doesn't exist
if not os.path.exists(os.path.join(os.getcwd(), 'systems')):
        os.mkdir('systems')
        warnings.warn('Systems folder is empty. Add system code to import.')

# Install required julia libraries
from juliacall import Main as jl
jl.seval("using Pkg")

if not jl.seval("\"DifferentialEquations\" in keys(Pkg.project().dependencies)"):
    print("Installing Julia DifferentialEquations library. This may take some time.")
    jl.seval("Pkg.add(\"DifferentialEquations\")")

if not jl.seval("\"Polynomials\" in keys(Pkg.project().dependencies)"):
    print("Installing Julia Polynomials library. This may take some time.")
    jl.seval("Pkg.add(\"Polynomials\")")
    
if not jl.seval("\"DelayDiffEq\" in keys(Pkg.project().dependencies)"):
    print("Installing Julia Delay Differential Equations library. This may take some time.")
    jl.seval("Pkg.add(\"DelayDiffEq\")")
    

import ds_featurizer.config
import ds_featurizer.generate_basin
import ds_featurizer.parameter_mesh
import ds_featurizer.folder_setup
