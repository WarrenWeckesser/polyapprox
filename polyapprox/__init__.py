"""
``polyapprox``
--------------

Some tools for forming polynomial or rational approximations
of the inverse of a function.
"""

__all__ = ['revert', 'inverse_taylor', 'inverse_pade']


from ._inverse_approximant_tools import revert, inverse_taylor, inverse_pade
