
def _raise_not_implemented_error(item, indices=None, frame_indices=None, value=None):
    raise NotImplementedError

element_fields = {

        'atom' : {
            'name' : _raise_not_implemented_error
            },

        'residue' : {
            'name' : _raise_not_implemented_error
            },

        'chain' : {
            },

        'molecule' : {
            },

        'system' : {
            'box' : _raise_not_implemented_error
            'cell' : _raise_not_implemented_error
            }

        }
