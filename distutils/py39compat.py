import sys
import platform


def ext_suffix(vars):
    """
    Ensure vars contains 'EXT_SUFFIX'. pypa/distutils#130
    """
    if sys.version_info < (3, 10):
        return vars
    if platform.system() != 'Windows':
        return vars
    import _imp
    vars.update(EXT_SUFFIX=_imp.extension_suffixes()[0])
