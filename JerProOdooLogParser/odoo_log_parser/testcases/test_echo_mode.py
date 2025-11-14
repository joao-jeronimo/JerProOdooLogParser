# -*- coding: utf-8 -*-
import re, unittest, random, os, odoo_log_parser
from odoo_log_parser.testcases.common import PythonLogParser_TestUtils
from unittest import TestCase
from unittest.mock import Mock, MagicMock

class TestEchoMode(unittest.TestCase):
    """
    Test behaviour of class odoo_log_parser.EchoMode.
    """
    
    def test_get_echo_plugin_invalid_plugin(self):
        """
        Method get_echo_plugin() must return None on invalid echo modes.
        """
        self.assertIsNone( odoo_log_parser.EchoMode.get_echo_plugin("this-is-an-invalid-echo-mode-name") )
    
    def test_get_echo_plugin_python(self):
        """
        Method get_echo_plugin() when called with 'python' must return the repr() function.
        """
        the_funk = odoo_log_parser.EchoMode.get_echo_plugin("python")
        self.assertEqual( the_funk('thing'), "'thing'" )
