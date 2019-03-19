# functions being tested
from split import Split
import sys
import argparse
import unittest

# pre 3.3 need to pip install mock
try:
    from unittest.mock import patch, MagicMock
    from tkinter import Tk
    from tkinter import *
    import _tkinter
except ImportError:
    from mock import patch, MagicMock
    from Tkinter import *
    from Tkinter import Tk
    import _tkinter

# https://stackoverflow.com/a/49028688/6305204
# TODO refactor into general test support class
# duplicate method get_stdout
class TKinterTestCase(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.pump_events()

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pump_events()

    def pump_events(self):
        while self.root.dooneevent(_tkinter.ALL_EVENTS | _tkinter.DONT_WAIT):
            pass

    def tk_name(self):
        if sys.version_info[0] < 3:
            return 'tkFileDialog'
        else:
            return 'tkinter.filedialog'

    # output helper (hides pdb output too)
    def get_stdout(self):
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        return sys.stdout.getvalue().strip()


class TestGui(TKinterTestCase):
    def __init__(self, methodName = "runTest"):
        unittest.TestCase.__init__(self, methodName)

    # TODO: better test that opens dialog rather than stubbing it
    def test_setup_params_gui_args(self):
        args = argparse.Namespace(filename = None, outputdir = None)
        with patch('argparse.ArgumentParser.parse_args', return_value = args):
            with patch(self.tk_name() + '.askopenfilename', return_value = 'test'):
                with patch(self.tk_name() + '.askdirectory', reutrn_value = 'test'):
                    with self.assertRaises(SystemExit) as context:
                        split = Split(self.root)
                        # self.pump_events()
                        # split.dialog = MagicMock(name='dialog', return_value='test')
                        split.setup_params()
                        output = self.get_stdout()
                        assertTrue(output, 'Invalid input or output location')

    # def test_tkinter(self):
    #     try:
    #         tkinter._test()
    #     except NameError:
    # # AttributeError: 'module' object has no attribute '_test'
    #         Tkinter._test()
    

if __name__ == '__main__':
    unittest.main()
