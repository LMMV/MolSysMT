from molmodmt.utils.exceptions import *
from os.path import basename as _basename
from mdtraj.core.topology import Topology as _mdtraj_Topology

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _mdtraj_Topology : form_name,
    'mdtraj.Topology': form_name
}

## To other form

def to_aminoacids3_seq(item, selection='all', frame_indices='all', syntaxis='MDTraj'):

    return ''.join([ r.name for r in item.residues ])

def to_aminoacids1_seq(item, selection='all', frame_indices='all', syntaxis='MDTraj'):

    from molmodmt.forms.seqs.api_aminoacids3 import to_aminoacids1_seq as _aminoacids3_to_aminoacids1
    tmp_item = to_aminoacids3_seq(item)
    tmp_item = _aminoacids3_to_aminoacids1(tmp_item)
    del(_aminoacids3_to_aminoacids1)
    return tmp_item

def to_openmm_Topology(item, selection='all', frame_indices='all', syntaxis='MDTraj'):

    return item.to_openmm()

def to_yank_Topography(item, selection='all', frame_indices='all', syntaxis='MDTraj'):

    from .api_openmm_Topology import to_yank_Topography as _opennn_Topology_to_yank_Topography
    tmp_form = to_openmm_Topology(item)
    tmp_form = _opennn_Topology_to_yank_Topography(tmp_form)
    del(_opennn_Topology_to_yank_Topography)
    return tmp_form

def to_parmed_Structure(item, selection='all', frame_indices='all', syntaxis='MDTraj'):

    from .api_openmm_Topology import to_parmed_Structure as _opennn_Topology_to_parmed_Structure
    tmp_form = to_openmm_Topology(item)
    tmp_form = _opennn_Topology_to_parmed_Structure(tmp_form)
    del(_opennn_Topology_to_parmed_Structure)
    return tmp_form

def to_parmed_GromacsTopologyFile(item, selection='all', frame_indices='all', syntaxis='MDTraj'):
    from parmed.gromacs import GromacsTopologyFile as _GromacsTopologyFile
    tmp_form = to_parmed_Structure(item)
    return _GromacsTopologyFile.from_structure(item)

def to_top(item,filename):
    from .api_parmed_GromacsTopologyFile import to_top as _to_top
    tmp_form = to_parmed_GromacsTopologyFile(item)
    return _to_top(tmp_form,filename)

# Select

def select_with_MDTraj(item, selection):
    return item.select(selection)

# Extract

def extract_atom_indices(item, atom_indices, mode='keeping_selection'):

    if mode=='removing_selection':
        from molmodmt.utils.atom_indices import complementary_atom_indices
        atom_indices_to_be_kept = complementary_atom_indices(item, atom_indices)
    elif mode=='keeping_selection':
        atom_indices_to_be_kept = atom_indices

    # item.subset improved

    from mdtraj.core.topology import Topology
    from mdtraj.utils import ilen

    atom_indices_to_be_kept = set(atom_indices_to_be_kept)
    newTopology = Topology()
    old_atom_to_new_atom = {}

    for chain in item._chains:
        newChain = newTopology.add_chain()
        for residue in chain._residues:
            resSeq = getattr(residue, 'resSeq', None) or residue.index
            newResidue = newTopology.add_residue(residue.name, newChain,
                                                 resSeq, residue.segment_id)
            for atom in residue._atoms:
                if atom.index in atom_indices_to_be_kept:
                    try:  # OpenMM Topology objects don't have serial attributes, so we have to check first.
                        serial = atom.serial
                    except AttributeError:
                        serial = None
                    newAtom = newTopology.add_atom(atom.name, atom.element,
                                                   newResidue, serial=serial)
                    old_atom_to_new_atom[atom] = newAtom

    bondsiter = item.bonds
    if not hasattr(bondsiter, '__iter__'):
        bondsiter = bondsiter()

    for bond in bondsiter:
        try:
            atom1, atom2 = bond
            newTopology.add_bond(old_atom_to_new_atom[atom1],
                                 old_atom_to_new_atom[atom2],
                                 type=bond.type,
                                 order=bond.order)
        except KeyError:
            pass
            # we only put bonds into the new topology if both of their partners
            # were indexed and thus HAVE a new atom

    # Delete empty residues
    newTopology._residues = [r for r in newTopology._residues if len(r._atoms) > 0]
    for chain in newTopology._chains:
        chain._residues = [r for r in chain._residues if len(r._atoms) > 0]

    # Delete empty chains
    newTopology._chains = [c for c in newTopology._chains
                           if len(c._residues) > 0]
    # Re-set the numAtoms and numResidues
    newTopology._numAtoms = ilen(newTopology.atoms)
    newTopology._numResidues = ilen(newTopology.residues)

    return newTopology

# Merge

def merge_two_items(item1, item2, in_place=False):

    if in_place:
        item1.join(item2)
        pass
    else:
        tmp_item=item1.copy()
        return tmp_item.join(item2)

# Duplicate

def duplicate(item):

    return item.copy()

########################
### Get
########################

## from atom

def get_n_atoms_from_atom (item, indices=None, frame_indices=None):

    return len(indices)

def get_n_residues_from_atom (item, indices=None, frame_indices=None):

    atom=list(item.atoms)
    residue_indices = [atom[ii].residue.index for ii in indices]
    residue_indices = list(set(residue_indices))
    del(atom)
    return len(residue_indices)

def get_residue_name_from_atom(item, indices=None, frame_indices=None):

    atom=list(item.atoms)
    residue_names = [atom[ii].residue.name for ii in indices]
    del(atom)
    return residue_names

def get_residue_index_from_atom(item, indices=None, frame_indices=None):

    atom=list(item.atoms)
    residue_indices = [atom[ii].residue.index for ii in indices]
    del(atom)
    return residue_indices

def get_n_chains_from_atom (item, indices=None, frame_indices=None):

    atom=list(item.atoms)
    chain_indices = [atom[ii].residue.chain.index for ii in indices]
    chain_indices = list(set(chain_indices))
    del(atom)
    return len(chain_indices)

def get_chain_index_from_atom(item, indices=None, frame_indices=None):

    atom=list(item.atoms)
    chain_indices = [atom[ii].residue.chain.index for ii in indices]
    del(atom)
    return chain_indices

def get_n_aminoacids_from_atom (item, indices=None, frame_indices=None):

    from molmodmt.topology import is_aminoacid

    residue_indices = get_residue_index_from_atom(item, indices=indices)
    residue_indices = list(set(residue_indices))

    residue=list(item.residues)
    residue_names = [residue[ii].name for ii in residue_indices]
    del(residue)

    n_aminoacids=0
    for residue_name in residue_names:
        if is_aminoacid(residue_name): n_aminoacids+=1
    del(residue_indices, residue_names)
    return n_aminoacids

def get_n_nucleotides_from_atom (item, indices=None, frame_indices=None):

    from molmodmt.topology import is_nucleotide

    residue_indices = get_residue_index_from_atom(item, indices=indices)
    residue_indices = list(set(residue_indices))

    residue=list(item.residues)
    residue_names = [residue[ii].name for ii in residue_indices]
    del(residue)

    n_nucleotides=0
    for residue_name in residue_names:
        if is_nucleotide(residue_name): n_nucleotides+=1
    del(residue_indices, residue_names)
    return n_nucleotides

def get_n_waters_from_atom (item, indices=None, frame_indices=None):

    from molmodmt.topology import is_water

    residue_indices = get_residue_index_from_atom(item, indices=indices)
    residue_indices = list(set(residue_indices))

    residue=list(item.residues)
    residue_names = [residue[ii].name for ii in residue_indices]
    del(residue)

    n_waters=0
    for residue_name in residue_names:
        if is_water(residue_name): n_waters+=1
    del(residue_indices, residue_names)
    return n_waters

def get_n_ions_from_atom (item, indices=None, frame_indices=None):

    from molmodmt.topology import is_ion

    residue_indices = get_residue_index_from_atom(item, indices=indices)
    residue_indices = list(set(residue_indices))

    residue=list(item.residues)
    residue_names = [residue[ii].name for ii in residue_indices]
    del(residue)

    n_ions=0
    for residue_name in residue_names:
        if is_ion(residue_name): n_ions+=1
    del(residue_indices, residue_names)
    return n_ions

def get_n_molecules_from_atom (item, indices=None, frame_indices=None):

    from molmodmt import get
    return len(get(item, indices=indices, molecules=True))

def get_masses_from_atom (item, indices=None, frame_indices=None):

    return [atom.element.mass for atom in item.atoms]

def get_bonded_atoms_from_atom (item, indices=None, frame_indices=None):

    set_indices = set(indices)
    tmp_bonded = { ii:[] for ii in indices}
    for bond in item.bonds:
        if bond.atom1.index in set_indices:
            if bond.atom2.index in set_indices:
                tmp_bonded[bond.atom1.index].append(bond.atom2.index)
                tmp_bonded[bond.atom2.index].append(bond.atom1.index)
    return tmp_bonded

def get_bonds_from_atom (item, indices=None, frame_indices=None):

    tmp_bonds = []
    for bond in item.bonds:
        tmp_bonds.append([bond.atom1.index,bond.atom2.index])
    return tmp_bonds

def get_graph_from_atom (item, indices=None, frame_indices=None):

    return item.to_bondgraph()

def get_molecules_from_atom (item, indices=None, frame_indices=None):

    set_indices = set(indices)
    tmp_molecules = []
    for mm in item.find_molecules():
        molecule = [ii.index for ii in mm if ii.index in set_indices]
        if len(molecule)>0:
            tmp_molecules.append(molecule)

    return tmp_molecules

## from system

def get_n_atoms_from_system (item, indices=None, frame_indices=None):

    return item.n_atoms

def get_n_residues_from_system (item, indices=None, frame_indices=None):

    return item.n_residues

def get_n_chains_from_system (item, indices=None, frame_indices=None):

    return item.n_chains

def get_n_aminoacids_from_system (item, indices=None, frame_indices=None):

    atom_indices = list(range(get_n_atoms_from_system(item)))
    return get_n_aminoacids_from_atom (item, indices=atom_indices)

def get_n_nucleotides_from_system (item, indices=None, frame_indices=None):

    atom_indices = list(range(get_n_atoms_from_system(item)))
    return get_n_nucleotides_from_atom (item, indices=atom_indices)

def get_n_waters_from_system (item, indices=None, frame_indices=None):

    atom_indices = list(range(get_n_atoms_from_system(item)))
    return get_n_waters_from_atom (item, indices=atom_indices)

def get_n_ions_from_system (item, indices=None, frame_indices=None):

    atom_indices = list(range(get_n_atoms_from_system(item)))
    return get_n_ions_from_atom (item, indices=atom_indices)

def get_n_bonds_from_system (item, indices=None, frame_indices=None):

    return item.n_bonds

def get_bonded_atoms_from_system (item, indices=None, frame_indices=None):

    tmp_bonded = [[] for ii in range(item.n_atoms)]
    for bond in item.bonds:
        tmp_bonded[bond.atom1.index].append(bond.atom2.index)
        tmp_bonded[bond.atom2.index].append(bond.atom1.index)
    return tmp_bonded

def get_bonds_from_system (item, indices=None, frame_indices=None):

    tmp_bonds = []
    for bond in item.bonds:
        tmp_bonds.append([bond.atom1.index,bond.atom2.index])
    return tmp_bonds

def get_graph_from_system (item, indices=None, frame_indices=None):

    return item.to_bondgraph()

def get_molecules_from_system (item, indices=None, frame_indices=None):

    tmp_molecules = []
    for mm in item.find_molecules():
        tmp_molecules.append([ii.index for ii in mm])
    return tmp_molecules

