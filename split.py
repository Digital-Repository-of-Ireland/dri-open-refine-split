#!/usr/bin/env python

from __future__ import print_function
import argparse
from os import path
import re

from legacy.tk_legacy import TkLegacy, gui, Tk


# Get the filename and outputdir by hook or by crook!
# If the machine has Tkinter installed we can use a graphical
# file browser. Otherwise the user can enter the params on the
# command line or via an input prompt
# The multiple methods are there to make it as easy as possible
# for users with different needs and experience to use the tool
class Split:
    def __init__(self, master=None):
        if master: self.master = master
        self.dialog = TkLegacy().get_dialog()

    def main(self):
        filename, outputdir = self.setup_params()
        self.process_file(filename, outputdir)

    def setup_params(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--filename', help='The file to be split')
        parser.add_argument('--outputdir', help='Directory in which to create the split xml files')
        args = parser.parse_args()

        if gui:
            filename = args.filename or self.dialog.askopenfilename(
                parent=self.master,
                initialdir=".",
                title="Select file",
                filetypes=(("xml files", "*.xml"), ("all files", "*.*"))
            )
            outputdir = args.outputdir or self.dialog.askdirectory(
                parent=self.master,
                initialdir=".",
                title="Select output diretory"
            )
        else:
            filename = args.filename or input("Please enter the input filename ")
            outputdir = args.outputdir or input("Please enter the output directory ")

        filename = filename.rstrip()
        outputdir = outputdir.rstrip()

        if path.isfile(filename) and path.isdir(outputdir):
            print("Processing input file", filename)
            print("Creating output xml files in", outputdir)
            return filename, outputdir
        else:
            print("Invalid input or output location")
            exit(1)

    # processes input file and creates output files
    # Reads the file line by line look for start indicator
    # This should be either a line beginning FILENAME followed by the filename
    # or if that is not found we will fall back to searching for the xml header
    # line and will name files sequentially
    def process_file(self, inputfile, outputdir):
        filecount = 1
        outfile = False
        with open(inputfile, encoding="utf8") as i:
            for line in i:

                # ignore blank lines
                searchObj = re.search(r'^\s*$', line)
                if searchObj:
                    continue

                # Set the outfile name
                searchObj = re.search(r'^FILENAME (.*)', line)
                if searchObj:
                    outfile = path.join(outputdir, searchObj.group(1).rstrip() + ".xml")
                    continue

                searchObj = re.search(r'^<qualifieddc', line)
                if searchObj and not outfile:
                    outfile = path.join(outputdir, str(filecount) + ".xml")

                # Write the line to the current outfile
                with open(outfile, "a") as o:
                    o.write(line)

                # If we have reached the end of the file reset the filename
                searchObj = re.search(r'^</qualifieddc', line)
                if searchObj:
                    outfile = False
                    filecount += 1


def main():
    root = Tk()
    split = Split(root)
    split.main()


if __name__ == '__main__':
    main()
