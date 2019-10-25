from os.path import basename as _basename
from molmodmt.utils.exceptions import *
from molmodel import Chain as _molmodel_Chain

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _molmodel_Chain : form_name,
    'molmodel.Chain' : form_name
}

def extract_subsystem(item, atom_indices=None, frame_indices=None):

    if (atom_indices is None) and (frame_indices is None):
        return item
    else:
        raise NotImplementedError

def duplicate(item):

    raise NotImplementedError

###### Get

## system

def get_form_from_system(item, indices=None, frame_indices=None):

    from molmodmt import get_form
    return get_form(item)

