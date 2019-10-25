from os.path import basename as _basename
from simtk.openmm.app import Topology as _simtk_openmm_app_Topology

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    'openmm.topology':form_name,
    'openmm.Topology':form_name,
    'simtk.openmm.app.topology.Topology':form_name,
    _simtk_openmm_app_Topology:form_name
}

def to_molmod_Topology(item, atom_indices=None, frame_indices=None):

    from molmodmt.native.io_topology import from_openmm_Topology as _from_openmm_Topology
    return _from_openmm_Topology(item, atom_indices=atom_indices)

def to_mdtraj_Topology(item, atom_indices=None, frame_indices=None):

    from .api_mdtraj_Topology import extract_subsystem as extract_mdtraj_Topology
    from mdtraj.core.topology import Topology as mdtraj_Topology
    tmp_item = mdtraj_Topology.from_openmm(item)
    tmp_item = extract_mdtraj_Topology(tmp_item, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

def to_parmed_Structure(item, atom_indices=None, frame_indices=None):

    from parmed.openmm import load_topology as openmm_Topology_to_parmed_Structure
    tmp_item = extract_subsystem(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item = openmm_Topology_to_parmed_Structure(tmp_item)
    return tmp_item

def to_yank_Topography(item, atom_indices=None, frame_indices=None):

    from yank import Topography as yank_Topography
    tmp_item = extract_subsystem(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item = yank_Topography(tmp_item)
    return tmp_item

def extract_subsystem(item, atom_indices=None, frame_indices=None):

    if (atom_indices is None) and (frame_indices is None):
        return item
    else:

        from simtk.openmm.app import Topology
        atom_indices_to_be_kept = atom_indices
        newAtoms = {}
        set_atom_indices = set(atom_indices_to_be_kept)
        for chain in item.chains():
            needNewChain = True
            for residue in chain.residues():
                needNewResidue = True
                for atom in residue.atoms():
                    if atom.index in set_atom_indices:
                        if needNewChain:
                            newChain = newTopology.addChain(chain.id)
                            needNewChain = False;
                        if needNewResidue:
                            newResidue = newTopology.addResidue(residue.name, newChain, residue.id, residue.insertionCode)
                            needNewResidue = False;
                        newAtom = newTopology.addAtom(atom.name, atom.element, newResidue, atom.id)
                        newAtoms[atom] = newAtom
        for bond in item.bonds():
            if bond[0].index in set_atom_indices and bond[1].index in set_atom_indices:
                newTopology.addBond(newAtoms[bond[0]], newAtoms[bond[1]])
        return newTopology

def duplicate(item):

    raise NotImplementedError

def select_with_MDTraj(item, selection):

    tmp_item = to_mdtraj_Topology(item, selection='all', syntaxis='MDTraj')
    return tmp_item.select(selection)

#### Get

def get_n_atoms_from_atom(item, indices=None, frame_indices=None):

    return len(indices)

def get_atom_name_from_atom(item, indices=None, frame_indices=None):

    atom=list(item.atoms())
    atom_name=[atom[ii].name for ii in indices]
    del(atom)
    return atom_name

def get_atom_index_from_atom(item, indices=None, frame_indices=None):

    return indices

def get_atom_id_from_atom(item, indices=None, frame_indices=None):

    atom=list(item.atoms())
    atom_id=[atom[ii].id for ii in indices]
    del(atom)
    return atom_id

def get_atom_type_from_atom(item, indices=None, frame_indices=None):

    atom=list(item.atoms())
    atom_type=[atom[ii].element.symbol for ii in indices]
    del(atom)
    return atom_type

def get_n_residues_from_atom(item, indices=None, frame_indices=None):

    atom=list(item.atoms())
    residue_indices = [atom[ii].residue.index for ii in indices]
    residue_indices = list(set(residue_indices))
    del(atom)
    return len(residue_indices)

def get_residue_name_from_atom(item, indices=None, frame_indices=None):

    residue_indices = get_residue_index_from_atom (item, indices=indices)
    residue=list(item.residues())
    residue_names = [residue[ii].name for ii in residue_indices]
    del(residue, residue_indices)
    return residue_names

def get_residue_index_from_atom(item, indices=None, frame_indices=None):

    atom=list(item.atoms())
    residue_indices = [atom[ii].residue.index for ii in indices]
    del(atom)
    return residue_indices

def get_residue_id_from_atom(item, indices=None, frame_indices=None):

    atom=list(item.atoms())
    residue_ids = [atom[ii].residue.id for ii in indices]
    del(atom)
    return residue_ids

def get_chain_index_from_atom(item, indices=None, frame_indices=None):

    atom=list(item.atoms())
    chain_indices = [atom[ii].residue.chain.index for ii in indices]
    del(atom)
    return chain_indices

def get_chain_id_from_atom (item, indices=None, frame_indices=None):

    atom=list(item.atoms())
    chain_ids = [atom[ii].residue.chain.id for ii in indices]
    del(atom)
    return chain_ids

def get_n_chains_from_atom (item, indices=None, frame_indices=None):

    pass

def get_n_molecules_from_atom (item, indices=None, frame_indices=None):

    pass

def get_n_aminoacids_from_atom (item, indices=None, frame_indices=None):

    from molmodmt.topology import is_aminoacid
    residue_indices = get_residue_index_from_atom(item, indices=indices)
    residue_indices = list(set(residue_indices))
    residue_names = get_residue_name_from_residue(item, indices=residue_indices)
    n_aminoacids=0
    for residue_name in residue_names:
        if is_aminoacid(residue_name): n_aminoacids+=1
    del(residue_indices, residue_names)
    return n_aminoacids

def get_n_nucleotides_from_atom (item, indices=None, frame_indices=None):

    from molmodmt.topology import is_nucleotide
    residue_indices = get_residue_index_from_atom(item, indices=indices)
    residue_indices = list(set(residue_indices))
    residue_names = get_residue_name_from_residue(item, indices=residue_indices)
    n_nucleotides=0
    for residue_name in residue_names:
        if is_nucleotide(residue_name): n_nucleotides+=1
    del(residue_indices, residue_names)
    return n_nucleotides

def get_n_waters_from_atom (item, indices=None, frame_indices=None):

    from molmodmt.topology import is_water
    residue_indices = get_residue_index_from_atom(item, indices=indices)
    residue_indices = list(set(residue_indices))
    residue_names = get_residue_name_from_residue(item, indices=residue_indices)
    n_waters=0
    for residue_name in residue_names:
        if is_water(residue_name): n_waters+=1
    del(residue_indices, residue_names)
    return n_waters

def get_n_ions_from_atom (item, indices=None, frame_indices=None):

    from molmodmt.topology import is_ion
    residue_indices = get_residue_index_from_atom(item, indices=indices)
    residue_indices = list(set(residue_indices))
    residue_names = get_residue_name_from_residue(item, indices=residue_indices)
    n_ions=0
    for residue_name in residue_names:
        if is_ion(residue_name): n_ions+=1
    del(residue_indices, residue_names)
    return n_ions

def get_molecule_type_from_atom (item, indices=None, frame_indices=None):

    from molmodmt.topology import residue_name_to_molecule_type
    residue_names = get_residue_name_from_atom(item, indices=indices)
    molecule_types = [residue_name_to_molecule_type(ii) for ii in residue_names]
    del(residue_names, residue_name_to_molecule_type)
    return molecule_types

## Residue

def get_n_atoms_from_residue (item, indices=None, frame_indices=None):

    return len(indices)

def get_residue_name_from_residue (item, indices=None, frame_indices=None):

    residue=list(item.residues())
    residue_names = [residue[ii].name for ii in indices]
    del(residue)
    return residue_names

def get_residue_index_from_residue (item, indices=None, frame_indices=None):

    return indices

def get_residue_id_from_residue (item, indices=None, frame_indices=None):

    residue=list(item.residues())
    residue_ids = [residue[ii].id for ii in indices]
    del(residue)
    result.append(residue_ids)

def get_chain_index_from_residue (item, indices=None, frame_indices=None):

    residue=list(item.residues())
    chain_indices = [residue[ii].chain.index for ii in indices]
    del(residue)
    return chain_indices

def get_chain_id_from_residue (item, indices=None, frame_indices=None):

    residue=list(item.residues())
    chain_ids = [residue[ii].chain.id for ii in indices]
    del(residue)
    return chain_ids

def get_molecule_type_from_residue (item, indices=None, frame_indices=None):

    from molmodmt.topology import residue_name_to_molecule_type
    residue=list(item.residues())
    residue_names = [residue[ii].name for ii in indices]
    molecule_types = [residue_name_to_molecule_type(ii) for ii in residue_names]
    del(residue, residue_names, residue_name_to_molecule_type)
    return molecule_types

## Chain

def get_chain_index_from_chain (item, indices=None, frame_indices=None):

    chain=list(item.chains())
    chain_indices = [chain[ii].index for ii in indices]
    del(chain)
    return chain_indices

def get_chain_id_from_chain (item, indices=None, frame_indices=None):

    chain=list(item.chains())
    chain_ids = [chain[ii].id for ii in indices]
    del(chain)
    return chain_ids

def get_n_chains_from_chain (item, indices=None, frame_indices=None):

    return len(indices)

def get_molecule_type_from_chain (item, indices=None, frame_indices=None):

    from molmodmt.topology import residue_name_to_molecule_type
    chain=list(item.chains())
    molecule_types = []
    for ii in indices:
        residue = list(chain[ii].residues())[0]
        molecule_types.append(residue_name_to_molecule_type(residue.name))
    del(chain, residue)
    return molecule_types

## System

def get_n_atoms_from_system (item, indices=None, frame_indices=None):

    return item.getNumAtoms()

def get_charge_from_system (item, indices=None, frame_indices=None):

    return 'por hacer'

def get_net_charge_from_system (item, indices=None, frame_indices=None):

    return 'por hacer'

def get_n_frames_from_system (item, indices=None, frame_indices=None):

    return 0

def get_form_from_system(item, indices=None, frame_indices=None):

    from molmodmt import get_form
    return get_form(item)

