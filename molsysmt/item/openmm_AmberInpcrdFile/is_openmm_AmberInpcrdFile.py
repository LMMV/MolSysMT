
def is_openmm_AmberInpcrdFile(item):

    item_fullname = item.__class__.__module__+'.'+item.__class__.__name__

    return item_fullname == 'openmm.app.amberinpcrdfile.AmberInpcrdFile'

