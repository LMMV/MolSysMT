from molsysmt._private.exceptions import LibraryNotFoundError
from molsysmt._private.digestion import digest_item, digest_atom_indices, digest_structure_indices

def to_pytraj_Trajectory(item, atom_indices='all', structure_indices='all', check=True):

    if check:

        digest_item(item, 'file:pdb')
        atom_indices = digest_atom_indices(atom_indices)
        structure_indices = digest_structure_indices(structure_indices)

    try:
        from pytraj import load
    except:
        raise LibraryNotFoundError('pytraj')

    from ..pytraj_Trajectory import extract as extract_pytraj_Trajectory

    tmp_item = load(item)
    tmp_item = extract_pytraj_Trajectory(tmp_item, atom_indices=atom_indices, structure_indices=structure_indices,
            copy_if_all=False, check=False)

    return tmp_item

