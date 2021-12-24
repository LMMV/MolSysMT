
def to_file_pir(item, selection='all', frame_indices='all', output_filename=None, syntaxis='MolSysMT'):

    from molsysmt.tools.biopython_SeqRecord import is_biopython_SeqRecord
    from molsysmt.basic import convert

    if not is_biopython_SeqRecord(item):
        raise ValueError

    if output_filename is None:
        raise ValueError

    tmp_item = convert(item, to_form=output_filename, selection=selection,
            frame_indices=frame_indices, syntaxis=syntaxis)

    return tmp_item

