
def is_mdtraj_XTCTrajectoryFile(item):

    item_fullname = item.__class__.__module__+'.'+item.__class__.__name__

    return item_fullname == 'mdtraj.formats.xtc.XTCTrajectoryFile'

