# https://github.com/librosa/librosa/issues/1682

import lazy_loader as lazy
from .version import version as __version__

_filename = __file__
if _filename.endswith('.pyi'):
    _filename = _filename[:-1]

__getattr__, __dir__, __all__ = lazy.attach_stub(__name__, _filename)
