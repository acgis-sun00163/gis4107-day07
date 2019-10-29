#-------------------------------------------------------------------------------
# Name:    test_doc_scanner.py
#
# Purpose: Test ex1 module.
#
# Author:  David Viljoen
#
# Dated:     15/10/2019
#-------------------------------------------------------------------------------

import doc_scanner
reload(doc_scanner)




def main():
    """main()"""
    expected = True
    in_text = 'aaaTx6op3fff'
    actual = doc_scanner.has_x_code(in_text)
    compare_expected_and_actual(in_text, expected, actual)

    expected = False
    in_text = 'aaax6op3fff'
    actual = doc_scanner.has_x_code(in_text)
    compare_expected_and_actual(in_text, expected, actual)

    expected = 4
    in_text = 'aaaTx6op3'
    actual = doc_scanner.get_x_code_position(in_text)
    compare_expected_and_actual(in_text, expected, actual)

    expected = -1
    in_text = 'aaax6op3fff'
    actual = doc_scanner.get_x_code_position(in_text)
    compare_expected_and_actual(in_text, expected, actual)


    expected = 4
    pattern = 'Tx'
    in_text = 'aaaTx6op3fff'
    actual = doc_scanner.get_pattern_position(pattern,in_text)
    compare_expected_and_actual(in_text, expected, actual)


    expected = -1
    pattern = 'gh'
    in_text = 'aaaTx6op3fff'
    actual = doc_scanner.get_pattern_position(pattern,in_text)
    compare_expected_and_actual(in_text, expected, actual)


def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()