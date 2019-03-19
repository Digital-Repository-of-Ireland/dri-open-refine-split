# functions being tested
from split import Split
import argparse
import unittest

# pre 3.3 need to pip install mock
try:
    from unittest.mock import patch, MagicMock
    from tkinter import *
except ImportError:
    from mock import patch, MagicMock
    from Tkinter import *

from support.tkinter_test_case import TKinterTestCase
from support.stdout_helper import get_stdout


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
                        self.pump_events()
                        # split.dialog = MagicMock(name='dialog', return_value='test')
                        split.setup_params()
                        output = get_stdout()
                        assertTrue(output, 'Invalid input or output location')    

if __name__ == '__main__':
    unittest.main()
