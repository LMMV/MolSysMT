#######################################################################################
########### THE FOLLOWING LINES NEED TO BE CUSTOMIZED FOR EVERY CLASS  ################
#######################################################################################

from molsysmt._private.execfile import execfile
from molsysmt._private.exceptions import NotImplementedMethodError, NotWithThisFormError
from molsysmt._private.digestion import digest

form='file:h5'


## From atom

@digest(form=form)
def get_atom_id_from_atom(item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_atom_id_from_atom as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_atom_name_from_atom(item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_atom_name_from_atom as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_atom_type_from_atom(item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_atom_type_from_atom as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_group_index_from_atom (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_group_index_from_atom as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_component_index_from_atom (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_component_index_from_atom as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_chain_index_from_atom (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_chain_index_from_atom as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_molecule_index_from_atom (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_molecule_index_from_atom as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_entity_index_from_atom (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_entity_index_from_atom as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_inner_bonded_atoms_from_atom (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_inner_bonded_atoms_from_atom as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_n_inner_bonds_from_atom (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_n_inner_bonds_from_atom as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices, structure_indices=structure_indices)

    return output

@digest(form=form)
def get_coordinates_from_atom(item, indices='all', structure_indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_coordinates_from_atom as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices, structure_indices=structure_indices)

    return output


## group

@digest(form=form)
def get_group_id_from_group(item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_group_id_from_group as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_group_name_from_group(item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_group_name_from_group as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_group_type_from_group(item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_group_type_from_group as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output


## component

@digest(form=form)
def get_component_id_from_component (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_component_id_from_component as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_component_name_from_component (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_component_name_from_component as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_component_type_from_component (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_component_type_from_component as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output


## molecule

@digest(form=form)
def get_molecule_id_from_molecule (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_molecule_id_from_molecule as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_molecule_name_from_molecule (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_molecule_name_from_molecule as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_molecule_type_from_molecule (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_molecule_type_from_molecule as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output


## chain

@digest(form=form)
def get_chain_id_from_chain (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_chain_id_from_chain as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_chain_name_from_chain (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_chain_name_from_chain as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_chain_type_from_chain (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_chain_type_from_chain as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output


## entity

@digest(form=form)
def get_entity_id_from_entity (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_entity_id_from_entity as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_entity_name_from_entity (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_entity_name_from_entity as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_entity_type_from_entity (item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_entity_type_from_entity as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output


## system

@digest(form=form)
def get_n_atoms_from_system(item):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_n_atoms_from_system as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_groups_from_system(item):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_n_groups_from_system as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_components_from_system(item):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_n_components_from_system as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_chains_from_system(item):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_n_chains_from_system as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_molecules_from_system(item):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_n_molecules_from_system as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_entities_from_system(item):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_n_entities_from_system as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_bonds_from_system(item):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_n_bonds_from_system as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_n_structures_from_system(item):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_n_structures_from_system as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item)

    return output

@digest(form=form)
def get_box_from_system(item, structure_indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_box_from_system as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, structure_indices=structure_indices)

    return output

@digest(form=form)
def get_time_from_system(item, structure_indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_time_from_system as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, structure_indices=structure_indices)

    return output

@digest(form=form)
def get_step_from_system(item, structure_indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_step_from_system as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, structure_indices=structure_indices)

    return output


## bond

@digest(form=form)
def get_bond_order_from_bond(item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_bond_order_from_bond as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_bond_type_from_bond(item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_bond_type_from_bond as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output

@digest(form=form)
def get_atom_index_from_bond(item, indices='all'):

    from . import to_mdtraj_HDF5TrajectoryFile
    from ..mdtraj_HDF5TrajectoryFile import get_atom_index_from_bond as aux_get

    tmp_item = to_mdtraj_HDF5TrajectoryFile(item)
    output = aux_get(tmp_item, indices=indices)

    return output


#######################################################################################
######### DO NOT TOUCH THE FOLLOWING LINES, JUST INCLUDE THEM AS THEY ARE #############
#######################################################################################

from os import path
this_folder = path.dirname(path.abspath(__file__))
common_get = path.join(this_folder, '../../_private/common_get.py')
execfile(common_get, globals(), locals())
del(path, this_folder, common_get)

