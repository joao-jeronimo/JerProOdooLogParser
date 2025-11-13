# -*- coding: utf-8 -*-
import unittest, os, importlib
from unittest.mock import patch, Mock, MagicMock, call as mocked_call
frontend_OdooLogParser = importlib.import_module("OdooLogParser")

class TestFrontend_OdooLogParser(unittest.TestCase):
    """
    Top-down tests the OdooLogParser.py frontend
    """
    
    @patch('builtins.print')
    def test_Main_skel(self, mock_print):
        """
        O método Main() esqueleto.
        """
        frontend_OdooLogParser.Main("OdooLogParser.py", [])
    
    ############################################################
    ############################################################
    ############################################################
    def setUp(self):
        pass
    @classmethod
    def setUpClass(cls):
        pass
