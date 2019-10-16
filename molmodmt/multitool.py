import os
import tempfile
from .utils.exceptions import *
from .utils.arguments import singular as _singular
from .utils.forms import digest as _digest_forms
from .utils.frame_indices import digest as _digest_frame_indices
from .utils.selection import digest as _digest_selection
from numpy import unique as _unique
from numpy import ndarray as _ndarray
from numpy import sort as _sort
from numpy import arange as _arange

####
#### Molecular Models forms
####

# Classes
from .forms.classes import dict_is_form as _dict_classes_is_form, \
    list_forms as _list_classes_forms, \
    dict_converter as _dict_classes_converter, \
    dict_selector as _dict_classes_selector, \
    dict_extractor as _dict_classes_extractor, \
    dict_duplicator as _dict_classes_duplicator, \
    dict_merger as _dict_classes_merger, \
    dict_get as _dict_classes_get, \
    dict_set as _dict_classes_set

# Files
from .forms.files import dict_is_form as _dict_files_is_form, \
    list_forms as _list_files_forms, \
    dict_converter as _dict_files_converter, \
    dict_selector as _dict_files_selector, \
    dict_extractor as _dict_files_extractor, \
    dict_duplicator as _dict_files_duplicator, \
    dict_merger as _dict_files_merger, \
    dict_get as _dict_files_get, \
    dict_set as _dict_files_set

# IDs
from .forms.ids import dict_is_form as _dict_ids_is_form, \
    list_forms as _list_ids_forms, \
    dict_converter as _dict_ids_converter, \
    dict_selector as _dict_ids_selector, \
    dict_extractor as _dict_ids_extractor, \
    dict_duplicator as _dict_ids_duplicator, \
    dict_merger as _dict_ids_merger, \
    dict_get as _dict_ids_get, \
    dict_set as _dict_ids_set

# Sequences
from .forms.seqs import dict_is_form as _dict_seqs_is_form, \
    list_forms as _list_seqs_forms, \
    dict_converter as _dict_seqs_converter, \
    dict_selector as _dict_seqs_selector, \
    dict_extractor as _dict_seqs_extractor, \
    dict_duplicator as _dict_seqs_duplicator, \
    dict_merger as _dict_seqs_merger, \
    dict_get as _dict_seqs_get, \
    dict_set as _dict_seqs_set

# Viewers
from .forms.viewers import dict_is_form as _dict_viewers_is_form, \
    list_forms as _list_viewers_forms, \
    dict_converter as _dict_viewers_converter, \
    dict_selector as _dict_viewers_selector, \
    dict_extractor as _dict_viewers_extractor, \
    dict_duplicator as _dict_viewers_duplicator, \
    dict_merger as _dict_viewers_merger, \
    dict_get as _dict_viewers_get, \
    dict_set as _dict_viewers_set

_dict_is_form = {**_dict_classes_is_form, **_dict_files_is_form,\
                 **_dict_ids_is_form, **_dict_seqs_is_form, **_dict_viewers_is_form}
_dict_converter = {**_dict_classes_converter, **_dict_files_converter,\
                   **_dict_ids_converter, **_dict_seqs_converter, **_dict_viewers_converter}
_dict_selector = {**_dict_classes_selector, **_dict_files_selector,\
                   **_dict_ids_selector, **_dict_seqs_selector, **_dict_viewers_selector}
_dict_extractor = {**_dict_classes_extractor, **_dict_files_extractor,\
                   **_dict_ids_extractor, **_dict_seqs_extractor, **_dict_viewers_extractor}
_dict_duplicator = {**_dict_classes_duplicator, **_dict_files_duplicator,\
                   **_dict_ids_duplicator, **_dict_seqs_duplicator, **_dict_viewers_duplicator}
_dict_merger    = {**_dict_classes_merger, **_dict_files_merger,\
                   **_dict_ids_merger, **_dict_seqs_merger, **_dict_viewers_merger}
_dict_get = {**_dict_classes_get, **_dict_files_get,\
                   **_dict_ids_get, **_dict_seqs_get, **_dict_viewers_get}
_dict_set = {**_dict_classes_set, **_dict_files_set,\
                   **_dict_ids_set, **_dict_seqs_set, **_dict_viewers_set}

####
#### Molecular Models attributes
####

# Coordinates
from .attributes.coordinates import list_forms as _list_coordinates_forms, \
    dict_reformatter as _dict_coordinates_reformatter

_dict_reformatter={}
_dict_reformatter['coordinates']=_dict_coordinates_reformatter

_list_attributes = list(_dict_reformatter.keys())

####
#### Methods
####

def select(item, selection='all', syntaxis='MDTraj'):

    """select(item, selection='all', syntaxis='MDTraj')

    AAAAAAAAAAAAAAAAAA

    BBBBBBBBBBBBBBBBBB
    CCCCCCCCCCCCCCCCCC
    DDDDDDDDDDDDDDDDDD

    Parameters
    ----------

    item: Molecular model in accepted form.
        Molecular model in any of the accepted forms by MolModMT.
    selection:
    syntaxis:

    Returns
    -------

    Examples
    --------

    See Also
    --------

    Notes
    -----
    """

    from numpy import array as _array
    from numpy import ndarray as _ndarray
    from numpy import int as _int
    from numpy import int64 as _int64
    from numpy import arange as _arange

    form_in, _ = _digest_forms(item)

    if type(selection)==str:
        if selection in ['all', 'All', 'ALL']:
            n_atoms = _dict_get[form_in]['system']['n_atoms'](item)
            atom_indices = _arange(n_atoms, dtype='int64')
        else:
            selection, syntaxis = _digest_selection(selection, syntaxis)
            atom_indices = _dict_selector[form_in][syntaxis](item, selection)
    elif type(selection) in [int, _int64, _int]:
        atom_indices = _array([selection], dtype='int64')
    elif hasattr(selection, '__iter__'):
        atom_indices = _array(selection, dtype='int64')
    else :
        atom_indices = None

    atom_indices.sort()
    return atom_indices

def extract(item, selection='all', frame_indices='all', syntaxis='MDTraj'):

    form_in, _ = _digest_forms(item)

    # mode in ['removing_selection','keeping_selection']

    selection_is_all = False

    if type(selection)==str:
        if selection=="all":
            selection_is_all = True
    elif hasattr(selection, '__iter__'):
        n_atoms_selection = len(selection)
        n_atoms = _dict_get[form_in]['system']['n_atoms'](item)
        if n_atoms == n_atoms_selection:
            selection_is_all = True

    if selection_is_all:
        return item
    else:
        form_in, _ = _digest_forms(item)
        atom_indices = select(item=item, selection=selection, syntaxis=syntaxis)
        frame_indices = _digest_frame_indices(item, frame_indices)
        tmp_item = _dict_extractor[form_in](item, atom_indices=atom_indices, frame_indices=frame_indices)
        return tmp_item

def merge(item1=None, item2=None, to_form=None):

    #item1 can be a list or tuple

    if type(item1) in [list,tuple]:
        _ , form_out = _digest_forms(item1[0], to_form)
        tmp_item = convert(item1[0], form_out)
        for in_item in item1[1:]:
            tmp_item2 = convert(in_item, form_out)
            tmp_item = _dict_merger[form](tmp_item, tmp_item2)
        return tmp_item
    else:
        _ , form_out = _digest_forms(item1, to_form)
        tmp_item1 = convert(item1,form)
        tmp_item2 = convert(item2,form)
        return _dict_merger[form](tmp_item1, tmp_item1)

def info(item=None, target='system', indices=None, selection="all", syntaxis="MDTraj"):

    from pandas import DataFrame as df
    form_in, _ = _digest_forms(item)
    target = _singular(target)

    if target=='atom':

        atom_index, atom_id, atom_name, atom_element, residue_index, residue_id, residue_name, chain_index, chain_id,\
        chain_name, molecule_type = get(item, target=target, indices=indices, selection=selection, syntaxis=syntaxis,
                            index=True, id=True, name=True, element=True,
                            residue_index=True, residue_id=True, residue_name=True,
                            chain_index=True, chain_id=True, chain_name=True,
                            molecule_type=True)

        return df({'index':atom_index, 'id':atom_id, 'name':atom_name, 'element':atom_element,
                   'residue index':residue_index, 'residue id':residue_id, 'residue name':residue_name,
                   'chain index':chain_index, 'chain id':chain_id, 'chain name':chain_name, 'molecule type':molecule_type})

    elif target=='residue':

        index, id, name, chain_index, chain_id,\
        molecule_type = get(item, target=target, selection=selection, syntaxis=syntaxis,
                            residue_index=True, residue_id=True, residue_name=True,
                            chain_index=True, chain_id=True, molecule_type=True)


        return df({'name':name, 'index':index, 'id':id, 'chain index':chain_index, 'chain id':chain_id,
                   'molecule type':molecule_type})

    elif target=='chain':

        index, id, molecule_type = get(item, target=target, selection=selection, syntaxis=syntaxis,
                                       chain_index=True, chain_id=True, molecule_type=True)

        return df({'index':index, 'id':id, 'molecule type':molecule_type})

    elif target=='system':

        raise NotImplementedError

    else:

        raise NotImplementedError

    pass

def _get_form(item=None):

    if type(item)==str:
        if ':' in item:
            prefix=item.split(':')[0]
            if prefix+':id' in _dict_ids_is_form.keys():
                item=_dict_ids_is_form[prefix+':id']
            elif prefix+':seq' in _dict_seqs_is_form.keys():
                item=_dict_seqs_is_form[prefix+':seq']
        else:
            item=item.split('.')[-1]

    try:
        return _dict_is_form[type(item)]
    except:
        try:
            return _dict_is_form[item]
        except:
            raise NotImplementedError("This item's form has not been implemented yet")

def get(item, target='system', indices=None, selection='all', frame_indices='all', syntaxis='MDTraj', **kwargs):

    # selection works as a mask if indices or ids are used

    form_in, _ = _digest_forms(item)
    target = _singular(target)
    attributes = [ key for key in kwargs.keys() if kwargs[key] ]

    frame_indices = _digest_frame_indices(item, frame_indices)

    if indices is None:
        if target == 'atom':
            indices = select(item, selection=selection, syntaxis=syntaxis)
        elif target == 'residue':
            indices = get(item, target='atom', selection=selection, syntaxis=syntaxis, residue_index=True)
            indices = list(_unique(indices))
        elif target == 'chain':
            indices = get(item, target='atom', selection=selection, syntaxis=syntaxis, chain_index=True)
            indices = list(_unique(indices))
        elif target == 'system':
            indices = 0

    results = []
    for attribute in attributes:
        result = _dict_get[form_in][target][attribute](item, indices=indices, frame_indices=frame_indices)
        results.append(result)

    if len(results)==1:
        return results[0]
    else:
        return results

def set(item, target='system', indices=None, selection='all', frame_indices='all', syntaxis='mdtraj', **kwargs):

    form_in, _ = _digest_forms(item)
    target = _singular(target)
    attributes = [ key for key in kwargs.keys() ]

    if indices is None:
        if target == 'atom':
            indices = select(item, selection=selection, syntaxis=syntaxis)
        elif target == 'residue':
            indices = get(item, target='atom', selection=selection, syntaxis=syntaxis, residue_index=True)
            indices = list(_unique(indices))
        elif target == 'chain':
            indices = get(item, target='atom', selection=selection, syntaxis=syntaxis, chain_index=True)
            indices = list(_unique(indices))
        elif target == 'system':
            indices = 0

    if frame_indices == 'all':
        n_frames = get(item, n_frames=True)
        frame_indices = _arange(n_frames)
    elif type(frame_indices)==int:
        frame_indices = [frame_indices]

    for attribute in attributes:
        value = kwargs[attribute]
        _dict_set[form_in][target][attribute](item, indices=indices, frame_indices=frame_indices, value=value)

    pass

def load (item, to_form='molmodmt.MolMod', selection='all', frame_indices='all', syntaxis='MDTraj', **kwargs):

    """load(item, to_form='molmodmt.MolMod', selection='all', frame_indices='all', syntaxis='MDTraj', **kwargs)

    Loading a molecular model.

    A molecular model coming from a file can be loaded as a new target with any form supported by
    MolModMt. This method is just an alias of `convert`. It was included here only to make the
    usability more intuitive.

    Parameters
    ----------

    item: molecular model
        Molecular model in any of the supported forms by MolModMT.

    to_form: str, default='molmodmt.MolMod'
        Any accepted form by MolModMt for the output target.

    selection: str, list, tuple or np.ndarray, defaul='all'
       Atoms selection over which this method applies. The selection can be given specified by a
       list, tuple or numpy array of integers (0-based), or by means of a string following any of
       the selection syntaxis parsable by MolModMT.

    syntaxis: str, default='mdtraj'
       Selection syntaxis used in the argument `selection` (in case `selection` is a string). The
       current options supported by MolModMt are 'mdtraj' or 'amber'. More information about this
       topic can be found in the section 'Selection'.

    Returns
    -------

       item: molecular model
       A new target is returned with the form specified by the corresponding input argument.

    Examples
    --------

    See Also
    --------

    Notes
    -----

    """

    return convert(item, to_form, selection=selection, frame_indices=frame_indices, syntaxis=syntaxis, **kwargs)


def convert(item, to_form='molmodmt.MolMod', selection='all', frame_indices='all', syntaxis='MDTraj', **kwargs):

    """load(item, to_form='molmodmt.MolMod', selection='all', frame_indices='all', syntaxis='MDTraj', **kwargs)

    Transforming a molecular model from its current form into other supported form.

    A molecular model in a given accepted form can be converted into a new target with any form
    other form supported by MolModMt. The list of supported forms can be found in the section
    'Molecular Model Forms'.

    Parameters
    ----------

    item: molecular model
        Molecular model in any of the supported forms by MolModMT.

    to_form: str, default='molmodmt.MolMod'
        The output object will take the form specified here. This form  supported form by MolModMt for the output target.

    selection: str, list, tuple or np.ndarray, defaul='all'
       Atoms selection over which this method applies. The selection can be given specified by a
       list, tuple or numpy array of integers (0-based), or by means of a string following any of
       the selection syntaxis parsable by MolModMT.

    syntaxis: str, default='mdtraj'
       Selection syntaxis used in the argument `selection` (in case `selection` is a string). The
       current options supported by MolModMt are 'mdtraj' or 'amber'. More information about this
       topic can be found in the section 'Selection'.

    Returns
    -------

       item: molecular model in accepted form.
       A new object is returned with the form specified by the corresponding input argument.

    Examples
    --------

    See Also
    --------

    :func:`molmodmt.load`

    Notes
    -----

    Todo
    ----

    Warning
    -------

    """
    form_in, form_out  = _digest_forms(item, to_form)
    frame_indices = _digest_frame_indices(item, frame_indices)
    atom_indices = select(item, selection=selection, syntaxis=syntaxis)
    out_file = None

    if type(form_out)==str:
        if form_out.split('.')[-1] in _list_files_forms:
            form_out=form.split('.')[-1]
            out_file=form

    if out_file is not None:
        return _dict_converter[form_in][form_out](item, filename=out_file,
                                                  atom_indices=atom_indices, frame_indices=frame_indices,
                                                  **kwargs)
    else:
        if form_out != form_in:
            return _dict_converter[form_in][form_out](item, atom_indices=atom_indices,
                                                      frame_indices=frame_indices, **kwargs)
        else:
            return extract(item, selection=atom_indices, frame_indices=frame_indices)

def duplicate(item=None):

    form_in, _ = _digest_forms(item)

    return _dict_duplicator[form_in](item)

def write(item=None, filename=None, selection='all', frame_indices='all', syntaxis='MDTraj'):

    return convert(item,filename, selection=selection, frame_indices='all', syntaxis=syntaxis)

def view(item=None, viewer='nglview', selection='all', frame_indices='all', syntaxis='MDTraj'):

    if type(item) in [list,tuple]:
        form_in = _get_form(item[0])
        tmp_item = merge(item)
    else:
        form_in = _get_form(item)
        tmp_item = item

    atom_indices = select(tmp_item, selection=selection, syntaxis=syntaxis)
    frame_indices = _digest_frame_indices(item, frame_indices)

    return _dict_converter[form_in][viewer](tmp_item, atom_indices=atom_indices,
            frame_indices=frame_indices)

def reformat(attribute=None, value=None, is_format=None, to_format=None):

    if (attribute is not None) and attribute in _list_attributes:
        if is_format is not None:
            if to_format is not None:

                return _dict_reformatter[attribute][is_format][to_format](value)

            else:
                raise BadCallError(BadCallMessage)
        else:
            raise BadCallError(BadCallMessage)
    else:
        raise BadCallError(BadCallMessage)

