from ...exceptions import ArgumentError
from ...variables import is_all
import numpy as np

def digest_group_indices(group_indices, caller):
    """ Checks if group_indices has the expected type and value.

    Parameters
    ----------
    indices : str or int or list or tuple or range.
        The indices

    caller: str, optional
        Name of the function or method that is being digested.
        For debugging purposes.

    Returns
    -------
    str or ndarray or None
        Either None, 'all' or an numpy array of integers with the indices.

    Raises
    -------
    ArgumentError
        If the given indices are not of the correct type.
    """

    if group_indices is None:
        return None
    elif is_all(group_indices):
        return 'all'
    elif isinstance(group_indices, (int, np.int64, np.int32)):
        return np.array([group_indices], dtype='int64')
    elif isinstance(group_indices, (np.ndarray, list, tuple, range)):
        return np.array(group_indices, dtype='int64')

    raise ArgumentError('group_indices', caller=caller, message=None)

