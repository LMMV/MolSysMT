import os
import tempfile
from .utils.exceptions import *
from .utils.arguments import singular
from .utils.engines import digest as digest_engine
from .utils.forms import digest as digest_forms
from .utils.frame_indices import digest as digest_frame_indices
from .utils.selection import digest as digest_selection
from .utils.selection import digest_syntaxis
from .utils.selection import indices_to_syntaxis
from .utils.atom_indices import intersection_indices
import numpy as np

####
#### Molecular Models forms
####

# Classes
from .forms.classes import dict_is_form as dict_classes_is_form, \
    list_forms as list_classes_forms, \
    dict_info as dict_classes_infotxt, \
    dict_converter as dict_classes_converter, \
    dict_selector as dict_classes_selector, \
    dict_extractor as dict_classes_extractor, \
    dict_copier as dict_classes_copier, \
    dict_merge as dict_classes_merge, \
    dict_add as dict_classes_add, \
    dict_concatenate as dict_classes_concatenate, \
    dict_append as dict_classes_append, \
    dict_get as dict_classes_get, \
    dict_set as dict_classes_set

# Files
from .forms.files import dict_is_form as dict_files_is_form, \
    list_forms as list_files_forms, \
    dict_info as dict_files_infotxt, \
    dict_converter as dict_files_converter, \
    dict_selector as dict_files_selector, \
    dict_extractor as dict_files_extractor, \
    dict_copier as dict_files_copier, \
    dict_merge as dict_files_merge, \
    dict_add as dict_files_add, \
    dict_concatenate as dict_files_concatenate, \
    dict_append as dict_files_append, \
    dict_get as dict_files_get, \
    dict_set as dict_files_set

# IDs
from .forms.ids import dict_is_form as dict_ids_is_form, \
    list_forms as list_ids_forms, \
    dict_info as dict_ids_infotxt, \
    dict_converter as dict_ids_converter, \
    dict_selector as dict_ids_selector, \
    dict_extractor as dict_ids_extractor, \
    dict_copier as dict_ids_copier, \
    dict_merge as dict_ids_merge, \
    dict_add as dict_ids_add, \
    dict_concatenate as dict_ids_concatenate, \
    dict_append as dict_ids_append, \
    dict_get as dict_ids_get, \
    dict_set as dict_ids_set

# Sequences
from .forms.seqs import dict_is_form as dict_seqs_is_form, \
    list_forms as list_seqs_forms, \
    dict_info as dict_seqs_infotxt, \
    dict_converter as dict_seqs_converter, \
    dict_selector as dict_seqs_selector, \
    dict_extractor as dict_seqs_extractor, \
    dict_copier as dict_seqs_copier, \
    dict_merge as dict_seqs_merge, \
    dict_add as dict_seqs_add, \
    dict_concatenate as dict_seqs_concatenate, \
    dict_append as dict_seqs_append, \
    dict_get as dict_seqs_get, \
    dict_set as dict_seqs_set

# Viewers
from .forms.viewers import dict_is_form as dict_viewers_is_form, \
    list_forms as list_viewers_forms, \
    dict_info as dict_viewers_infotxt, \
    dict_converter as dict_viewers_converter, \
    dict_selector as dict_viewers_selector, \
    dict_extractor as dict_viewers_extractor, \
    dict_copier as dict_viewers_copier, \
    dict_merge as dict_viewers_merge, \
    dict_add as dict_viewers_add, \
    dict_concatenate as dict_viewers_concatenate, \
    dict_append as dict_viewers_append, \
    dict_get as dict_viewers_get, \
    dict_set as dict_viewers_set


dict_is_form = {**dict_classes_is_form, **dict_files_is_form,\
                 **dict_ids_is_form, **dict_seqs_is_form, **dict_viewers_is_form}

dict_infotxt = {**dict_classes_infotxt, **dict_files_infotxt,\
                   **dict_ids_infotxt, **dict_seqs_infotxt, **dict_viewers_infotxt}
dict_converter = {**dict_classes_converter, **dict_files_converter,\
                   **dict_ids_converter, **dict_seqs_converter, **dict_viewers_converter}
dict_selector = {**dict_classes_selector, **dict_files_selector,\
                   **dict_ids_selector, **dict_seqs_selector, **dict_viewers_selector}
dict_extractor = {**dict_classes_extractor, **dict_files_extractor,\
                   **dict_ids_extractor, **dict_seqs_extractor, **dict_viewers_extractor}
dict_copier = {**dict_classes_copier, **dict_files_copier,\
                   **dict_ids_copier, **dict_seqs_copier, **dict_viewers_copier}
dict_merge = {**dict_classes_merge, **dict_files_merge,\
                   **dict_ids_merge, **dict_seqs_merge, **dict_viewers_merge}
dict_add = {**dict_classes_add, **dict_files_add,\
                   **dict_ids_add, **dict_seqs_add, **dict_viewers_add}
dict_append = {**dict_classes_append, **dict_files_append,\
                   **dict_ids_append, **dict_seqs_append, **dict_viewers_append}
dict_concatenate = {**dict_classes_concatenate, **dict_files_concatenate,\
                   **dict_ids_concatenate, **dict_seqs_concatenate, **dict_viewers_concatenate}
dict_get = {**dict_classes_get, **dict_files_get,\
                   **dict_ids_get, **dict_seqs_get, **dict_viewers_get}
dict_set = {**dict_classes_set, **dict_files_set,\
                   **dict_ids_set, **dict_seqs_set, **dict_viewers_set}

dict_type = {}
for form in list_classes_forms:
    dict_type[form]='class'
for form in list_files_forms:
    dict_type[form]='file'
for form in list_ids_forms:
    dict_type[form]='id'
for form in list_seqs_forms:
    dict_type[form]='seq'
for form in list_viewers_forms:
    dict_type[form]='viewer'

list_types = ['class', 'file', 'id', 'seq', 'viewer']

####
#### Methods
####

def select(item, selection='all', target='atom', mask=None, syntaxis='MolSysMT', to_syntaxis=None):

    # to_syntaxis: 'NGLView', 'MDTraj', ...

    """select(item, selection='all', target='atom', syntaxis='MolSysMT')

    Get the atom indices corresponding to a selection criterion.

    Paragraph with detailed explanation.

    Parameters
    ----------

    item: molecular model
        Molecular model in any supported form (see: :doc:`/Forms`). The object being acted on by the method.

    selection: str, default='all'
       Selection criterion given by means of a string following any of the selection syntaxis parsable by MolSysMT.

    mask: list, tuple, numpy array or None. default=None
       XXX

    target: str, default='atom'
       The output indices list can correspond to 'atom', 'group', 'component', 'molecule', 'chain',
       'entity' or 'bond' indices.

    syntaxis: str, default='MolSysMT'
       Syntaxis used to write the argument `selection`. The current options supported by MolSysMt
       can be found in :doc:`/Atoms_Selection`.

    Returns
    -------

    Numpy array of integers
        List of indices in agreement with the selection criterion applied over `item`. The nature
        of the indices is chosen with the input argument 'output_indices': 'atom' (default),
        'group', 'component', 'molecule', 'chain' or 'entity'.

    Examples
    --------

    :doc:`/Atoms_Selection`

    See Also
    --------

    Notes
    -----

    """

    form_in, _ = digest_forms(item)
    syntaxis = digest_syntaxis(syntaxis)
    if to_syntaxis is not None:
        to_syntaxis = digest_syntaxis(to_syntaxis)

    if mask=='all':
        mask=None

    if type(selection)==str:
        if selection in ['all', 'All', 'ALL']:
            n_atoms = dict_get[form_in]['system']['n_atoms'](item)
            atom_indices = np.arange(n_atoms, dtype='int64')
        else:
            selection, syntaxis = digest_selection(selection, syntaxis)
            atom_indices = dict_selector[form_in][syntaxis](item, selection)
    elif type(selection) in [int, np.int64, np.int]:
        atom_indices = np.array([selection], dtype='int64')
    elif hasattr(selection, '__iter__'):
        atom_indices = np.array(selection, dtype='int64')
    else :
        atom_indices = None

    output_indices = []

    if target=='atom':
        output_indices = atom_indices
    elif target=='group':
        output_indices = get(item, target='atom', indices=atom_indices, group_index=True)
        output_indices = np.unique(output_indices)
    elif target=='component':
        output_indices = get(item, target='atom', indices=atom_indices, component_index=True)
        output_indices = np.unique(output_indices)
    elif target=='chain':
        output_indices = get(item, target='atom', indices=atom_indices, chain_index=True)
        output_indices = np.unique(output_indices)
    elif target=='molecule':
        output_indices = get(item, target='atom', indices=atom_indices, molecule_index=True)
        output_indices = np.unique(output_indices)
    elif target=='entity':
        output_indices = get(item, target='atom', indices=atom_indices, entity_index=True)
        output_indices = np.unique(output_indices)
    elif target=='bond':
        output_indices = get(item, target='atom', indices=atom_indices, inner_bond_index=True)

    else:
        raise NotImplementedError

    if mask is not None:
        output_indices = intersection_indices(output_indices,mask)

    if to_syntaxis is None:
        return output_indices
    else:
        return indices_to_syntaxis(item, output_indices, target=target, to_syntaxis=to_syntaxis)

def remove(item, selection=None, frame_indices=None, to_form=None, syntaxis='MolSysMT'):

    """remove(item, selection=None, frame_indices=None, syntaxis='MolSysMT')

    Remove atoms or frames from the molecular model.

    Paragraph with detailed explanation.

    Parameters
    ----------

    item: molecular model
        Molecular model in any of the supported forms by MolSysMT. (See: XXX)

    selection: str, list, tuple or np.ndarray, default=None
       Atoms selection over which this method applies. The selection can be given by a
       list, tuple or numpy array of integers (0-based), or by means of a string following any of
       the selection syntaxis parsable by MolSysMT (see: :func:`molsysmt.select`).

    frame_indices: str, list, tuple or np.ndarray, default=None
        XXX

    syntaxis: str, default='MolSysMT'
       Syntaxis used in the argument `selection` (in case it is a string). The
       current options supported by MolSysMt can be found in section XXX (see: :func:`molsysmt.select`).

    Returns
    -------
    item: molecular model
        The result is a new molecular model with the same form as the input item.

    Examples
    --------
    Remove chains 0 and 1 from the pdb: 1B3T.
    >>> import molsysmt as m3t
    >>> system = m3t.load('pdb:1B3T')
    Check the number of chains
    >>> m3t.get(system, n_chains=True)
    8
    Remove chains 0 and 1
    >>> new_system = m3t.remove(system, 'chainid 0 1')
    Check the number of chains of the new molecular model
    >>> m3t.get(new_system, n_chains=True)
    6

    See Also
    --------

    :func:`molsysmt.select`

    Notes
    -----
    There is a specific method to remove solvent atoms: molsysmt.remove_solvent and another one to
    remove hydrogens: molsysmt.remove_hydrogens.

    """

    atom_indices_to_be_kept = 'all'
    frame_indices_to_be_kept = 'all'

    if selection is not None:
        from .utils.atom_indices import complementary_atom_indices
        atom_indices_to_be_removed = select(item, selection, syntaxis=syntaxis)
        atom_indices_to_be_kept = complementary_atom_indices(item, atom_indices_to_be_removed)

    if frame_indices is not None:
        from .utils.frame_indices import digest as digest_frame_indices
        from .utils.frame_indices import complementary_frame_indices
        frame_indices_to_be_removed = digest_frame_indices(item, frame_indices)
        frame_indices_to_be_kept = complementary_frame_indices(item, frame_indices_to_be_removed)

    return extract(item, selection=atom_indices_to_be_kept, frame_indices=frame_indices_to_be_kept,
                   to_form=to_form, syntaxis=syntaxis)

def extract(item, selection='all', frame_indices='all', to_form=None, syntaxis='MolSysMT'):

    """extract(item, selection='all', frame_indices='all', syntaxis='MolSysMT')

    Extract a subset of a molecular model.

    Paragraph with detailed explanation.

    Parameters
    ----------

    item: molecular model
        Molecular model in any of the supported forms by MolSysMT. (See: XXX)

    selection: str, list, tuple or np.ndarray, defaul='all'
       Atoms selection over which this method applies. The selection can be given by a
       list, tuple or numpy array of integers (0-based), or by means of a string following any of
       the selection syntaxis parsable by MolSysMT (see: :func:`molsysmt.select`).

    syntaxis: str, default='MolSysMT'
       Syntaxis used in the argument `selection` (in case it is a string). The
       current options supported by MolSysMt can be found in section XXX (see: :func:`molsysmt.select`).

    Returns
    -------
    None
        The method prints out a pandas dataframe with relevant information depending on the target
        and the form of the item.

    Examples
    --------

    See Also
    --------

    :func:`molsysmt.select`

    Notes
    -----

    """

    form_in, form_out = digest_forms(item, to_form)

    if selection is 'all':
        atom_indices='all'
    else:
        atom_indices = select(item=item, selection=selection, syntaxis=syntaxis)

    out_file = None

    if type(form_out)==str:
        if form_out.split('.')[-1] in list_files_forms:
            out_file=form_out
            form_out=form_out.split('.')[-1]

    if (out_file is not None) and (form_in==form_out) :

        return dict_extractor[form_in](item, output_filepath=out_file, atom_indices=atom_indices, frame_indices=frame_indices)

    else:

        tmp_item = dict_extractor[form_in](item, atom_indices=atom_indices, frame_indices=frame_indices)

        if form_in!=form_out:
            tmp_item = convert(tmp_item, to_form=form_out)

        return tmp_item

def merge(items=None, selections='all', frame_indices='all', syntaxis='MolSysMT', to_form=None):

    """merge(items=None, selection='all', frame_indices='all', syntaxis='MolSysMT' to_form=None)

    XXX

    Paragraph with detailed explanation.

    Parameters
    ----------

    item: molecular model
        Molecular model in any of the supported forms by MolSysMT. (See: XXX)

    to_form: str, default='molsysmt.MolSys'
        Any accepted form by MolSysMt for the output object.

    selection: str, list, tuple or np.ndarray, defaul='all'
       Atoms selection over which this method applies. The selection can be given by a
       list, tuple or numpy array of integers (0-based), or by means of a string following any of
       the selection syntaxis parsable by MolSysMT (see: :func:`molsysmt.select`).

    syntaxis: str, default='MolSysMT'
       Syntaxis used in the argument `selection` (in case it is a string). The
       current options supported by MolSysMt can be found in section XXX (see: :func:`molsysmt.select`).

    Returns
    -------
    None
        The method prints out a pandas dataframe with relevant information depending on the target
        and the form of the item.

    Examples
    --------

    See Also
    --------

    :func:`molsysmt.get`, :func:`molsysmt.select`
    Notes
    -----

    """

    if type(items) not in [list, tuple]:
        raise ValueError('The argument items needs to be a list or tuple of molecular systems')

    if to_form is None:
        to_form = get_form(items[0])

    n_items = len(items)

    if type(selections) not in [list, tuple]:
        selections = [selections for ii in range(n_items)]
    elif len(selections)!=n_items:
        raise ValueError("The length of the lists items and selections need to be equal.")

    if type(frame_indices) not in [list, tuple]:
        frame_indices = [frame_indices for ii in range(n_items)]
    elif len(frame_indices)!=n_items:
        raise ValueError("The length of the lists items and selections need to be equal.")

    list_items = []
    list_atom_indices = []
    list_frame_indices = []

    for aux_item, aux_selection, aux_frame_indices in zip(items, selections, frame_indices):
        if get_form(aux_item)!=to_form:
            list_items.append(convert(aux_item, selection=aux_selection, frame_indices=aux_frame_indices, syntaxis=syntaxis, to_form=to_form))
            list_atom_indices('all')
            list_frame_indices('all')
        else:
            list_items.append(aux_item)
            list_atom_indices.append(select(aux_item, selection=aux_selection, syntaxis=syntaxis))
            list_frame_indices.append(aux_frame_indices)

    tmp_item = dict_merge[to_form](list_items, list_atom_indices=list_atom_indices, list_frame_indices=list_frame_indices)

    return tmp_item

def add(item, items=None, selections='all', frame_indices='all', syntaxis='MolSysMT'):

    # like merge but in place

    raise NotImplementedError

def concatenate(items=None, selections='all', frame_indices='all', syntaxis='MolSysMT', to_form=None):

    if type(items) not in [list, tuple]:
        raise ValueError('The argument items needs to be a list or tuple of molecular systems')

    if to_form is None:
        to_form = get_form(items[0])

    aux_items = []
    aux_atom_indices = []
    for ii in items:
        if get_form(ii)!=to_form:
            aux_items.append(convert(ii, selection=selection, syntaxis=syntaxis, to_form=to_form))
            aux_atom_indices.append('all')
        else:
            aux_items.append(ii)
            if selection is not 'all':
                aux_atom_indices.append(select(ii, selection=selection, syntaxis=syntaxis))
            else:
                aux_atom_indices.append('all')

    tmp_item = dict_concatenate[to_form](aux_items, atom_indices=atom_indices)

    if to_form is None:
        to_form = get_form(items[0])

    tmp_item = convert(items[0], to_form=to_form)

    for in_item in items[1:]:
        tmp_item2 = convert(in_item, to_form=to_form)
        tmp_item = dict_merger[to_form](tmp_item, tmp_item2)

    return tmp_item

def append(item, items=None, selections='all', frame_indices='all', syntaxis='MolSysMT'):

    # appending coordinates

    raise NotImplementedError

def info(item=None, target='system', indices=None, selection='all', syntaxis='MolSysMT', output='dataframe'):

    """info(item, target='system', indices=None, selection='all', syntaxis='MolSysMT')

    Print out general information of a molecular model.

    Paragraph with detailed explanation.

    Parameters
    ----------

    item: molecular model
        Molecular model in any of the supported forms by MolSysMT. (See: XXX)

    target: str, default='system'
        The nature of the entities this method is going to work with: 'atom', 'group', 'chain' or
        'system'.

    indices: int, list, tuple or np.ndarray, default=None
        List of indices referring the set of targetted entities ('atom', 'group' or 'chain') this
        method is going to work with. The set of indices can be given by a list, tuple or numpy
        array of integers (0-based).


    selection: str, list, tuple or np.ndarray, default='all'
       Atoms selection over which this method applies. The selection can be given by a
       list, tuple or numpy array of integers (0-based), or by means of a string following any of
       the selection syntaxis parsable by MolSysMT.

    syntaxis: str, default='MolSysMT'
       Selection syntaxis used in the argument `selection` (in case `selection` is a string). Find
       current options supported by MolSysMt in section 'Selection'.

    Returns
    -------
    None
        The method prints out a pandas dataframe with relevant information depending on the target
        and the form of the item.

    Examples
    --------

    See Also
    --------

    :func:`molsysmt.get`, :func:`molsysmt.select`

    Notes
    -----

    """

    if output=='dataframe':

        from pandas import DataFrame as df
        form_in, _ = digest_forms(item)
        target = singular(target)

        if target=='atom':

            atom_index, atom_id, atom_name, atom_type,\
            group_index, group_id, group_name, group_type,\
            component_index,\
            chain_index,\
            molecule_index, molecule_type,\
            entity_index, entity_name= get(item, target=target, indices=indices, selection=selection, syntaxis=syntaxis,
                                           atom_index=True, atom_id=True, atom_name=True, atom_type=True,
                                           group_index=True, group_id=True, group_name=True, group_type=True,
                                           component_index=True,
                                           chain_index=True,
                                           molecule_index=True, molecule_type=True,
                                           entity_index=True, entity_name=True)

            return df({'index':atom_index, 'id':atom_id, 'name':atom_name, 'type':atom_type,
                       'group index':group_index, 'group id':group_id, 'group name':group_name, 'group type':group_type,
                       'component index':component_index,
                       'chain index':chain_index,
                       'molecule index':molecule_index, 'molecule type':molecule_type,
                       'entity index':entity_index, 'entity name':entity_name}).style.hide_index()

        elif target=='group':

            group_index, group_id, group_name, group_type,\
            n_atoms, component_index,\
            chain_index,\
            molecule_index, molecule_type,\
            entity_index, entity_name = get(item, target=target, indices=indices, selection=selection, syntaxis=syntaxis,
                                            group_index=True, group_id=True, group_name=True, group_type=True, n_atoms=True,
                                            component_index=True, chain_index=True, molecule_index=True, molecule_type=True,
                                            entity_index=True, entity_name=True)

            return df({'index':group_index, 'id':group_id, 'name':group_name, 'type':group_type,
                       'n atoms':n_atoms,
                       'component index':component_index,
                       'chain index':chain_index,
                       'molecule index':molecule_index, 'molecule type':molecule_type,
                       'entity index':entity_index, 'entity name':entity_name}).style.hide_index()

        elif target=='component':

            component_index, n_atoms, n_groups,\
            chain_index,\
            molecule_index, molecule_type,\
            entity_index, entity_name = get(item, target=target, indices=indices, selection=selection, syntaxis=syntaxis,
                                            component_index=True, n_atoms=True, n_groups=True,
                                            chain_index=True,
                                            molecule_index=True, molecule_type=True,
                                            entity_index=True, entity_name=True)

            return df({'index':component_index,
                       'n atoms':n_atoms, 'n groups':n_groups,
                       'chain index':chain_index,
                       'molecule index':molecule_index, 'molecule type':molecule_type,
                       'entity index':entity_index, 'entity name':entity_name}).style.hide_index()

        elif target=='chain':

            chain_index, chain_id, chain_name,\
            n_atoms, n_groups, n_components,\
            molecule_index, molecule_type,\
            entity_index, entity_name = get(item, target=target, indices=indices, selection=selection, syntaxis=syntaxis,
                                            chain_index=True, chain_id=True, chain_name=True,
                                            n_atoms=True, n_groups=True, n_components=True,
                                            molecule_index=True, molecule_type=True,
                                            entity_index=True, entity_name=True)

            if len(molecule_index.shape)>1:
                n_objects = molecule_index.shape[0]
                aux_obj1_array = np.empty([n_objects], dtype='object')
                aux_obj2_array = np.empty([n_objects], dtype='object')
                for ii in range(n_objects):
                    aux_obj1_array[ii]=molecule_index[ii]
                    aux_obj2_array[ii]=molecule_type[ii]
                molecule_index=aux_obj1_array
                molecule_type=aux_obj2_array

            for ii in range(len(molecule_index)):
                if len(molecule_index[ii])==1:
                    molecule_index[ii]=molecule_index[ii][0]
                    molecule_type[ii]=molecule_type[ii][0]

            if len(entity_index.shape)>1:
                n_objects =entity_index.shape[0]
                aux_obj1_array = np.empty([n_objects], dtype='object')
                aux_obj2_array = np.empty([n_objects], dtype='object')
                for ii in range(n_objects):
                    aux_obj1_array[ii]=entity_index[ii]
                    aux_obj2_array[ii]=entity_name[ii]
                entity_index=aux_obj1_array
                entity_name=aux_obj2_array

            for ii in range(len(entity_index)):
                if len(entity_index[ii])==1:
                    entity_index[ii]=entity_index[ii][0]
                    entity_name[ii]=entity_name[ii][0]

            return df({'index':chain_index, 'id':chain_id, 'name':chain_name,
                       'n atoms':n_atoms, 'n groups':n_groups, 'n components':n_components,
                       'molecule index':molecule_index, 'molecule type':molecule_type,
                       'entity index':entity_index, 'entity name':entity_name}).style.hide_index()

        elif target=='molecule':

            molecule_index, molecule_name, molecule_type,\
            n_atoms, n_groups, n_components, chain_index,\
            entity_index, entity_name = get(item, target=target, indices=indices, selection=selection, syntaxis=syntaxis,
                                            molecule_index=True, molecule_name=True, molecule_type=True,
                                            n_atoms=True, n_groups=True, n_components=True, chain_index=True,
                                            entity_index=True, entity_name=True)

            if len(chain_index.shape)>1:
                n_objects = chain_index.shape[0]
                aux_obj_array = np.empty([n_objects], dtype='object')
                for ii in range(n_objects):
                    aux_obj_array[ii]=chain_index[ii]
                chain_index=aux_obj_array

            for ii in range(len(chain_index)):
                if len(chain_index[ii])==1:
                    chain_index[ii]=chain_index[ii][0]

            return df({'index':molecule_index, 'name':molecule_name, 'type':molecule_type,
                       'n atoms':n_atoms, 'n groups':n_groups, 'n components':n_components,
                       'chain index':chain_index,
                       'entity index':entity_index, 'entity name':entity_name}).style.hide_index()

        elif target=='entity':

            entity_index, entity_name, entity_type,\
            n_atoms, n_groups, n_components, n_chains,\
            n_molecules = get(item, target=target, indices=indices, selection=selection, syntaxis=syntaxis,
                    entity_index=True, entity_name=True, entity_type=True,
                    n_atoms=True, n_groups=True, n_components=True,
                    n_chains=True, n_molecules=True)

            return df({'index':entity_index, 'name':entity_name, 'type': entity_type,
                       'n atoms':n_atoms, 'n groups':n_groups, 'n components':n_components,
                       'n chains':n_chains, 'n molecules':n_molecules
                       }).style.hide_index()

        elif target=='system':

            form, n_atoms, n_groups, n_components, n_chains, n_molecules, n_entities = get(item, target=target,
                    form=True, n_atoms=True, n_groups=True, n_components=True, n_chains=True, n_molecules=True, n_entities=True)

            n_ions, n_waters, n_cosolutes, n_small_molecules, n_peptides, n_proteins, n_dnas, n_rnas = get(item, target=target,
                    n_ions=True, n_waters=True, n_cosolutes=True, n_small_molecules=True, n_peptides=True, n_proteins=True,
                    n_dnas=True, n_rnas=True)

            n_frames = get(item, target=target, n_frames=True)

            tmp_df = df({'form':form, 'n_atoms':n_atoms, 'n_groups':n_groups, 'n_components':n_components,
                'n_chains':n_chains, 'n_molecules':n_molecules, 'n_entities':n_entities,
                'n_waters':n_waters, 'n_ions':n_ions, 'n_cosolutes':n_cosolutes, 'n_small_molecules':n_small_molecules,
                'n_peptides':n_peptides, 'n_proteins':n_proteins, 'n_dnas':n_dnas, 'n_rnas':n_rnas,
                'n_frames':n_frames}, index=[0])

            if n_ions==0: tmp_df.drop(columns=['n_ions'], inplace=True)
            if n_waters==0: tmp_df.drop(columns=['n_waters'], inplace=True)
            if n_cosolutes==0: tmp_df.drop(columns=['n_cosolutes'], inplace=True)
            if n_small_molecules==0: tmp_df.drop(columns=['n_small_molecules'], inplace=True)
            if n_peptides==0: tmp_df.drop(columns=['n_peptides'], inplace=True)
            if n_proteins==0: tmp_df.drop(columns=['n_proteins'], inplace=True)
            if n_dnas==0: tmp_df.drop(columns=['n_dnas'], inplace=True)
            if n_rnas==0: tmp_df.drop(columns=['n_rnas'], inplace=True)

            return tmp_df.style.hide_index()

        else:

            raise ValueError('"target" needs one of the following strings: "atom", "group",\
                             "component", "chain", "molecule", "entity" or "system"')


    elif output=='short_string':

        string = None

        if indices is None and selection is not None:

            indices = select(item, selection=selection, target=target)

        string = _element2string(item, indices=indices, target=target)

        if len(string)==1:
            return string[0]
        else:
            return string

    elif output=='long_string':

        if target=='atom':

            group_indices, chain_indices, molecule_indices = get(item, target=target, indices=indices, group_index=True,
                                chain_index=True, molecule_index=True)

            atom_string = _element2string(item, indices=indices, target=target)
            group_string = _element2string(item, indices=group_indices, target='group')
            chain_string = _element2string(item, indices=chain_indices, target='chain')
            molecule_string = _element2string(item, indices=molecule_indices, target='molecule')

            string=[]

            for list_strings in zip(atom_string, group_string, chain_string,
                                    molecule_string):

                string.append('/'.join(list_strings))

            if len(string)==1:
                string=string[0]

        elif target=='group':

            chain_indices, molecule_indices = get(item, target=target, indices=indices,
                                chain_index=True, molecule_index=True)

            group_string = _element2string(item, indices=indices, target=target)
            chain_string = _element2string(item, indices=chain_indices, target='chain')
            molecule_string = _element2string(item, indices=molecule_indices, target='molecule')

            string=[]

            for list_strings in zip(group_string, chain_string,
                                    molecule_string):

                string.append('/'.join(list_strings))

            if len(string)==1:
                string=string[0]

        elif target=='component':

            chain_indices, molecule_indices = get(item, target=target, indices=indices,
                                chain_index=True, molecule_index=True)

            component_string = _element2string(item, indices=indices, target=target)
            chain_string = _element2string(item, indices=chain_indices, target='chain')
            molecule_string = _element2string(item, indices=molecule_indices, target='molecule')

            string=[]

            for list_strings in zip(component_string, chain_string, molecule_string):

                string.append('/'.join(list_strings))

            if len(string)==1:
                string=string[0]

        elif target=='chain':


            chain_string = _element2string(item, indices=indices, target=target)
            string=chain_string

            if len(string)==1:
                string=string[0]

        elif target=='molecule':


            molecule_string = _element2string(item, indices=indices, target=target)
            string=molecule_string

            if len(string)==1:
                string=string[0]

        elif target=='entity':

            entity_string = _element2string(item, indices=indices, target=target)
            string=entity_string

            if len(string)==1:
                string=string[0]

        else:

            raise NotImplementedError

        return string

    else:

        raise ValueError()

def _element2string(item, indices=None, target='atom'):

    string=[]

    if target=='atom':

        atom_indices, atom_ids, atom_names = get(item, target=target, indices=indices, index=True, id=True, name=True)
        for atom_index, atom_id, atom_name in zip(atom_indices, atom_ids, atom_names):
            string.append(atom_name+'-'+str(atom_id)+'@'+str(atom_index))

    elif target=='group':

        group_indices, group_ids, group_names = get(item, target=target, indices=indices, index=True, id=True, name=True)
        for group_index, group_id, group_name in zip(group_indices, group_ids, group_names):
            string.append(group_name+'-'+str(group_id)+'@'+str(group_index))

    elif target=='component':

        component_indices = get(item, target=target, indices=indices, index=True)
        for component_index in component_indices:
            string.append(str(component_index))

    elif target=='chain':

        chain_indices, chain_ids, chain_names = get(item, target=target, indices=indices, index=True, id=True, name=True)
        for chain_index, chain_id, chain_name in zip(chain_indices, chain_ids, chain_names):
            string.append(chain_name+'-'+str(chain_id)+'@'+str(chain_index))

    elif target=='molecule':

        molecule_indices, molecule_names = get(item, target=target, indices=indices, index=True, name=True)
        for molecule_index, molecule_name in zip(molecule_indices, molecule_names):
            string.append(molecule_name+'@'+str(molecule_index))

    elif target=='entity':

        entity_indices, entity_names = get(item, target=target, indices=indices, index=True, name=True)
        for entity_index, entity_name in zip(entity_indices, entity_names):
            string.append(entity_name+'@'+str(entity_index))

    return string


def get_form(item=None):

    from simtk.unit import Quantity

    if type(item) == Quantity:

        from .forms.classes.api_XYZ import this_Quantity_is_XYZ
        if this_Quantity_is_XYZ(item):
            return 'XYZ'
        else:
            raise NotImplementedError("This item's form has not been implemented yet")

    if type(item)==str:

        if ':' in item:
            prefix=item.split(':')[0]
            if prefix+':id' in dict_ids_is_form.keys():
                item=dict_ids_is_form[prefix+':id']
            elif prefix+':seq' in dict_seqs_is_form.keys():
                item=dict_seqs_is_form[prefix+':seq']
        else:
            item=item.split('.')[-1]

    if type(item)==list:
        output = [get_form(ii) for ii in item]
        return output

    try:
        return dict_is_form[type(item)]
    except:
        try:
            return dict_is_form[item]
        except:
            raise NotImplementedError("This item's form has not been implemented yet")

def get(item, target='atom', indices=None, selection='all', frame_indices='all', syntaxis='MolSysMT', **kwargs):

    """get(item, target='system', indices=None, selection='all', frame_indices='all', syntaxis='MolSysMT')

    Get specific attributes and observables.

    Paragraph with detailed explanation.

    Parameters
    ----------

    item: molecular model
        Molecular model in any of the supported forms by MolSysMT. (See: XXX)

    target: str, default='system'
        The nature of the entities this method is going to work with: 'atom', 'group', 'chain' or
        'system'.

    indices: int, list, tuple or np.ndarray, default=None
        List of indices referring the set of targetted entities ('atom', 'group' or 'chain') this
        method is going to work with. The set of indices can be given by a list, tuple or numpy
        array of integers (0-based).


    selection: str, list, tuple or np.ndarray, default='all'
       Atoms selection over which this method applies. The selection can be given by a
       list, tuple or numpy array of integers (0-based), or by means of a string following any of
       the selection syntaxis parsable by MolSysMT.

    syntaxis: str, default='MolSysMT'
       Selection syntaxis used in the argument `selection` (in case `selection` is a string). Find
       current options supported by MolSysMt in section 'Selection'.

    Returns
    -------
    None
        The method prints out a pandas dataframe with relevant information depending on the target
        chosen.

    Examples
    --------

    See Also
    --------

    :func:`molsysmt.get`, :func:`molsysmt.select`

    Notes
    -----

    """

    # In case of list of items

    if type(item) in [list, tuple]:
        results=[get(ii, target=target, indices=indices, selection=selection,
            frame_indices=frame_indices, syntaxis=syntaxis, **kwargs) for ii in item]
        return results

    # selection works as a mask if indices or ids are used

    form_in, _ = digest_forms(item)
    target = singular(target)
    attributes = [ key for key in kwargs.keys() if kwargs[key] ]

    # Patch to keep "residue":
    if target=='residue':
        target='group'

    tmp_attributes=[]
    for attribute in attributes:
        if 'residue' in attribute:
            tmp_attributes.append(attribute.replace('residue','group'))
        else:
            tmp_attributes.append(attribute)
    attributes=tmp_attributes

    # doing the work here

    if type(indices)==str:
        if indices in ['all', 'All', 'ALL']:
            indices = 'all'
        else:
            raise ValueError()
    elif type(indices) in [int, np.int64, np.int]:
        indices = np.array([indices], dtype='int64')
    elif hasattr(indices, '__iter__'):
        indices = np.array(indices, dtype='int64')

    if indices is None:
        if selection is not 'all':
            indices = select(item, target=target, selection=selection, syntaxis=syntaxis)
        else:
            indices = 'all'

    if type(frame_indices)==str:
        if frame_indices in ['all', 'All', 'ALL']:
            frame_indices = 'all'
        else:
            raise ValueError()
    elif type(frame_indices) in [int, np.int64, np.int]:
        frame_indices = np.array([frame_indices], dtype='int64')
    elif hasattr(frame_indices, '__iter__'):
        frame_indices = np.array(frame_indices, dtype='int64')


    results = []
    for attribute in attributes:
        result = dict_get[form_in][target][attribute](item, indices=indices, frame_indices=frame_indices)
        results.append(result)

    if len(results)==1:
        return results[0]
    else:
        return results

def set(item, target='system', indices=None, selection='all', frame_indices='all', syntaxis='MolSysMT', **kwargs):

    """into(item, target='system', indices=None, selection='all', frame_indices='all', syntaxis='MolSysMT')

    Set a new value to an attribute.

    Paragraph with detailed explanation.

    Parameters
    ----------

    item: molecular model
        Molecular model in any of the supported forms by MolSysMT. (See: XXX)

    target: str, default='system'
        The nature of the entities this method is going to work with: 'atom', 'group', 'chain' or
        'system'.

    indices: int, list, tuple or np.ndarray, default=None
        List of indices referring the set of targetted entities ('atom', 'group' or 'chain') this
        method is going to work with. The set of indices can be given by a list, tuple or numpy
        array of integers (0-based).

    selection: str, list, tuple or np.ndarray, defaul='all'
       Atoms selection over which this method applies. The selection can be given by a
       list, tuple or numpy array of integers (0-based), or by means of a string following any of
       the selection syntaxis parsable by MolSysMT (see: :func:`molsysmt.select`).

    frame_indices: int, list, tuple, np.ndarray or 'all', default='all'
        List of indices referring the set of frames this method is going to work with. This set of indices can be given by a list, tuple or numpy
        array of integers (0-based).

    syntaxis: str, default='MolSysMT'
       Syntaxis used in the argument `selection` (in case it is a string). The
       current options supported by MolSysMt can be found in section XXX (see: :func:`molsysmt.select`).

    Returns
    -------

    None
        XXX.

    Examples
    --------

    See Also
    --------

    :func:`molsysmt.select`

    Notes
    -----

    """


    form_in, _ = digest_forms(item)
    target = singular(target)
    attributes = [ key for key in kwargs.keys() ]

    # Patch to keep "residue":
    if target=='residue':
        target='group'

    tmp_attributes=[]
    for attribute in attributes:
        if 'residue' in attribute:
            tmp_attribute = attribute.replace('residue','group')
            tmp_attributes.append(tmp_attribute)
            kwargs [tmp_attribute]= kwargs[attribute]
            del(kwargs[attribute])
        else:
            tmp_attributes.append(attribute)
    attributes=tmp_attributes

    # doing the work here

    if indices is None:
        if target == 'atom':
            indices = select(item, selection=selection, syntaxis=syntaxis)
        elif target == 'group':
            indices = get(item, target='atom', selection=selection, syntaxis=syntaxis, group_index=True)
            indices = list(_unique(indices))
        elif target == 'chain':
            indices = get(item, target='atom', selection=selection, syntaxis=syntaxis, chain_index=True)
            indices = list(_unique(indices))
        elif target == 'system':
            indices = 0

    if frame_indices is 'all':
        n_frames = get(item, target='system', n_frames=True)
        frame_indices = np.arange(n_frames)
    elif type(frame_indices)==int:
        frame_indices = [frame_indices]

    for attribute in attributes:
        value = kwargs[attribute]
        dict_set[form_in][target][attribute](item, indices=indices, frame_indices=frame_indices, value=value)

    pass

def convert(item, to_form='molsysmt.MolSys', selection='all', frame_indices='all', syntaxis='MolSysMT', **kwargs):

    """convert(item, to_form='molsysmt.MolSys', selection='all', frame_indices='all', syntaxis='MolSysMT', **kwargs)

    Convert a molecular model into other form.

    A molecular model in a given accepted form can be converted into any other supported form
    by MolSysMt. The list of supported forms can be found in the section 'XXX'.

    Parameters
    ----------

    item: molecular model
        Molecular model in any supported form by MolSysMT (see: XXX).

    selection: str, list, tuple or np.ndarray, defaul='all'
       Atoms selection over which this method applies. The selection can be given by a
       list, tuple or numpy array of integers (0-based), or by means of a string following any of
       the selection syntaxis parsable by MolSysMT (see: :func:`molsysmt.select`).

    to_form: str, default='molsysmt.MolSys'
        The output object will take the form specified here. This form supported form by MolSysMt
        for the output object.

    syntaxis: str, default='MolSysMT'
       Syntaxis used in the argument `selection` (in case it is a string). The
       current options supported by MolSysMt can be found in section XXX (see: :func:`molsysmt.select`).

    Returns
    -------

       item: molecular model

       A new object is returned with the form specified by the argument `to_form`.

    Examples
    --------

    See Also
    --------

    :func:`molsysmt.load`, :func:`molsysmt.select`

    Notes
    -----

    """

    # atom_indices and frame_indices is solved here
    # either is 'all' or numpy.array
    # to avoid select or getting numframes inside api methods.

    same_system = False

    if selection is 'all' and frame_indices is 'all':
        same_system = True

    if type(to_form) in [list, tuple]:

        tmp_item=[]
        for item_out in to_form:
            tmp_item.append(convert(item, to_form=item_out, selection=selection,
                            frame_indices=frame_indices, syntaxis=syntaxis))

        any_not_None = False
        for ii in tmp_item:
           any_not_None+=(ii is not None)

        if not any_not_None:
            tmp_item=None

    else:

        form_in, form_out  = digest_forms(item, to_form)

        if type(form_in) not in [tuple,list]:

            if selection is 'all':
                atom_indices='all'
            else:
                atom_indices = select(item, selection=selection, syntaxis=syntaxis)

            out_file = None

            if type(form_out)==str:
                if form_out.split('.')[-1] in list_files_forms:
                    out_file=form_out
                    form_out=form_out.split('.')[-1]

            if out_file is not None:
                if form_in!=form_out:
                    tmp_item = dict_converter[form_in][form_out](item, output_filepath=out_file,
                                                          atom_indices=atom_indices, frame_indices=frame_indices,
                                                          **kwargs)
                elif same_system:
                    print('aaaaaaaaquiiiiiii')
                    tmp_item = copy(item, output_filepath=out_file)

                else:
                    tmp_item = extract(item, selection=atom_indices, frame_indices=frame_indices,
                                       to_form=out_file)

            else:
                if form_in!=form_out:
                    tmp_item = dict_converter[form_in][form_out](item, atom_indices=atom_indices,
                                                                  frame_indices=frame_indices, **kwargs)
                elif same_system:
                    tmp_item = copy(item)

                else:
                    tmp_item = extract(item, selection=atom_indices, frame_indices=frame_indices)

        else:

            if len(form_in)!=2:
                raise ValueError('The length of input items list is not 2.')

            topology_item = None
            topology_form = None
            trajectory_item = None
            trajectory_form = None
            with_topology = get(item, target='system', has_topology=True)
            with_topology = np.array(with_topology)
            n_topologies = with_topology.sum()
            with_trajectory = get(item, target='system', has_coordinates=True)
            with_trajectory = np.array(with_trajectory)
            n_trajectories = with_trajectory.sum()

            if n_topologies == 0:
                raise ValueError('There is no input item with topology')
            elif n_topologies == 1:
                topology_index = np.nonzero(with_topology)[0][0]
                coordinates_index = np.nonzero(~with_topology)[0][0]
                if with_coordinates[coordinates_index] is False:
                    raise ValueError('The item {} has the topology of the molecular system but {} has\
                                     no coordinates'.format(form_in[topology_index], form_in[coordinates_index]))
            elif n_topologies == 2:
                if n_coordinates ==0:
                    raise ValueError('Both items have topological information but no coordinates.')
                elif n_coordinates == 2:
                    print('Both items have topology and coordinates. The first one will be taken form\
                          topology and the second one for coordiantes.')
                    topology_index = 0
                    trajectory_index = 1
                else:
                    coordinates_index = np.nonzero(with_coordinates)[0][0]
                    topology_index = np.nonzero(~with_coordinates)[0][0]

            topology_item = item[topology_index]
            topology_form = form_in[topology_index]
            trajectory_item = item[coordinates_index]
            trajectory_form = form_in[coordinates_index]

            if selection is 'all':
                atom_indices='all'
            else:
                atom_indices = select(topology_item, selection=selection, syntaxis=syntaxis)

            out_file = None

            if type(form_out)==str:

                if form_out.split('.')[-1] in list_files_forms:
                    out_file=form_out
                    form_out=form_out.split('.')[-1]

            try:

                if out_file is not None:

                    if topology_form!=form_out:
                        tmp_item = dict_converter[topology_form][form_out](topology_item, trajectory_item=trajectory_item, output_filepath=out_file,
                                                              atom_indices=atom_indices, frame_indices=frame_indices,
                                                              **kwargs)
                    elif same_system:
                        tmp_item = copy(topology_item, output_filepath=out_file)

                    else:
                        tmp_item = extract(topology_item, selection=atom_indices, frame_indices=frame_indices,
                                           to_form=out_file)

                else:

                    if topology_form!=form_out:

                        tmp_item = dict_converter[topology_form][form_out](topology_item, trajectory_item=trajectory_item, atom_indices=atom_indices,
                                                                      frame_indices=frame_indices, **kwargs)
                    elif same_system:
                        tmp_item = copy(topology_item)

                    else:
                        tmp_item = extract(topology_item, selection=atom_indices, frame_indices=frame_indices)

            except:

                if out_file is not None:

                    if trajectory_form!=form_out:
                        tmp_item = dict_converter[trajectory_form][form_out](trajectory_item, output_filepath=out_file,
                                                              atom_indices=atom_indices, frame_indices=frame_indices,
                                                              **kwargs)
                    elif same_system:
                        tmp_item = copy(trajectory_item, output_filepath=out_file)
                    else:
                        tmp_item = extract(trajectory_item, selection=atom_indices, frame_indices=frame_indices,
                                           to_form=out_file)

                else:
                    if trajectory_form!=form_out:
                        tmp_item = dict_converter[trajectory_form][form_out](trajectory_item, atom_indices=atom_indices,
                                                                      frame_indices=frame_indices, **kwargs)
                    elif same_system:
                        tmp_item = copy(trajectory_item)
                    else:
                        tmp_item = extract(trajectory_form, selection=atom_indices, frame_indices=frame_indices)

    return tmp_item

def copy(item=None, output_filepath=None):

    form_in, _ = digest_forms(item)

    if output_filepath is None:
        return dict_copier[form_in](item)
    else:
        return dict_copier[form_in](item, output_filepath=output_filepath)

def write(item=None, filename=None, selection='all', frame_indices='all', syntaxis='MolSysMT'):

    return convert(item, to_form=filename, selection=selection, frame_indices='all', syntaxis=syntaxis)

def view(item=None, viewer='NGLView', selection='all', frame_indices='all',
        appending_coordinates=False, standardize=True, syntaxis='MolSysMT'):

    viewer = digest_engine(viewer)

    if type(item) in [list,tuple]:

        with_topologies = get(item, target='system', has_topology=True)
        with_coordinates = get(item, target='system', has_coordinates=True)

        if (len(item)==2) and (sum(with_topologies)==1) and (sum(with_coordinates)>0):
            tmp_item = convert(item, to_form=viewer, selection=selection, frame_indices=frame_indices, syntaxis=syntaxis)

        else:

            # There should be the possibility to create a list of nglview.NGLWidget to merge them
            # In the meantime the auxiliary step of converting all items to molsysmt will be used

            list_aux_items = []

            for ii in item:
                aux_item = convert(ii, to_form='molsysmt.MolSys', selection=selection, frame_indices=frame_indices, syntaxis=syntaxis)
                list_aux_items.append(aux_item)

            if appending_coordinates:
                tmp_item = concatenate(list_aux_items)
            else:
                tmp_item = merge(list_aux_items)

            tmp_item = convert(tmp_item, to_form=viewer)

    else:

        tmp_item = convert(item, to_form=viewer, selection=selection, frame_indices=frame_indices, syntaxis=syntaxis)

    if standardize:
        if viewer=='NGLView':
            from .nglview import standardize_view
            standardize_view(tmp_item)

    return tmp_item

