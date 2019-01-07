from os.path import basename as _basename
import parmed

form_name=_basename(__file__).split('.')[0].split('_')[-1]

is_form={
    'parmed':form_name,
    parmed:form_name
    }

def to_modeller(item):

    from simtk.openmm.app.modeller import Modeller as _openmm_app_modeller
    tmp_form = _openmm_app_modeller(item.topology,item.positions)
    del(_openmm_app_modeller)
    return tmp_form

def to_mol2(item,out_file):

    return item.save(out_file)

def to_pdb(item,out_file):

    return item.save(out_file)
