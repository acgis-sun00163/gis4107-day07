#-------------------------------------------------------------------------------
# Name:    test_string_utils.py
#
#
#
# Created by Chengjiaqi Sun
#
# Dated:     15/10/2019
#-------------------------------------------------------------------------------

import string_utils
reload(string_utils)


def main():
    """main()"""
    expected = 'J.S.W.'
    full_name = 'John Samuel Wobbly'
    actual = string_utils.get_initials(full_name)
    compare_expected_and_actual(full_name, expected, actual)

    expected = 'D.M.'
    full_name = 'Dylan McDermott'
    actual = string_utils.get_initials(full_name)
    compare_expected_and_actual(full_name, expected, actual)

    expected = 'N.Y.'
    full_name = 'Nora Young '
    actual = string_utils.get_initials(full_name)
    compare_expected_and_actual(full_name, expected, actual)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()