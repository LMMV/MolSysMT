from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest_item, digest_step, digest_time, digest_box

def append_structures(item, step=None, time=None, coordinates=None, box=None, check=True):

    if check:

        digest_item(item, 'mdtraj.HDF5TrajectoryFile')
        step = digest_step(step)
        time = digest_time(time)
        coordinates = digest_coordinates(coordinates)
        box = digest_box(box)

    raise NotImplementedMethodError()

