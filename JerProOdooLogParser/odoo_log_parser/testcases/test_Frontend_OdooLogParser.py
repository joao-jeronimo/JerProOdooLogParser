# -*- coding: utf-8 -*-
import unittest, os, importlib
from unittest.mock import patch, Mock, MagicMock, call as mocked_call
frontend_OdooLogParser = importlib.import_module("OdooLogParser")

class TestFrontend_OdooLogParser(unittest.TestCase):
    """
    Top-down tests the OdooLogParser.py frontend
    """
    
    def test_Main_fails_on_nonsucess_logfile(self):
        """
        Method Main() must return non-zero if the logfile
        contains traces non-successfull test.
        """
        frontend_OdooLogParser.Main("OdooLogParser.py", ['--odoolog', '/path/to/odoo/logfile.log'])
    
    ############################################################
    ############################################################
    ############################################################
    def setUp(self):
        pass
    @classmethod
    def setUpClass(cls):
        pass
