from molsysmt._private_tools.exceptions import *

def from_file_xtc(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    raise NotImplementedError()

    #from molsysmt import convert
    #from .io_trajectory import from_xtc as xtc_to_Trajectory
    #from .molsys import MolSys

    #tmp_item = MolSys()
    #tmp_item.topology = convert(topology, to_form='molsysmt.Topology', selection=atom_indices, frame_indices=frame_indices)
    #tmp_item.trajectory = xtc_to_Trajectory(item, atom_indices=atom_indices, frame_indices=frame_indices)
    #tmp_item.topography = None
    #tmp_item.structure = None

    #return tmp_item

