# dri-open-refine-split
Scripts for splitting an exported XML file from Open Refine to create multiple xml files for batch ingest into DRI. So far just a Python script, but other options might be added in future.

This tool should be used in conjuction with the Open Refine Dublin Core export template here https://gist.github.com/hellbunnie/dfca37537a80ec698a4cf9c773e4566a

If you follow the instructions on this gist you will end up with a single large file with all of your xml records in it. it is necessary to split these into multiple individual files, one per DC record before ingesting into DRI (or another repository).

Users on Windows machines are unlikely to have access to tool such as awk that make splitting the files relatively easy, so this script is provided to perform the splitting.

If you have included a FILENAME line in your export template then this script will automatically use those filenames to create your xml files. Otherwise the files will be named 1.xml, 2.xml, etc.

# Installation
Install Python 3 for your system.

To use the Graphical User Interface install the Python 3 Tkinter module.

Clone the repository from Github.

# Running
You can run this tool by double-clicking on the split.py file. Alternatively, you can run it from the command line.

Optional command-line parameters are --filename and --outputdir

If you do not pass the intput filename and outputdir on the command line you will be prompted to enter or select them. If you have Tkinter installed you can select the input file and output directory via a Graphical User Interface, otherwise they can be typed in on the command line.

# Tests
You can run the tests by entering the following into the command line.  
`python -m unittest discover tests --buffer`

Tested on python versions: 3.4 - 3.6
For more information see the .travis.yml file
