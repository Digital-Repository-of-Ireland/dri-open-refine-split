import sys


def get_stdout():
    # used to test values sent to stdout (hides pdb output too)
    if not hasattr(sys.stdout, "getvalue"):
        self.fail("need to run in buffered mode (--buffer)")
    return sys.stdout.getvalue().strip()
