import prettytable

def _summary_for_db(dbdata):
    test_result_class = dbdata.keys()
    ### Count things that exist:
    # The total number of tests:
    count_tests_total = 0
    for tc in test_result_class:
        # Accomulate all tests from thins class:
        count_tests_total += len( dbdata[tc] )
    # The number of sucesses, failures and errors:
    count_tests_success = len(dbdata['tests_succeeded'])
    count_tests_failures = len(dbdata['tests_failing'])
    count_tests_errors = len(dbdata['tests_errors'])
    # Whether there are non-successes:
    non_successes = ( count_tests_total - count_tests_success )
    # The global status:
    if non_successes == 0:
        global_status = 'ALL SUCCEEDED'
    if count_tests_failures > 0:
        global_status = 'FAILURES'
    if count_tests_errors > 0:
        global_status = 'SETUP ERRORS'
    else:
        global_status = 'OTHER ERRORS'
    ### Compute the final explanation:
    ret_acc = ""
    # Grand totals for this database:
    ret_acc += (
        f"Global status: {global_status}\n"
        f"Total number of tests: {count_tests_total}\n"
        f"Successful tests: {count_tests_success}\n"
        f"Failing tests: {count_tests_failures}\n"
        f"Number of errors: {count_tests_errors}\n"
        )
    # Info about failures:
    ret_acc += (
        f"==================================\n"
        f"===== List of failing tests:\n"
        )
    for tf in dbdata['tests_failing']:
        ret_acc += (
            f"== Test path: {tf['test_path']}\n"
            f"Module: {tf['test_path'].split('.')[2]}\n"
            f"Test case name: {tf['test_path'].split('.')[-2]}\n"
            f"Test name: {tf['test_path'].split('.')[-1]}\n"
            f"Test Log:\n"
            )
        for logline in tf['test_log'].split('\n'):
            ret_acc += ( f"F   {logline}\n" )
    # Info about errors:
    ret_acc += (
        f"==================================\n"
        f"===== List of other errors:\n"
        )
    for terr in dbdata['tests_errors']:
        ret_acc += (
            f"== Test path: {terr['test_path']}\n"
            f"Module: {terr['test_path'].split('.')[2]}\n"
            f"Test case name: {terr['test_path'].split('.')[-2]}\n"
            f"Test name: {terr['test_path'].split('.')[-1]}\n"
            f"Test Log:\n"
            )
        for logline in terr['test_log'].split('\n'):
            ret_acc += ( f"E   {logline}\n" )
    return ret_acc

def summary_digest2string(the_digest, term_width=87):
        """
        Computes a test summary for easy reading:
        """
        report_acc = ""
        ### One summary for each database:
        dbs_in_test = the_digest.keys()
        for dbn in dbs_in_test:
            # The header:
            report_acc += f"====================================================================\n"
            report_acc += f"====================================================================\n"
            report_acc += f"=========== Summary for database: {dbn}:\n"
            # The report for this DB:
            report_acc += _summary_for_db(the_digest[dbn])
        return report_acc
