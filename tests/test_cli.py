# functions being tested
from split import Split

import glob
import os
import argparse
import unittest

try:
    from unittest.mock import patch
except ImportError:
    # pre 3.3 need to pip install mock
    from mock import patch

from support.stdout_helper import get_stdout


class TestCli(unittest.TestCase):
    def __init__(self, methodName="runTest"):
        unittest.TestCase.__init__(self, methodName)
        self.file1 = os.path.join('.', 'tests', 'fixtures', 'qdc1.xml')
        self.outputdir = os.path.join('.', 'tests', 'fixtures', 'out')

    # TODO: stub filesystem? python equivalent to ruby fakefs?
    def tearDown(self):
        # clean up, remove xml files from output after each test
        for file in glob.glob(os.path.join(self.outputdir, '*.xml')):
            os.remove(file)

    def test_process_file_not_found(self):
        with self.assertRaises(EnvironmentError) as context:
            Split().process_file('asdf', 'asdf')

        self.assertTrue("No such file or directory: 'asdf'" in str(context.exception))

    def test_setup_params_cli_args(self):
        args = argparse.Namespace(filename=self.file1, outputdir=self.outputdir)
        with patch('argparse.ArgumentParser.parse_args', return_value=args):
            self.assertEqual((self.file1, self.outputdir), Split().setup_params())
            output = get_stdout()
            self.assertTrue("Processing input file " + self.file1 in output)
            self.assertTrue("Creating output xml files in " + self.outputdir in output)

    def test_setup_params_invalid_params(self):
        # if either the input file or output directory are invalid, print warning
        for arg_list in [[self.file1, "asdf"], ["asdf", self.outputdir]]:
            args = argparse.Namespace(filename=arg_list[0], outputdir=arg_list[1])
            with patch('argparse.ArgumentParser.parse_args', return_value=args):
                with self.assertRaises(SystemExit):
                    Split().setup_params()
                    output = get_stdout()
                    self.assertTrue("Invalid input or output location" in output)

    def test_split_with_filenames(self):
        args = argparse.Namespace(filename=self.file1, outputdir=self.outputdir)
        with patch('argparse.ArgumentParser.parse_args', return_value=args):
            files = ['test1.xml', 'test2.xml']
            for file in files:
                file_path = os.path.join(self.outputdir, file)
                self.assertFalse(os.path.isfile(file_path))

            Split().main()

            for file in files:
                file_path = os.path.join(self.outputdir, file)
                self.assertTrue(os.path.isfile(file_path))


if __name__ == '__main__':
    unittest.main()
