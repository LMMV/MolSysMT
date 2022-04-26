#######################################################################################
########### THE FOLLOWING LINES NEED TO BE CUSTOMIZED FOR EVERY CLASS  ################
#######################################################################################

from molsysmt._private.execfile import execfile
from molsysmt._private.exceptions import NotWithThisFormError as _NotWithThisFormError
from molsysmt._private.exceptions import NotImplementedMethodError as _NotImplementedMethodError
from molsysmt._private.digestion import digest_item as _digest_item
from molsysmt._private.digestion import digest_indices as _digest_indices
from molsysmt._private.digestion import digest_structure_indices as _digest_structure_indices
from molsysmt import puw as _puw
import numpy as _np
from networkx import Graph as _Graph

_form='mdtraj.HDF5TrajectoryFile'

## From atom

def get_atom_id_from_atom(item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_atom_id_from_atom as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_atom_name_from_atom(item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_atom_name_from_atom as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_atom_type_from_atom(item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_atom_type_from_atom as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_group_index_from_atom (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_group_index_from_atom as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_component_index_from_atom (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_component_index_from_atom as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_chain_index_from_atom (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_chain_index_from_atom as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_molecule_index_from_atom (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_molecule_index_from_atom as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_entity_index_from_atom (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_entity_index_from_atom as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_inner_bonded_atoms_from_atom (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_inner_bonded_atoms_from_atom as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_n_inner_bonds_from_atom (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_n_inner_bonds_from_atom as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, structure_indices=structure_indices, check=False)

    return output

def get_coordinates_from_atom(item, indices='all', structure_indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)
        structure_indices = _digest_structure_indices(structure_indices)

    from molsysmt._private.math import serie_to_chunks

    if structure_indices is 'all':
        structure_indices = _np.arange(get_n_structures_from_system(item))
    if indices is 'all':
        indices = _np.arange(get_n_atoms_from_system(item))

    starts_serie_frames, size_serie_frames = serie_to_chunks(structure_indices)

    xyz_list = []

    for start, size in zip(starts_serie_frames, size_serie_frames):
        item.seek(start)
        frame_hdf5 = item.read(n_frames=size, atom_indices=indices)
        xyz = frame_hdf5.coordinates
        xyz_list.append(xyz)

    xyz = _np.concatenate(xyz_list)
    del(xyz_list)

    xyz = xyz.astype('float64')

    xyz = xyz*_puw.unit('nm')
    xyz = _puw.standardize(xyz)

    return xyz

## group

def get_group_id_from_group(item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_group_id_from_group as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_group_name_from_group(item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_group_name_from_group as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_group_type_from_group(item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_group_type_from_group as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

## component

def get_component_id_from_component (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_component_id_from_component as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_component_name_from_component (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_component_name_from_component as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_component_type_from_component (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_component_type_from_component as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

## molecule

def get_molecule_id_from_molecule (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_molecule_id_from_molecule as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_molecule_name_from_molecule (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_molecule_name_from_molecule as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_molecule_type_from_molecule (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_molecule_type_from_molecule as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

## chain

def get_chain_id_from_chain (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_chain_id_from_chain as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_chain_name_from_chain (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_chain_name_from_chain as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_chain_type_from_chain (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_chain_type_from_chain as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

## entity

def get_entity_id_from_entity (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_entity_id_from_entity as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_entity_name_from_entity (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_entity_name_from_entity as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

def get_entity_type_from_entity (item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_entity_type_from_entity as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, indices=indices, check=False)

    return output

## system

def get_n_atoms_from_system(item, check=True):

    if check:

        _digest_item(item, _form)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_n_atoms_from_system as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, check=False)

    return output

def get_n_groups_from_system(item, check=True):

    if check:

        _digest_item(item, _form)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_n_groups_from_system as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, check=False)

    return output

def get_n_components_from_system(item, check=True):

    if check:

        _digest_item(item, _form)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_n_components_from_system as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, check=False)

    return output

def get_n_chains_from_system(item, check=True):

    if check:

        _digest_item(item, _form)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_n_chains_from_system as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, check=False)

    return output

def get_n_molecules_from_system(item, check=True):

    if check:

        _digest_item(item, _form)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_n_molecules_from_system as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, check=False)

    return output

def get_n_entities_from_system(item, check=True):

    if check:

        _digest_item(item, _form)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_n_entities_from_system as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, check=False)

    return output

def get_n_bonds_from_system(item, check=True):

    if check:

        _digest_item(item, _form)

    from . import to_mdtraj_Topology
    from ..mdtraj_Topology import get_n_bonds_from_system as aux_get

    tmp_item = to_mdtraj_Topology(item, check=False)
    output = aux_get(tmp_item, check=False)

    return output

def get_box_from_system(item, structure_indices='all', check=True):

    if check:

        _digest_item(item, _form)
        structure_indices = _digest_structure_indices(structure_indices)

    from molsysmt._private.math import serie_to_chunks
    from molsysmt.pbc import box_vectors_from_box_lengths_and_angles

    if structure_indices is 'all':
        structure_indices = _np.arange(get_n_structures_from_system(item))

    starts_serie_frames, size_serie_frames = serie_to_chunks(structure_indices)

    box_list = []

    for start, size in zip(starts_serie_frames, size_serie_frames):
        item.seek(start)
        frame_hdf5 = item.read(n_frames=size)
        cell_lengths = frame_hdf5.cell_lengths
        cell_angles = frame_hdf5.cell_angles
        box = box_vectors_from_box_lengths_and_angles(cell_lengths*_puw.unit('nm'), cell_angles*_puw.unit('degrees'))
        box_list.append(_puw.get_value(box))

    box = _np.concatenate(box_list)
    del(box_list)

    box = box.astype('float64')

    box = box*_puw.unit('nm')
    box = _puw.standardize(box)

    return box

def get_time_from_system(item, structure_indices='all', check=True):

    if check:

        _digest_item(item, _form)
        structure_indices = _digest_structure_indices(structure_indices)

    from molsysmt._private.math import serie_to_chunks

    if structure_indices is 'all':
        structure_indices = _np.arange(get_n_structures_from_system(item))

    starts_serie_frames, size_serie_frames = serie_to_chunks(structure_indices)

    time_list = []

    for start, size in zip(starts_serie_frames, size_serie_frames):
        item.seek(start)
        frame_hdf5 = item.read(n_frames=size)
        time = frame_hdf5.time
        time_list.append(time)

    time = _np.concatenate(time_list)
    del(time_list)

    time = time.astype('float64')

    time = time*_puw.unit('ps')
    time = _puw.standardize(time)

    return time

def get_step_from_system(item, structure_indices='all', check=True):

    if check:

        _digest_item(item, _form)
        structure_indices = _digest_structure_indices(structure_indices)

    return None

def get_n_structures_from_system(item, check=True):

    if check:

        _digest_item(item, _form)

    return item._handle.root.coordinates.shape[0]

def get_bonded_atoms_from_system(item, check=True):

    if check:

        _digest_item(item, _form)

    raise NotImplementedError

## bond

def get_bond_order_from_bond(item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    raise NotImplementedError

def get_bond_type_from_bond(item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    raise NotImplementedError

def get_atom_index_from_bond(item, indices='all', check=True):

    if check:

        _digest_item(item, _form)
        indices = _digest_indices(indices)

    raise NotImplementedError

#######################################################################################
######### DO NOT TOUCH THE FOLLOWING LINES, JUST INCLUDE THEM AS THEY ARE #############
#######################################################################################

from os import path
this_folder = path.dirname(path.abspath(__file__))
common_get = path.join(this_folder, '../../_private/common_get.py')
execfile(common_get, globals(), locals())
del(path, this_folder, common_get)

#######################################################################################
############## REMOVE COMMON GET METHODS NOT DEFINED FOR THIS FORM ####################
#######################################################################################

del(

    # From atom
    #get_atom_index_from_atom,
    #get_group_id_from_atom,
    #get_group_name_from_atom,
    #get_group_type_from_atom,
    #get_component_id_from_atom,
    #get_component_name_from_atom,
    #get_component_type_from_atom,
    #get_chain_id_from_atom,
    #get_chain_name_from_atom,
    #get_chain_type_from_atom,
    #get_molecule_id_from_atom,
    #get_molecule_name_from_atom,
    #get_molecule_type_from_atom,
    #get_entity_id_from_atom,
    #get_entity_name_from_atom,
    #get_entity_type_from_atom,
    #get_n_atoms_from_atom,
    #get_n_groups_from_atom,
    #get_n_components_from_atom,
    #get_n_molecules_from_atom,
    #get_n_chains_from_atom,
    #get_n_entities_from_atom,
    #get_bonded_atoms_from_atom,
    #get_bond_index_from_atom,
    #get_n_bonds_from_atom,
    #get_inner_bond_index_from_atom,

    # From group
    #get_atom_index_from_group,
    #get_atom_id_from_group,
    #get_atom_name_from_group,
    #get_atom_type_from_group,
    #get_group_index_from_group,
    #get_component_index_from_group,
    #get_component_id_from_group,
    #get_component_name_from_group,
    #get_component_type_from_group,
    #get_chain_index_from_group,
    #get_chain_id_from_group,
    #get_chain_name_from_group,
    #get_chain_type_from_group,
    #get_molecule_index_from_group,
    #get_molecule_id_from_group,
    #get_molecule_name_from_group,
    #get_molecule_type_from_group,
    #get_entity_index_from_group,
    #get_entity_id_from_group,
    #get_entity_name_from_group,
    #get_entity_type_from_group,
    #get_n_atoms_from_group,
    #get_n_groups_from_group,
    #get_n_components_from_group,
    #get_n_molecules_from_group,
    #get_n_chains_from_group,
    #get_n_entities_from_group,

    # From component
    #get_atom_index_from_component,
    #get_atom_id_from_component,
    #get_atom_name_from_component,
    #get_atom_type_from_component,
    #get_group_index_from_component,
    #get_group_id_from_component,
    #get_group_name_from_component,
    #get_group_type_from_component,
    #get_component_index_from_component,
    #get_chain_index_from_component,
    #get_chain_id_from_component,
    #get_chain_name_from_component,
    #get_chain_type_from_component,
    #get_molecule_index_from_component,
    #get_molecule_id_from_component,
    #get_molecule_name_from_component,
    #get_molecule_type_from_component,
    #get_entity_index_from_component,
    #get_entity_id_from_component,
    #get_entity_name_from_component,
    #get_entity_type_from_component,
    #get_n_atoms_from_component,
    #get_n_groups_from_component,
    #get_n_components_from_component,
    #get_n_molecules_from_component,
    #get_n_chains_from_component,
    #get_n_entities_from_component,

    # From molecule
    #get_atom_index_from_molecule,
    #get_atom_id_from_molecule,
    #get_atom_name_from_molecule,
    #get_atom_type_from_molecule,
    #get_group_index_from_molecule,
    #get_group_id_from_molecule,
    #get_group_name_from_molecule,
    #get_group_type_from_molecule,
    #get_component_index_from_molecule,
    #get_component_id_from_molecule,
    #get_component_name_from_molecule,
    #get_component_type_from_molecule,
    #get_chain_index_from_molecule,
    #get_chain_id_from_molecule,
    #get_chain_name_from_molecule,
    #get_chain_type_from_molecule,
    #get_molecule_index_from_molecule,
    #get_entity_index_from_molecule,
    #get_entity_id_from_molecule,
    #get_entity_name_from_molecule,
    #get_entity_type_from_molecule,
    #get_n_atoms_from_molecule,
    #get_n_groups_from_molecule,
    #get_n_components_from_molecule,
    #get_n_molecules_from_molecule,
    #get_n_chains_from_molecule,
    #get_n_entities_from_molecule,

    # From chain
    #get_atom_index_from_chain,
    #get_atom_id_from_chain,
    #get_atom_name_from_chain,
    #get_atom_type_from_chain,
    #get_group_index_from_chain,
    #get_group_id_from_chain,
    #get_group_name_from_chain,
    #get_group_type_from_chain,
    #get_component_index_from_chain,
    #get_component_id_from_chain,
    #get_component_name_from_chain,
    #get_component_type_from_chain,
    #get_chain_index_from_chain,
    #get_molecule_index_from_chain,
    #get_molecule_id_from_chain,
    #get_molecule_name_from_chain,
    #get_molecule_type_from_chain,
    #get_entity_index_from_chain,
    #get_entity_id_from_chain,
    #get_entity_name_from_chain,
    #get_entity_type_from_chain,
    #get_n_atoms_from_chain,
    #get_n_groups_from_chain,
    #get_n_components_from_chain,
    #get_n_molecules_from_chain,
    #get_n_chains_from_chain,
    #get_n_entities_from_chain,

    # From entity
    #get_atom_index_from_entity,
    #get_atom_id_from_entity,
    #get_atom_name_from_entity,
    #get_atom_type_from_entity,
    #get_group_index_from_entity,
    #get_group_id_from_entity,
    #get_group_name_from_entity,
    #get_group_type_from_entity,
    #get_component_index_from_entity,
    #get_component_id_from_entity,
    #get_component_name_from_entity,
    #get_component_type_from_entity,
    #get_chain_index_from_entity,
    #get_chain_id_from_entity,
    #get_chain_name_from_entity,
    #get_chain_type_from_entity,
    #get_molecule_index_from_entity,
    #get_molecule_id_from_entity,
    #get_molecule_name_from_entity,
    #get_molecule_type_from_entity,
    #get_entity_index_from_entity,
    #get_n_atoms_from_entity,
    #get_n_groups_from_entity,
    #get_n_components_from_entity,
    #get_n_molecules_from_entity,
    #get_n_chains_from_entity,
    #get_n_entities_from_entity,

    # From system
    #get_n_aminoacids_from_system,
    #get_n_nucleotides_from_system,
    #get_n_ions_from_system,
    #get_n_waters_from_system,
    #get_n_cosolutes_from_system,
    #get_n_small_molecules_from_system,
    #get_n_peptides_from_system,
    #get_n_proteins_from_system,
    #get_n_dnas_from_system,
    #get_n_rnas_from_system,
    #get_n_lipids_from_system,
    #get_coordinates_from_system,
    #get_box_shape_from_system,
    #get_box_lengths_from_system,
    #get_box_angles_from_system,
    #get_box_volume_from_system,
    #get_bonded_atoms_from_system,
    #get_bond_index_from_system,
    #get_inner_bonded_atoms_from_system,
    #get_inner_bond_index_from_system,

    # From bond
    #get_bond_index_from_bond,
    #get_n_bonds_from_bond

    )

