def is_molsysmt_MolSys(item):

    item_fullname = item.__class__.__module__+'.'+item.__class__.__name__
    output = (item_fullname == 'molsysmt.native.molsys.MolSys')

    return output

