def is_molsysmt_Structures(item):

    item_fullname = item.__class__.__module__+'.'+item.__class__.__name__
    output = (item_fullname == 'molsysmt.native.structures.Structures')

    return output

