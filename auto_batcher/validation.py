from typing import Any, Union, Callable

def _validate_any(obj: Any, error_msg: str, default: Union[None, Any], validator_fn: Callable[[Any], bool]) -> Any:
    """Validates that a given object passes a given validation function

    If the given object is passes the validation function, the same object is
    returned. If the object did not pass and `default` is not `None`, the
    `default` object is returned. Otherwise, a TypeError is raised.

    Parameters
    ----------
    obj : Any
        the object to validate against the validation function
    error_msg : str
        the message to include in the TypeError if raised
    default : Union[None, Any]
        a default obejct to return in case `obj` failed the validation function
    validator_fn : Callable[[Any], bool]
        The function used to validate the object, it accepts a single parameter for
        the object and returns a boolean

    Returns
    -------
    Any
        The `obj` if it passed the validation function. If not, `default` is returned if specified

    Raises
    ------
    TypeError
        If `obj` did not pass the validation function and no `default` object is specified
    """
    final_obj = None

    if validator_fn(obj):
        final_obj = obj
    elif validator_fn(default):
        final_obj = default
    else:
        raise TypeError(error_msg)

    return final_obj

def validate_callable(obj: Any, error_msg: str, default: Union[None, Callable] = None) -> Callable:
    """Validates that a given object is callable.

    If the given object is indeed callable, the same object is returned. If the object
    is not callable and `default` is not `None`, the `default` callable is returned.
    Otherwise, a TypeError is raised.

    Parameters
    ----------
    obj : Any
        the object to validate that it's callable
    error_msg: str
        the message to include in the TypeError if raised
    default : Union[None, Callable], optional
        a default callable to return in case `obj` is not callable, by default None

    Returns
    -------
    Callable
        The `obj` if it's callable. If not, `default` is returned if specified

    Raises
    ------
    TypeError
        If `obj` is not callable and no `default` callable is specified
    """
    return _validate_any(obj, error_msg, default, validator_fn=callable)


def validate_int(obj: Any, error_msg: str, default: Union[None, int] = None) -> int:
    """Validates that a given object is an integer

    If the given object is indeed an integer, the same object is returned. If the object
    is not an integer and `default` is not `None`, the `default` integer is returned.
    Otherwise, a TypeError is raised.

    Parameters
    ----------
    obj : Any
        The object to validate that it's an integer
    error_msg : str
        the message to include in the TypeError if raised
    default : Union[None, int], optional
        a default integer to return in case `obj` is not an integer, by default None

    Returns
    -------
    int
        The `obj` if it's an inetger. If not, `default` is returned if specified

    Raises
    ------
    TypeError
        If `obj` is not an integer and no `default` integer is specified
    """
    return _validate_any(obj, error_msg, default, validator_fn=lambda o: isinstance(o, int))
