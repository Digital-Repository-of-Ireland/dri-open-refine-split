import sys

# https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python
# output helper (hides pdb output too)


def get_stdout():
    if not hasattr(sys.stdout, "getvalue"):
        self.fail("need to run in buffered mode")
    return sys.stdout.getvalue().strip()
