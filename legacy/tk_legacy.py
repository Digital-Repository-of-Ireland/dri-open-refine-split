gui = True
try:
    from tkinter import filedialog, Toplevel, Tk
    from tkinter import *
except ImportError:
    # 2.7 support block
    try:
        from Tkinter import Toplevel, Tk
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
