import unittest
import sys  
import _tkinter

try:
    from tkinter import Tk
except ImportError:
    from Tkinter import Tk

# https://stackoverflow.com/a/49028688/6305204
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
