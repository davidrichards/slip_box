import os,pickle,re,shutil,sys,zlib

from configobj import ConfigObj
from contextlib import contextmanager
import datetime as dt
from datetime import datetime
from functools import partial
from pathlib import Path
import pathlib

@contextmanager
def check_raises(**kw):
    """Assert some code raises an error.
    Can pass in a message (`check_raises(message="Custom message")`).
    Can pass in an exception (`check_raises(exception=ArgumentError)`).
    """
    message = kw.get('message', "Expected to raise, did not.")
    expected_exception = kw.get('exception', Exception)
    failed = False
    try:
        yield
    except expected_exception:
        failed = True
    except Exception as e:
        message = f"Expected to raise {expected_exception}. Instead received {e.__class__.__name__}"
    finally:
        if not failed:
            assert False, message

def check_is_near(a, b, message=None, **kw):
    """Wrap the numpy isclose function."""
    if message is None:
        message = f"Expected {a} to be close to {b}."
    result = np.isclose(a, b, **kw)
    if np.size(result) == 1: result = [result]
    if not all(result):
        assert False, message

def check_equals(a, b, **kw):
    """Check if two values are equal.
    Not type sensitive.
    Can handle 1 or n-dimensional objects."""
    kw = {**kw, **{'atol': 0, 'message': f"Expected {a} to equal {b}."}}
    return check_is_near(a, b, **kw)

def remove_file(path):
    """Helper function to remove a file if it exists.
    Useful for testing."""
    path = str(path)
    if os.path.exists(path):
        os.unlink(path)
