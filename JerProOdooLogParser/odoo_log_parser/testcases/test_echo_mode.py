# -*- coding: utf-8 -*-
import re, unittest, random, os, odoo_log_parser
from odoo_log_parser.testcases.common import PythonLogParser_TestUtils
from unittest import TestCase
from unittest.mock import Mock, MagicMock

class TestEchoMode(unittest.TestCase):
    """
    Test behaviour of class odoo_log_parser.EchoMode.
    """
    maxDiff = None
    
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
    
    def test_get_echo_plugin_pretty(self):
        """
        Method get_echo_plugin() when called with 'pretty' must return prettified Python code.
        """
        the_funk = odoo_log_parser.EchoMode.get_echo_plugin("pretty")
        self.assertEqual( the_funk([4,5,6,7,3,2,2,[4,5,6,7,3,2,2,[4,5,6,7,3,2,2,[4,5,6,7,3,2,2,]]]]), (
            "[   4,\n"
            "    5,\n"
            "    6,\n"
            "    7,\n"
            "    3,\n"
            "    2,\n"
            "    2,\n"
            "    [4, 5, 6, 7, 3, 2, 2, [4, 5, 6, 7, 3, 2, 2, [4, 5, 6, 7, 3, 2, 2]]]]"
            ))
    
    def test_get_echo_plugin_tabular(self):
        """
        Method get_echo_plugin() when called with 'tabular' must return the table.
        """
        
        # "/odoo/Suite-code/manager/autoerp_lib/testcases/fixtures/odoolog_skels_demo.log"
        
        the_funk = odoo_log_parser.EchoMode.get_echo_plugin("tabular")
        self.assertEqual( the_funk(
            {   'adhoc-test17': {
                    'setup_errors': [],
                    'tests_errors': [],
                    'tests_failing': [
                        {   'test_path': 'odoo.addons.hr_payroll_community_demo_data.tests.test_skel.TestObjects.test_fails',
                            'test_log': (
                                'FAIL: TestObjects.test_fails\n'
                                'Traceback (most recent call last):\n'
                                '  File "/odoo/Instances/demodevel-jj-hr-odoo17/SuiteRepos/SimplePayslipTemplate/0_Installable/17.0/hr_payroll_community_demo_data/tests/test_skel.py", line 7, in test_fails\n'
                                '    self.assertTrue(False)\n'
                                'AssertionError: False is not true\n'
                                ' '
                                ),
                            },
                        ],
                    'tests_succeeded': [
                        {   'test_path': 'odoo.addons.hr_payroll_community_demo_data.tests.test_skel.TestObjects.test_passes',
                            'test_log': 'Starting TestObjects.test_passes ... ',
                            },
                        ],
                    }}
            ), (
        """
== Database: adhoc-test17
+-------------+--------------------------------+--------------------------------------+
| Test status | Test path                      | Test log                             |
+-------------+--------------------------------+--------------------------------------+
|             | odoo                           | ▓FAIL: TestObjects.test_fails        |
| FAIL        | addons                         | ▓Traceback (most recent call last):  |
|             | hr_payroll_community_demo_data | ▓  File "/odoo/Instances/demodevel-j |
|             | tests                          |  j-hr-odoo17/SuiteRepos/SimplePaysli |
|             | test_skel                      |  pTemplate/0_Installable/17.0/hr_pay |
|             | TestObjects                    |  roll_community_demo_data/tests/test |
|             | test_fails                     |  _skel.py", line 7, in test_fails    |
|             |                                | ▓    self.assertTrue(False)          |
|             |                                | ▓AssertionError: False is not true   |
|             |                                | ▓                                    |
+-------------+--------------------------------+--------------------------------------+
|             | odoo                           | ▓Starting TestObjects.test_passes .. |
| SUCCESS     | addons                         |  .                                   |
|             | hr_payroll_community_demo_data |                                      |
|             | tests                          |                                      |
|             | test_skel                      |                                      |
|             | TestObjects                    |                                      |
|             | test_passes                    |                                      |
+-------------+--------------------------------+--------------------------------------+""").lstrip())
