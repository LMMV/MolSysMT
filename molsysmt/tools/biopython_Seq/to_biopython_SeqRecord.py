
def to_biopython_SeqRecord(item, selection='all', frame_indices='all', id=None, name=None,
        description=None, syntaxis='MolSysMT'):

    from molsysmt.tools.biopython_Seq import is_biopython_Seq
    from molsysmt.basic import convert

    if not is_biopython_Seq(item):
        raise ValueError

    tmp_item = convert(item, to_form='biopython.SeqRecord', selection=selection,
            frame_indices=frame_indices, syntaxis=syntaxis, id=id, name=name,
            description=description)

    return tmp_item

