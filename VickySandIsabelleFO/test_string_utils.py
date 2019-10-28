#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Isabelle
#
# Created:     15-10-2019
# Copyright:   (c) Isabelle 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import string_utils
reload(string_utils)

def main():
    """main()"""
    expected = 'J.S.W.'
    full_name = 'John Samuel Wobbly'
    actual = string_utils.get_initials(full_name)
    compare_expected_and_actual(full_name, expected, actual)

    expected = 'I.O.'
    full_name = 'Isabelle Ouimette'
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
