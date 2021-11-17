import numpy as np
from molsysmt import puw
from molsysmt._private_tools.molecular_system import digest_molecular_system
from molsysmt._private_tools.frame_indices import digest_frame_indices
from molsysmt.lib import geometry as libgeometry
from molsysmt.structure.get_dihedral_angles import get_dihedral_angles
from molsysmt.structure.set_dihedral_angles import set_dihedral_angles


def shift_dihedral_angles(molecular_system, quartets=None, angles_shifts=None, blocks=None,
                          frame_indices='all', pbc=True, in_place=False, engine='MolSysMT'):

    from molsysmt.basic import get

    molecular_system = digest_molecular_system(molecular_system)
    frame_indices = digest_frame_indices(frame_indices)

    if type(quartets) in [list,tuple]:
        quartets = np.array(quartets, dtype=int)
    elif type(quartets) is np.ndarray:
        pass
    else:
        raise ValueError

    shape = quartets.shape

    if len(shape)==1:
        if shape[0]==4:
            quartets=quartets.reshape([1,4])
        else:
            raise ValueError
    elif len(shape)==2:
        if shape[1]!=4:
            raise ValueError
    else:
        raise ValueError

    n_quartets = quartets.shape[0]
    n_frames = get(molecular_system, target='system', frame_indices=frame_indices, n_frames=True)

    angles_shifts_units = puw.get_unit(angles_shifts)
    angles_shifts_value = puw.get_value(angles_shifts)

    if type(angles_shifts_value) in [float]:
        if (n_quartets==1 and n_frames==1):
            angles_shifts_value = np.array([[angles_shifts_value]], dtype=float)
        else:
            raise ValueError("angles_shifts do not match the number of frames and quartets")
    elif type(angles_shifts_value) in [list,tuple]:
        angles_shifts_value = np.array(angles_shifts_value, dtype=float)
    elif type(angles_shifts_value) is np.ndarray:
        pass
    else:
        raise ValueError

    shape = angles_shifts_value.shape

    if len(shape)==1:
        angles_shifts_value = angles_shifts_value.reshape([n_frames, n_quartets])

    angles_shifts=angles_shifts_value*angles_shifts_units

    angles = get_dihedral_angles(molecular_system, quartets=quartets, frame_indices=frame_indices, pbc=pbc)
    angles = angles + angles_shifts

    return set_dihedral_angles(molecular_system, quartets=quartets, angles=angles, blocks=None,
                               frame_indices=frame_indices, pbc=pbc, in_place=in_place, engine=engine)
