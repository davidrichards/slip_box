# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00.00.indexes.ipynb (unless otherwise specified).

__all__ = ['integer_to_alpha', 'letter_to_value', 'alpha_to_integer', 'alphabet', 'is_integer', 'validate_index',
           'next_index', 'next_child', 'to_filename']

# Cell
from .imports import *

# Cell

alphabet = list('abcdefghijklmnopqrstuvwxyz')

def integer_to_alpha(n, alphabet=alphabet):
    """Convert numbers > 0 to alphabetic representations.
    For the regular alphabet, 1 == a, 26==z, 27==aa,
    52 == az, etc."""
    string = ''
    base = len(alphabet)

    while n > 0:
        denominator = n // base # denominator from floor division
        remainder = n % base

        # Take the nth letter in the alphabet.
        # 5 would be e, which is the 5th position in the alphabet
        # with an index of 4 (zero-based index).
        # If there is no remainder, 0 - 1 is -1, the last
        # letter in the alphabet.
        string = f'{alphabet[remainder - 1]}{string}'

        if remainder == 0: # no remainder means decrement the denominator...
            denominator -= 1
        n = denominator
    return string

def letter_to_value(letter, alphabet=alphabet):
    """Where does this letter fall in this alphabet?"""
    if not letter in alphabet: return 0
    return (alphabet.index(letter) + 1)

def alpha_to_integer(string, alphabet=alphabet):
    """Convert a string to an integer"""
    letters = list(str(string)) # 'abc' -> ['a', 'b', 'c']
    base = len(alphabet)
    increasing = list(reversed(letters))
    result = 0
    for position, letter in enumerate(increasing):
        value = letter_to_value(letter, alphabet=alphabet)
        value_at_position = (base ** position) * value
        result += value_at_position
    return result

# Cell

def is_integer(o):
    try:
        return int(o) == float(o)
    except:
        return False

def validate_index(current, separator='.', **kw):
    """Ensure the index can be iterated."""
    if current is None: return False
    if current == '': return False
    if len(str(current).split(separator)) == 0: return False
    return True

def next_index(current, separator='.', default='1', alphabet=alphabet, **kw):
    """Get the next value for an index.
    None returns '1', '' returns '1',
    1.a returns 1.b, etc."""

    if not validate_index(current, separator=separator): return default

    current = str(current)
    parts = current.split(separator)
    o = parts[-1]
    valid = parts[:-1]

    if is_integer(o):
        integer = int(o)
        if integer < 1: integer = 0
        value = str(integer + 1)
    else:
        integer = alpha_to_integer(o, alphabet=alphabet)
        value = integer_to_alpha(integer + 1, alphabet=alphabet)

    valid.append(value)

    return separator.join(valid)

def next_child(current, separator='.', default='1', alphabet=alphabet, **kw):
    """Get the next child for an index.
    None returns '1', '' returns '1',
    1.a returns 1.a.1, 2 returns 2.a."""

    if not validate_index(current, separator=separator): return default

    current = str(current)
    o = current.split(separator)[-1]
    if is_integer(o):
        value = alphabet[0]
    else:
        value = '1'

    return current + separator + value

# Cell

def to_filename(s, reference=None, index=None, child=False, separator=".", suffix="md", **kw):
    s = str(s).lower()
    title = separator.join(s.split())
    if index is None:
        fn = next_child if child else next_index
        index = fn(reference, separator=separator, **kw)
    return f"{index}{separator}{title}.{suffix}"