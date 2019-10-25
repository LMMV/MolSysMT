import numpy as _np
from simtk import unit as _unit
from os.path import basename as _basename
from mdtraj.formats.xtc import XTCTrajectoryFile as _mdtraj_XTCTrajectoryFile

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _mdtraj_XTCTrajectoryFile: form_name,
    'mdtraj.XTCTrajectoryFile': form_name
    }

def load_frame (item, indices=None, atom_indices=None):

    from molmodmt.utils.math import serie_to_chunks

    starts_serie_frames, size_serie_frames = serie_to_chunks(indices)

    xyz_list = []
    time_list = []
    step_list = []
    box_list = []

    for start, size in zip(starts_serie_frames, size_serie_frames):
        item.seek(start)
        xyz, time, step, box = item.read(n_frames=size, atom_indices=atom_indices)
        xyz_list.append(xyz)
        time_list.append(time)
        step_list.append(step)
        box_list.append(box)

    xyz = _np.concatenate(xyz_list)
    del(xyz_list)
    time = _np.concatenate(time_list)
    del(time_list)
    step = _np.concatenate(step_list)
    del(step_list)
    box = _np.concatenate(box_list)
    del(box_list)

    xyz = xyz.astype('float64')
    box = box.astype('float64')
    time = time.astype('float64')
    step = step.astype('int64')

    xyz = xyz*_unit.nanometer
    box = box*_unit.nanometer
    time = time*_unit.picoseconds

    return step, time, xyz, box

def extract_subsystem(item, atom_indices=None, frame_indices=None):

    if (atom_indices is None) and (frame_indices is None):
        return item
    else:
        raise NotImplementedError

def duplicate(item):

    raise NotImplementedError

#### Get

def get_frames_from_atom (item, indices=None, frame_indices=None):

    step, time, xyz, box = load_frame(item, frame_indices, indices)
    return step, time, xyz, box

# system

def get_frames_from_system (item, indices=None, frame_indices=None):

    step, time, xyz, box = load_frame(item, indices=frame_indices)
    return step, time, xyz, box

def get_n_frames_from_system (item, indices=None, frame_indices=None):

    return len(item.offsets)

def get_box_shape_from_system (item, indices=None, frame_indices=None):

    from molmodmt.utils.pbc import get_shape_from_box
    position = item.tell()
    xyz, time, step, box = item.read(n_frames=1)
    item.seek(position)
    shape = get_shape_from_box(box*_unit.nanometers)
    del(xyz, time, step, box)
    return shape

def get_n_atoms_from_system (item, indices=None, frame_indices=None):

    position = item.tell()
    xyz, time, step, box = item.read(n_frames=1)
    n_atoms = xyz.shape[1]
    del(xyz, time, step, box)
    item.seek(position)
    return n_atoms

def get_form_from_system(item, indices=None, frame_indices=None):

    from molmodmt import get_form
    return get_form(item)

