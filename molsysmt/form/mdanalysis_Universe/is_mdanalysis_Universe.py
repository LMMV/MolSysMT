
def is_mdanalysis_Universe(item):

    item_fullname = item.__class__.__module__+'.'+item.__class__.__name__
    output = (item_fullname == 'MDAnalysis.core.universe.Universe')
    return output

