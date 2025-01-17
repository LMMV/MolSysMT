
def argument_names_standardization(caller, kwargs):

    if caller=='molsysmt.basic.get.get':

        element = kwargs['element']

        if 'name' in kwargs:
            kwargs = _replace_key_in_dict(kwargs, 'name', element+'_name')
        if 'index' in kwargs:
            kwargs = _replace_key_in_dict(kwargs, 'index', element+'_index')
        if 'id' in kwargs:
            kwargs = _replace_key_in_dict(kwargs, 'id', element+'_id')
        if 'type' in kwargs:
            kwargs = _replace_key_in_dict(kwargs, 'type', element+'_type')
            changed = True
        if 'order' in kwargs:
            kwargs = _replace_key_in_dict(kwargs, 'order', element+'_order')

    return kwargs

def _replace_key_in_dict(dictionary, old_key, new_key):

    # The order of the dictionary entries must be kept

    output = {}
    for key in dictionary:
        if key == old_key:
            output[new_key]=dictionary[key]
        else:
            output[key]=dictionary[key]

    return output

