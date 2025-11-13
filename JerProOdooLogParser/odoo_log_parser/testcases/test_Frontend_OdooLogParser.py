# -*- coding: utf-8 -*-
import unittest, os, importlib, assert_mixins
from unittest.mock import patch, Mock, MagicMock, call as mocked_call
frontend_OdooLogParser = importlib.import_module("OdooLogParser")

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')

class TestFrontend_OdooLogParser(unittest.TestCase, assert_mixins.ElementaryMixin):
    """
    Top-down tests the OdooLogParser.py frontend
    """
    
    def test_Main_fails_on_nonsucess_logfile(self):
        """
        Method Main() must return non-zero if the logfile
        contains traces non-successfull test.
        """
        self.assertPosixFailure(frontend_OdooLogParser.Main("OdooLogParser.py", ['--odoolog', os.path.join(FIXTURES_DIR, 'odoolog_errors_in_called_by_setup.log')]))
        self.assertPosixFailure(frontend_OdooLogParser.Main("OdooLogParser.py", ['--odoolog', os.path.join(FIXTURES_DIR, 'odoolog_skels_demo.log')]) )
        self.assertPosixSuccess(frontend_OdooLogParser.Main("OdooLogParser.py", ['--odoolog', os.path.join(FIXTURES_DIR, 'odoolog_two_succeeded.log')]) )
        self.assertPosixFailure(frontend_OdooLogParser.Main("OdooLogParser.py", ['--odoolog', os.path.join(FIXTURES_DIR, 'odoolog_with_setup_errors.log')]) )
        self.assertPosixFailure(frontend_OdooLogParser.Main("OdooLogParser.py", ['--odoolog', os.path.join(FIXTURES_DIR, 'odoolog_with_test_errors.log')]) )
        ### To be fixed:
        # Module dependency errors are not detected as such for now:
        self.assertPosixSuccess(frontend_OdooLogParser.Main("OdooLogParser.py", ['--odoolog', os.path.join(FIXTURES_DIR, 'odoolog_moddep_errors.log')]) )
        # Module install errors are not detected as such for now:
        self.assertPosixSuccess(frontend_OdooLogParser.Main("OdooLogParser.py", ['--odoolog', os.path.join(FIXTURES_DIR, 'odoolog_mod_install_errors.log')]) )
        # Module version string errors are not detected as such for now:
        self.assertPosixSuccess(frontend_OdooLogParser.Main("OdooLogParser.py", ['--odoolog', os.path.join(FIXTURES_DIR, 'odoolog_wrong_version_string.log')]) )
    
    ############################################################
    ############################################################
    ############################################################
    def setUp(self):
        pass
    @classmethod
    def setUpClass(cls):
        pass
