from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *

def to_molsysmt_TrajectoryDict(item, atom_indices='all', structure_indices='all', check=True):

    if check:

        digest_item(item, 'molsysmt.Structures')
        atom_indices = digest_atom_indices(atom_indices)
        structure_indices = digest_structure_indices(structure_indices)

    from . import get_coordinates_from_atom, get_step_from_system, get_time_from_system, get_box_from_system

    coordinates = get_coordinates_from_atom(item, indices=atom_indices, structure_indices=structure_indices, check=False)
    step = get_step_from_system(item, structure_indices=structure_indices, check=False)
    time = get_time_from_system(item, structure_indices=structure_indices, check=False)
    box = get_box_from_system(item, structure_indices=structure_indices, check=False)

    tmp_item = {}

    if step is not None:
        tmp_item['step']=step

    if time is not None:
        tmp_item['time']=time

    if coordinates is not None:
        tmp_item['coordinates']=coordinates

    if box is not None:
        tmp_item['box']=box

    return tmp_item

