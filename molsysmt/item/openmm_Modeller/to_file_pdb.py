from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *

def to_file_pdb(item, atom_indices='all', structure_indices='all', output_filename=None):

    if check:

        digest_item(item, 'openmm.Modeller')
        atom_indices = digest_atom_indices(atom_indices)
        structure_indices = digest_structure_indices(structure_indices)

    if output_filename is None:
        raise ValueError

    from . import to_openmm_Topology
    from . import get_coordinates_from_atom
    from ..openmm_Topology import to_file_pdb as openmm_Topology_to_file_pdb

    tmp_item = to_openmm_Topology(item, atom_indices=atom_indices, structure_indices=structure_indices)
    coordinates = get_coordinates_from_atom(item, atom_indices=atom_indices, structure_indices=structure_indices)
    tmp_item = openmm_Topology_to_file_pdb(tmp_item, coordinates=coordinates, output_filename=output_filename)

    return tmp_item

