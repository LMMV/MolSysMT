def is_openmm_PDBFile(item):

    item_fullname = item.__class__.__module__+'.'+item.__class__.__name__
    output = (item_fullname == 'openmm.app.pdbfile.PDBFile')

    return output

