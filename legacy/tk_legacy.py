# python 2.7 support

gui = True
try:
    from tkinter import filedialog
    from tkinter import *
except ImportError:
    # 2.7. block
    try:
        from Tkinter import *
        import Tkinter, Tkconstants, tkFileDialog
    except ImportError as e:
        gui = False

class TkLegacy:
    def get_dialog(self):
        # 2.7. block https://pythonspot.com/tk-file-dialogs/
        try:
            return filedialog
        except NameError:
            return tkFileDialog

    # used in test
    def get_root(self):
        try:
            return tkinter.Tk()
        except NameError:
            return Tkinter.Tk()
