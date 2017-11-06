from .base import *

env = 'dev'

if env == 'dev':
    try:
        from .local import *
    except ImportError:
        pass

if env == 'prod':
    from .production import *
