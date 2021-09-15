from molsysmt._private_tools.exceptions import BadCallError

elements = [
    'atom',
    'group',
    'component',
    'chain',
    'molecule',
    'entity',
    'system',
    'bond',
]

elements_from_plural={
    'atoms' : 'atom',
    'groups' : 'group',
    'residue' : 'group',
    'residues' : 'group',
    'components' : 'component',
    'chains' : 'chain',
    'molecules' : 'molecule',
    'entities' : 'entity',
    'systems' : 'system',
    'bonds' : 'bond',
}

def digest_element(element):

    try:
        tmp_element = element.lower()
        if tmp_element in elements_from_plural:
            tmp_element = elements_from_plural[tmp_element]
        elif tmp_element not in elements:
            raise BadCallError()
        return tmp_element
    except:
        raise BadCallError()


def elements2string(molecular_system, indices=None, target='atom'):

    from molsysmt.basic import get
    from molsysmt._private_tools.targets import digest_target

    target = digest_target(target)

    string=[]

    if target=='atom':

        atom_indices, atom_ids, atom_names = get(molecular_system, target=target, indices=indices, index=True, id=True, name=True)
        for atom_index, atom_id, atom_name in zip(atom_indices, atom_ids, atom_names):
            string.append(atom_name+'-'+str(atom_id)+'@'+str(atom_index))

    elif target=='group':

        group_indices, group_ids, group_names = get(molecular_system, target=target, indices=indices, index=True, id=True, name=True)
        for group_index, group_id, group_name in zip(group_indices, group_ids, group_names):
            string.append(group_name+'-'+str(group_id)+'@'+str(group_index))

    elif target=='component':

        component_indices = get(molecular_system, target=target, indices=indices, index=True)
        for component_index in component_indices:
            string.append(str(component_index))

    elif target=='chain':

        chain_indices, chain_ids, chain_names = get(molecular_system, target=target, indices=indices, index=True, id=True, name=True)
        for chain_index, chain_id, chain_name in zip(chain_indices, chain_ids, chain_names):
            if chain_name is None:
                chain_name = '_'
            string.append(chain_name+'-'+str(chain_id)+'@'+str(chain_index))

    elif target=='molecule':

        molecule_indices, molecule_names = get(molecular_system, target=target, indices=indices, index=True, name=True)
        for molecule_index, molecule_name in zip(molecule_indices, molecule_names):
            if molecule_name is None:
                molecule_name = '_'
            string.append(molecule_name+'@'+str(molecule_index))

    elif target=='entity':

        entity_indices, entity_names = get(molecular_system, target=target, indices=indices, index=True, name=True)
        for entity_index, entity_name in zip(entity_indices, entity_names):
            if entity_name is None:
                molecule_name = '_'
            string.append(entity_name+'@'+str(entity_index))

    return string

