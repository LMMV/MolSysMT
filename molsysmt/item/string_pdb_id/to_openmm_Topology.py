from molsysmt._private.exceptions import *
from molsysmt._private.digestion import *

def to_openmm_Topology(item, atom_indices='all', structure_indices='all'):

    if check:

        digest_item(item, 'string:pdb_id')
        atom_indices = digest_atom_indices(atom_indices)
        structure_indices = digest_structure_indices(structure_indices)

    from . import to_string_pdb_text
    from ..string_pdb_text import to_openmm_Modeller as string_pdb_text_to_openmm_Topology

    tmp_item = to_string_pdb_text(item, atom_indices=atom_indices, structure_indices=structure_indices)
    tmp_item = string_pdb_text_to_openmm_Topology(tmp_item)

    return tmp_item

