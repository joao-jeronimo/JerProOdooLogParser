import prettytable

def _wrap_and_mark_lines(src_text, available_len):
    """
    Wraps the src_text using newlines. Line continuations are indented,
    whereas line beginings are marked with a ▓ character.
        src_text        The text to wrap.
        available_len   The width available for use.
    """
    if available_len <= 0:
        raise Exception("Internal error: can't wrap with lines of 0 length or negative!")
    # Split the full text into real lines:
    src_lines = src_text.split("\n")
    # Each real line is split according to our available_len arg:
    resulting_lines = []
    for realline in src_lines:
        # Establish start of the first subline:
        subline_start = 0
        while subline_start < len(realline):
            # Establish end of the current subline:
            subline_end = min(subline_start+available_len-1, len(realline))
            # Subslice the line into a subline:
            subslice = realline[subline_start:subline_end]
            # First subline gets a ▓ char in the begining, other lines get a space:
            if subline_start == 0:
                subline = "▓" + subslice
            else:
                subline = " " + subslice
            # Collect the processed subline:
            resulting_lines.append(subline)
            # Advance the start accordingly:
            subline_start = subline_end
    # Reassemble the resulting lines:
    return "\n".join(resulting_lines)

def tabular_digest2string(the_digest, term_width=80):
        """
        Convert the test digest, as returned by the python log parsing library, into
        some readable text in a tabular format.
            the_digest      The full test digest as returned by the python log parsing library.
            term_width      Terminal width for the test output table.
        """
        def packagename_width(packname):
            """
            Returns athe minimum width of a pythons package name that is going
            to be written one element per line. See unit tests for reference
            on what this means.
                packname    A string in the form modulename.modulename.modulesme.etc.etc
            """
            packname_elems = packname.split(".")
            # The longest of the elements is the minimum space that hot to be
            # reserved for the column.
            return max([
                len(elem)
                for elem in packname_elems
                ])
        ### Intro configuration:
        prettytab = prettytable.PrettyTable()
        prettytab.align = "l"
        #######################################################
        #### One table for each Database:     #################
        #######################################################
        ret_string = ""
        for instancename in the_digest.keys():
            
            db_digest = the_digest[instancename]
            ### Setup column labels and calculate column widths:
            # Col 1:
            col1_lbl = "Test status"
            col1_width = len(col1_lbl)
            # Col 2:
            col2_lbl = "Test path"
            col2_lengths = list()
            col2_lengths.append( len(col2_lbl) )
            if 'setup_errors' in db_digest:
                col2_lengths.extend([
                    packagename_width(testinfo["test_path"])
                    for testinfo in db_digest['setup_errors']
                    ])
            if 'tests_errors' in db_digest:
                col2_lengths.extend([
                    packagename_width(testinfo["test_path"])
                    for testinfo in db_digest['tests_errors']
                    ])
            if 'tests_failing' in db_digest:
                col2_lengths.extend([
                    packagename_width(testinfo["test_path"])
                    for testinfo in db_digest['tests_failing']
                    ])
            if 'tests_succeeded' in db_digest:
                col2_lengths.extend([
                    packagename_width(testinfo["test_path"])
                    for testinfo in db_digest['tests_succeeded']
                    ])
            col2_width = max(col2_lengths)
            # Col 3:
            col3_lbl = "Test log"
            col3_width = (term_width - (2 + col1_width + 3 + col2_width + 3 + 2))
            ### Insert data in table:
            # Headers
            prettytab.field_names = [col1_lbl, col2_lbl, col3_lbl]
            # List the setup errors:
            for testinfo in db_digest.get('setup_errors', []):
                # Add it to the table:
                prettytab.add_row([
                    "\nSETUP ERROR",
                    testinfo["test_path"].replace(".", "\n"),
                    _wrap_and_mark_lines(testinfo["test_log"], col3_width),
                    ], divider=True)
            # List the tests that terminated with errors:
            for testinfo in db_digest.get('tests_errors', []):
                # Add it to the table:
                prettytab.add_row([
                    "\nTEST ERROR",
                    testinfo["test_path"].replace(".", "\n"),
                    _wrap_and_mark_lines(testinfo["test_log"], col3_width),
                    ], divider=True)
            # List the failed tests:
            for testinfo in db_digest.get('tests_failing', []):
                # Add it to the table:
                prettytab.add_row([
                    "\nFAIL",
                    testinfo["test_path"].replace(".", "\n"),
                    _wrap_and_mark_lines(testinfo["test_log"], col3_width),
                    ], divider=True)
            # List the failed tests:
            for testinfo in db_digest.get('tests_succeeded', []):
                # Add it to the table:
                prettytab.add_row([
                    "\nSUCCESS",
                    testinfo["test_path"].replace(".", "\n"),
                    _wrap_and_mark_lines(testinfo["test_log"], col3_width),
                    ], divider=True)
            # Convert encapsulated data to table:
            db_tab_string = (
                f"== Database: {instancename}\n"
                f"{prettytab.get_string()}"
                )
            # Accomulate the table to be returned in the end:
            ret_string += db_tab_string
        return ret_string
