try:
    import uvloop

    uvloop.install()
except ImportError:
    pass

from .app import app  # noqa
