import errno
import os


def mkdir_all(path):
    try:
        os.makedirs(path, mode=0o777)
    except OSError as exc:  # Python ≥ 2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        # possibly handle other errno cases here, otherwise finally:
        else:
            raise
