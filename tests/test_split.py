# functions being tested
from split import Split

import sys
import argparse
import unittest

# pre 3.3 need to pip install mock
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from support.stdout_helper import get_stdout


class TestSplit(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        unittest.TestCase.__init__(self, methodName)
        self.filename = "./tests/fixtures/qdc1.xml"
        self.outputdir = "./tests/fixtures/out"

    def test_process_file_not_found(self):
        with self.assertRaises(EnvironmentError) as context:
            Split().process_file('asdf', 'asdf')

        self.assertTrue("No such file or directory: 'asdf'" in str(context.exception))

    def test_setup_params_cli_args(self):
        args = argparse.Namespace(filename=self.filename, outputdir=self.outputdir)
        with patch('argparse.ArgumentParser.parse_args', return_value=args):
            self.assertEqual((self.filename, self.outputdir), Split().setup_params())
            output = get_stdout()
            self.assertTrue("Processing input file " + self.filename in output)
            self.assertTrue("Creating output xml files in " + self.outputdir in output)

    def test_setup_params_invalid_params(self):
        # if either the input file or output directory are invalid, print warning
        for arg_list in [[self.filename, "asdf"], ["asdf", self.outputdir]]:
            args = argparse.Namespace(filename=arg_list[0], outputdir=arg_list[1])
            with patch('argparse.ArgumentParser.parse_args', return_value=args):
                with self.assertRaises(SystemExit):
                    Split().setup_params()
                    output = get_stdout()
                    self.assertTrue("Invalid input or output location" in output)


if __name__ == '__main__':
    unittest.main()
