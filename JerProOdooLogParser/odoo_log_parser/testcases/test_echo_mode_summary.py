# -*- coding: utf-8 -*-
import unittest, odoo_log_parser

class TestEchoMode_summary(unittest.TestCase):
    """
    Test the behaviour of the method odoo_log_parser.echo_modes.summary_digest2string() for various inputs.
    """
    maxDiff = None
    
    def test_summary_digest2string(self):
        """
        Method summary_digest2string() shows the summary.
        """
        self.assertEqual(
            odoo_log_parser.echo_modes.summary_digest2string(
                the_digest = {
                    'adhoc-test17' : {
                        'tests_failing' : [
                                {   'test_path' : "odoo.addons.fake_module.tests.test_pretended.TestObjects.test_fails",
                                    'test_log'  : (
                                        "Failure log line 1\n"
                                        "Failure log line 2\n"
                                        ),
                                    },
                            ],
                        'tests_errors' : [
                                {   'test_path' : "odoo.addons.fake_module.tests.test_pretended.TestObjects.test_with_errors",
                                    'test_log'  : (
                                        "Error log line 1\n"
                                        "Error log line 2\n"
                                        ),
                                    },
                            ],
                        'tests_succeeded' : [
                                {   'test_path' : "odoo.addons.fake_module.tests.test_pretended.TestObjects.test_succeeds",
                                    'test_log'  : "Starting TestObjects.test_succeeds ... ",
                                    },
                            ],
                        },
                    },
                ), (
                    "====================================================================\n"
                    "====================================================================\n"
                    "=========== Summary for database: adhoc-test17:\n"
                    "Global status: SETUP ERRORS\n"
                    "Total number of tests: 3\n"
                    "Successful tests: 1\n"
                    "Failing tests: 1\n"
                    "Number of errors: 1\n"
                    "==================================\n"
                    "===== List of failing tests:\n"
                    "== Test path: odoo.addons.fake_module.tests.test_pretended.TestObjects.test_fails\n"
                    "Module: fake_module\n"
                    "Test case name: TestObjects\n"
                    "Test name: test_fails\n"
                    "Test Log:\n"
                    "F   Failure log line 1\n"
                    "F   Failure log line 2\n"
                    "F   \n"
                    "==================================\n"
                    "===== List of other errors:\n"
                    "== Test path: odoo.addons.fake_module.tests.test_pretended.TestObjects.test_with_errors\n"
                    "Module: fake_module\n"
                    "Test case name: TestObjects\n"
                    "Test name: test_with_errors\n"
                    "Test Log:\n"
                    "E   Error log line 1\n"
                    "E   Error log line 2\n"
                    "E   \n"
                ))
