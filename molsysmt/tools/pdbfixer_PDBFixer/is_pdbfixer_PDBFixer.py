_item_fullname_='pdbfixer.PDBFixer'

def is_pdbfixer_PDBFixer(item):

    item_fullname = item.__class__.__module__+'.'+item.__class__.__name__

    return _item_fullname_==item_fullname

