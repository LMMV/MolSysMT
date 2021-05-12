from molsysmt._private_tools.exceptions import *

def from_crd(item, molecular_system, atom_indices='all', frame_indices='all'):

    from molsysmt.forms.files.api_crd import to_mdanalysis_Universe as crd_to_mdanalysis_Universe
    from molsysmt.forms.classes.api_mdanalysis_Universe import to_molsysmt_Trajectory as mdanalysis_Universe_to_molsysmt_Trajectory

    tmp_item, tmp_molecular_system = crd_to_mdanalysis_Universe(item, molecular_system)
    tmp_item, tmp_molecular_system = mdanalysis_Universe_to_molsysmt_Trajectory(tmp_item, tmp_molecular_system, atom_indices=atom_indices, frame_indices=frame_indices)

    return tmp_item, tmp_molecular_system

def to_crd(item, molecular_system, atom_indices='all', frame_indices='all'):

    raise NotImplementedError()
