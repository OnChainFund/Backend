"""
This type stub file was generated by pyright.
"""

import cytoolz

__all__ = ['merge', 'merge_with']
@cytoolz.curry
def merge(d, *dicts, **kwargs):
    ...

@cytoolz.curry
def merge_with(func, d, *dicts, **kwargs):
    ...

