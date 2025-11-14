# -*- coding: utf-8 -*-
import unittest, os, importlib, assert_mixins
from unittest.mock import patch, Mock, MagicMock, call as mocked_call
frontend_OdooLogParser = importlib.import_module("OdooLogParser")

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')

class TestFrontend_OdooLogParser(unittest.TestCase, assert_mixins.PosixMixin):
    """
    Top-down tests the OdooLogParser.py frontend
    """
    
    def test_Main_fails_on_nonsucess_logfile(self):
        """
        Method Main() must return non-zero if the logfile contains traces
        non-successfull test.
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
    
    def test_Main_always_succeed_avoids_failing(self):
        """
        Method Main() must have a --always-succeed flag that causes it to never
        return a failure code.
        """
        filenames = [
            'odoolog_errors_in_called_by_setup.log',    'odoolog_skels_demo.log',       'odoolog_two_succeeded.log',        'odoolog_with_setup_errors.log',
            'odoolog_with_test_errors.log',             'odoolog_moddep_errors.log',    'odoolog_mod_install_errors.log',   'odoolog_wrong_version_string.log',
            ]
        for fn in filenames:
            self.assertPosixSuccess(frontend_OdooLogParser.Main("OdooLogParser.py", ['--always-succeed', '--odoolog', os.path.join(FIXTURES_DIR, fn)]))
    
    @patch('builtins.print')
    def test_Main_echo_mode_is_optionso(self, mock_print):
        """
        Flag --echo-mode is optional but tells the use that (s)he can use it.
        """
        front_retval = frontend_OdooLogParser.Main("OdooLogParser.py", [
            '--always-succeed',
            '--odoolog', os.path.join(FIXTURES_DIR, 'odoolog_two_succeeded.log'),
            ])
        mock_print.assert_called_once_with("Hint: Use the --echo-mode flag to parse the log digest.")
        self.assertPosixSuccess(front_retval)
    @patch('builtins.print')
    def test_Main_echo_mode_fails_on_crazy_mode(self, mock_print):
        """
        Flag --echo-mode causes the program to fail of an invalid mode is requested.
        """
        front_retval = frontend_OdooLogParser.Main("OdooLogParser.py", [
            '--always-succeed',
            '--echo-mode', 'this-is-an-invalid-echo-mode-name',
            '--odoolog', os.path.join(FIXTURES_DIR, 'odoolog_two_succeeded.log'),
            ])
        mock_print.assert_called_once_with("ERROR: Echo mode 'this-is-an-invalid-echo-mode-name' not found!")
        self.assertPosixFailure(front_retval)
    @patch('builtins.print')
    def test_Main_echo_mode_python_prints_python(self, mock_print):
        """
        Flag «--echo-mode python» causes the raw digest to be printed out.
        """
        front_retval = frontend_OdooLogParser.Main("OdooLogParser.py", [
            '--always-succeed',
            '--echo-mode', 'python',
            '--odoolog', os.path.join(FIXTURES_DIR, 'odoolog_two_succeeded.log'),
            ])
        mock_print.assert_called_once_with(
              f"===============================\n"
            + f"== Echoing «python»:\n"
            + f"===============================\n"
            + "{'demodevel-jj-hr-odoo13': {'setup_errors': [], 'tests_errors': [], 'tests_failing': [], 'tests_succeeded': [{'test_path': 'odoo.addons.test_simple_payslip_template.tests.test_action_report_simplepayslip.TestActionReportSimplePayslip.test_report_action_created_and_conditioned', 'test_log': 'Starting TestActionReportSimplePayslip.test_report_action_created_and_conditioned ... '}, {'test_path': 'odoo.addons.test_simple_payslip_template.tests.test_printing_payslip.TestPrintingPayslip.test_beginnings', 'test_log': 'Starting TestPrintingPayslip.test_beginnings ... '}, {'test_path': 'odoo.addons.test_simple_payslip_template.tests.test_printing_payslip.TestPrintingPayslip.test_printing_payslip', 'test_log': 'Starting TestPrintingPayslip.test_printing_payslip ... '}]}}" + "\n"
            )
        self.assertPosixSuccess(front_retval)
    
    ############################################################
    ############################################################
    ############################################################
    def setUp(self):
        pass
    @classmethod
    def setUpClass(cls):
        pass
