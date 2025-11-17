# -*- coding: utf-8 -*-
import unittest, odoo_log_parser

class TestEchoMode_tabular(unittest.TestCase):
    """
    Test the behaviour of the method odoo_log_parser.echo_modes.tabular_digest2string() for various inputs.
    """
    maxDiff = None
    
    def test_tabular_digest2string_tabulates_failures(self):
        """
        Method run_instance_tests_and_resume() shows test failures as such.
        """
        self.assertEqual(
            odoo_log_parser.echo_modes.tabular_digest2string(
                the_digest = {
                    'adhoc-test17' : {
                        'tests_failing' : [
                                {   'test_path' : "odoo.addons.hr_payroll_community_demo_data.tests.test_skel.TestObjects.test_fails",
                                    'test_log'  : """FAIL: TestObjects.test_fails
Traceback (most recent call last):
  File "/odoo/Instances/demodevel-jj-hr-odoo17/SuiteRepos/SimplePayslipTemplate/0_Installable/17.0/hr_payroll_community_demo_data/tests/test_skel.py", line 7, in test_fails
    self.assertTrue(False)
AssertionError: False is not true
 """,
                                    },
                            ],
                        },
                    },
                term_width = 87
                ),
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
+-------------+--------------------------------+--------------------------------------+""".lstrip())
    
    def test_tabular_digest2string_tabulates_testerrors(self):
        """
        Method run_instance_tests_and_resume() shows test errors as such.
        """
        self.assertEqual(
            odoo_log_parser.echo_modes.tabular_digest2string(
                the_digest = {
                    'adhoc-test17' : {
                        'tests_errors' : [
                                {   'test_path' : "odoo.addons.test_simple_payslip_template.tests.test_action_report_simplepayslip.TestActionReportSimplePayslip.test_report_action_created_and_conditioned",
                                    'test_log'  : """ERROR: TestActionReportSimplePayslip.test_report_action_created_and_conditioned
Traceback (most recent call last):
  File "/odoo/releases/13.0/odoo/tools/cache.py", line 85, in lookup
    r = d[key]
  File "/odoo/releases/13.0/odoo/tools/func.py", line 69, in wrapper
    return func(self, *args, **kwargs)
  File "/odoo/releases/13.0/odoo/tools/lru.py", line 44, in __getitem__
    a = self.d[obj].me
KeyError: ('ir.model.data', <function IrModelData.xmlid_lookup at 0x7fc19901e040>, 'action_report_simplepayslip')

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/odoo/Instances/demodevel-jj-hr-odoo13/SuiteRepos/SimplePayslipTemplate/0_Installable/13.0/test_simple_payslip_template/tests/test_action_report_simplepayslip.py", line 12, in test_report_action_created_and_conditioned
    the_repact = self.env.ref('action_report_simplepayslip')
  File "/odoo/releases/13.0/odoo/api.py", line 504, in ref
    return self['ir.model.data'].xmlid_to_object(xml_id, raise_if_not_found=raise_if_not_found)
  File "/odoo/releases/13.0/odoo/addons/base/models/ir_model.py", line 1713, in xmlid_to_object
    t = self.xmlid_to_res_model_res_id(xmlid, raise_if_not_found)
  File "/odoo/releases/13.0/odoo/addons/base/models/ir_model.py", line 1697, in xmlid_to_res_model_res_id
    return self.xmlid_lookup(xmlid)[1:3]
  File "<decorator-gen-25>", line 2, in xmlid_lookup
  File "/odoo/releases/13.0/odoo/tools/cache.py", line 90, in lookup
    value = d[key] = self.method(*args, **kwargs)
  File "/odoo/releases/13.0/odoo/addons/base/models/ir_model.py", line 1683, in xmlid_lookup
    module, name = xmlid.split('.', 1)
ValueError: not enough values to unpack (expected 2, got 1)
 """,
                                    },
                            ],
                        },
                    },
                term_width = 101
                ),
            """
== Database: adhoc-test17
+-------------+--------------------------------------------+----------------------------------------+
| Test status | Test path                                  | Test log                               |
+-------------+--------------------------------------------+----------------------------------------+
|             | odoo                                       | ▓ERROR: TestActionReportSimplePayslip. |
| TEST ERROR  | addons                                     |  test_report_action_created_and_condit |
|             | test_simple_payslip_template               |  ioned                                 |
|             | tests                                      | ▓Traceback (most recent call last):    |
|             | test_action_report_simplepayslip           | ▓  File "/odoo/releases/13.0/odoo/tool |
|             | TestActionReportSimplePayslip              |  s/cache.py", line 85, in lookup       |
|             | test_report_action_created_and_conditioned | ▓    r = d[key]                        |
|             |                                            | ▓  File "/odoo/releases/13.0/odoo/tool |
|             |                                            |  s/func.py", line 69, in wrapper       |
|             |                                            | ▓    return func(self, *args, **kwargs |
|             |                                            |  )                                     |
|             |                                            | ▓  File "/odoo/releases/13.0/odoo/tool |
|             |                                            |  s/lru.py", line 44, in __getitem__    |
|             |                                            | ▓    a = self.d[obj].me                |
|             |                                            | ▓KeyError: ('ir.model.data', <function |
|             |                                            |   IrModelData.xmlid_lookup at 0x7fc199 |
|             |                                            |  01e040>, 'action_report_simplepayslip |
|             |                                            |  ')                                    |
|             |                                            | ▓During handling of the above exceptio |
|             |                                            |  n, another exception occurred:        |
|             |                                            | ▓Traceback (most recent call last):    |
|             |                                            | ▓  File "/odoo/Instances/demodevel-jj- |
|             |                                            |  hr-odoo13/SuiteRepos/SimplePayslipTem |
|             |                                            |  plate/0_Installable/13.0/test_simple_ |
|             |                                            |  payslip_template/tests/test_action_re |
|             |                                            |  port_simplepayslip.py", line 12, in t |
|             |                                            |  est_report_action_created_and_conditi |
|             |                                            |  oned                                  |
|             |                                            | ▓    the_repact = self.env.ref('action |
|             |                                            |  _report_simplepayslip')               |
|             |                                            | ▓  File "/odoo/releases/13.0/odoo/api. |
|             |                                            |  py", line 504, in ref                 |
|             |                                            | ▓    return self['ir.model.data'].xmli |
|             |                                            |  d_to_object(xml_id, raise_if_not_foun |
|             |                                            |  d=raise_if_not_found)                 |
|             |                                            | ▓  File "/odoo/releases/13.0/odoo/addo |
|             |                                            |  ns/base/models/ir_model.py", line 171 |
|             |                                            |  3, in xmlid_to_object                 |
|             |                                            | ▓    t = self.xmlid_to_res_model_res_i |
|             |                                            |  d(xmlid, raise_if_not_found)          |
|             |                                            | ▓  File "/odoo/releases/13.0/odoo/addo |
|             |                                            |  ns/base/models/ir_model.py", line 169 |
|             |                                            |  7, in xmlid_to_res_model_res_id       |
|             |                                            | ▓    return self.xmlid_lookup(xmlid)[1 |
|             |                                            |  :3]                                   |
|             |                                            | ▓  File "<decorator-gen-25>", line 2,  |
|             |                                            |  in xmlid_lookup                       |
|             |                                            | ▓  File "/odoo/releases/13.0/odoo/tool |
|             |                                            |  s/cache.py", line 90, in lookup       |
|             |                                            | ▓    value = d[key] = self.method(*arg |
|             |                                            |  s, **kwargs)                          |
|             |                                            | ▓  File "/odoo/releases/13.0/odoo/addo |
|             |                                            |  ns/base/models/ir_model.py", line 168 |
|             |                                            |  3, in xmlid_lookup                    |
|             |                                            | ▓    module, name = xmlid.split('.', 1 |
|             |                                            |  )                                     |
|             |                                            | ▓ValueError: not enough values to unpa |
|             |                                            |  ck (expected 2, got 1)                |
|             |                                            | ▓                                      |
+-------------+--------------------------------------------+----------------------------------------+""".lstrip())
    
    def test_tabular_digest2string_tabulates_setuperrors(self):
        """
        Method run_instance_tests_and_resume() shows setup errors as such.
        """
        self.assertEqual(
            odoo_log_parser.echo_modes.tabular_digest2string(
                the_digest = {
                    'adhoc-test17' : {
                        'setup_errors' : [
                                {   'test_path' : "odoo.addons.test_simple_payslip_template.tests.test_skel.TestObjects.setUpClass",
                                    'test_log'  : """ERROR: setUpClass (odoo.addons.test_simple_payslip_template.tests.test_skel.TestObjects)
Traceback (most recent call last):
  File "/odoo/Instances/demodevel-jj-hr-odoo13/SuiteRepos/SimplePayslipTemplate/0_Installable/13.0/test_simple_payslip_template/tests/test_skel.py", line 27, in setUpClass
    self.main_company = self.env.ref('base.main_company')
AttributeError: type object 'TestObjects' has no attribute 'env'
 """,
                                    },
                            ],
                        },
                    },
                term_width = 87
                ),
            """
== Database: adhoc-test17
+-------------+------------------------------+----------------------------------------+
| Test status | Test path                    | Test log                               |
+-------------+------------------------------+----------------------------------------+
|             | odoo                         | ▓ERROR: setUpClass (odoo.addons.test_s |
| SETUP ERROR | addons                       |  imple_payslip_template.tests.test_ske |
|             | test_simple_payslip_template |  l.TestObjects)                        |
|             | tests                        | ▓Traceback (most recent call last):    |
|             | test_skel                    | ▓  File "/odoo/Instances/demodevel-jj- |
|             | TestObjects                  |  hr-odoo13/SuiteRepos/SimplePayslipTem |
|             | setUpClass                   |  plate/0_Installable/13.0/test_simple_ |
|             |                              |  payslip_template/tests/test_skel.py", |
|             |                              |   line 27, in setUpClass               |
|             |                              | ▓    self.main_company = self.env.ref( |
|             |                              |  'base.main_company')                  |
|             |                              | ▓AttributeError: type object 'TestObje |
|             |                              |  cts' has no attribute 'env'           |
|             |                              | ▓                                      |
+-------------+------------------------------+----------------------------------------+""".lstrip())
    
    def test_tabular_digest2string_tabulates_successes(self):
        """
        Method run_instance_tests_and_resume() shows test succeses as such.
        """
        self.assertEqual(
            odoo_log_parser.echo_modes.tabular_digest2string(
                the_digest = {
                    'adhoc-test17' : {
                        'tests_succeeded' : [
                                {   'test_path' : "odoo.addons.test_simple_payslip_template.tests.test_skel.TestActionReportSimplePayslip.test_report_action_created_and_conditioned",
                                    'test_log'  : """Starting TestActionReportSimplePayslip.test_report_action_created_and_conditioned ... """,
                                    },
                            ],
                        },
                    },
                term_width = 87
                ),
            """
== Database: adhoc-test17
+-------------+--------------------------------------------+--------------------------+
| Test status | Test path                                  | Test log                 |
+-------------+--------------------------------------------+--------------------------+
|             | odoo                                       | ▓Starting TestActionRepo |
| SUCCESS     | addons                                     |  rtSimplePayslip.test_re |
|             | test_simple_payslip_template               |  port_action_created_and |
|             | tests                                      |  _conditioned ...        |
|             | test_skel                                  |                          |
|             | TestActionReportSimplePayslip              |                          |
|             | test_report_action_created_and_conditioned |                          |
+-------------+--------------------------------------------+--------------------------+""".lstrip())
