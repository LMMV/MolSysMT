def is_file_mol2(item):

    output = False

    if type(item)==str:
        output = item.endswith('.mol2')

    return output

