from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *
from molsysmt._private.variables import is_all
import numpy as np

def get_component_name_from_component(molecular_system, indices='all'):

    if check:

        digest_single_molecular_system(molecular_system)
        indices = digest_indices(indices)

    if is_all(indices):

        from . import get_n_components_from_system
        n_components = get_n_components_from_system(molecular_system, check=False)
        output = np.full(n_components, None, dtype=object)

    else:

        output = np.full(indices.shape[0], None, dtype=object)

    return output

