from os.path import basename as _basename
from molmodmt.utils.exceptions import *
from molmodel import Chain as _molmodel_Chain

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _molmodel_Chain : form_name,
    'molmodel.Chain' : form_name
}

