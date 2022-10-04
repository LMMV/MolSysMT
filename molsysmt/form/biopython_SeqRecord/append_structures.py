from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='biopython.SeqRecord')
def append_structures(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedMethodError()
