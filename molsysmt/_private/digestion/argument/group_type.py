from ...exceptions import ArgumentError
from ...variables import is_all

def digest_group_type(group_type, caller=None):
    """Checks if `group_type` has the expected type and value.

    Parameters
    ----------
    group_type : Any
        The `group_type` argument for digestion.
    caller: str, optional
        Name of the function or method that is being digested.

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/#the-any-type

    Returns
    -------
    bool
        Either True or False when caller is `get`.

    Raises
    -------
    ArgumentError
        If the given `group_type` has not of the correct type or value.
    """

    if caller=='molsysmt.basic.get.get':
        if isinstance(group_type, bool):
            return group_type

    raise ArgumentError('group_type', value=group_type, caller=caller, message=None)

