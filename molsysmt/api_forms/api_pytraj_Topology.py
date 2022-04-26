from molsysmt._private.exceptions import *
import numpy as np

from molsysmt.form.pytraj_Topology.is_pytraj_Topology import is_pytraj_Topology as is_form
from molsysmt.form.pytraj_Topology.extract import extract
from molsysmt.form.pytraj_Topology.add import add
from molsysmt.form.pytraj_Topology.append_structures import append_structures
from molsysmt.form.pytraj_Topology.get import *
from molsysmt.form.pytraj_Topology.set import *

form_name='pytraj.Topology'
form_type='class'
form_info=["",""]

form_attributes = {

    'atom_index' : True,
    'atom_id' : True,
    'atom_name' : True,
    'atom_type' : True,

    'bond_index' : True,
    'bond_id' : True,
    'bond_name' : True,
    'bond_type' : True,
    'bond_order' : True,

    'group_index' : True,
    'group_id' : True,
    'group_name' : True,
    'group_type' : True,

    'component_index' : True,
    'component_id' : False,
    'component_name' : False,
    'component_type' : False,

    'molecule_index' : True,
    'molecule_id' : True,
    'molecule_name' : True,
    'molecule_type' : True,

    'chain_index' : True,
    'chain_id' : True,
    'chain_name' : True,
    'chain_type' : True,

    'entity_index' : False,
    'entity_id' : False,
    'entity_name' : False,
    'entity_type' : False,

    'coordinates' : False,
    'velocities' : False,
    'box' : False,
    'time' : False,
    'step' : False,

    'forcefield' : False,
    'temperature' : False,
    'pressure' : False,
    'integrator' : False,
    'damping' : False,
}

def to_molsysmt_Topology(item, molecular_system, atom_indices='all', structure_indices='all'):

    from molsysmt.form.pytraj_Topology import to_molsysmt_Topology as pytraj_Topology_to_molsysmt_Topology

    tmp_item = pytraj_Topology_to_molsysmt_Topology(item, atom_indices=atom_indices, check=False)

    return tmp_item

