from molsysmt._private.exceptions import ArgumentError

def digest_n_proteins(n_proteins, caller=None):

    if caller=='molsysmt.basic.get.get':
        if isinstance(n_proteins, bool):
            return n_proteins

    raise ArgumentError('n_proteins', value=n_proteins, caller=caller, message=None)

