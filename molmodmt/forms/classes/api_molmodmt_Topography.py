from os.path import basename as _basename
from molmodmt.utils.exceptions import *
from molmodmt.native.topography import Topography as _molmodmt_Topography

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _molmodmt_Topography : form_name,
    'molmodmt.Topography': form_name
}

def extract_subsystem(item, atom_indices=None, frame_indices=None):

    if (atom_indices is None) and (frame_indices is None):
        return item
    else:
        raise NotImplementedError


def duplicate(item):

    tmp_item = _molmodmt_Topography()

    return item

###### Get

## system

def get_form_from_system(item, indices=None, frame_indices=None):

    from molmodmt import get_form
    return get_form(item)

