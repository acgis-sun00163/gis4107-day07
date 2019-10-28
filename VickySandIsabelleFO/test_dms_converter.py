#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Isabelle
#
# Created:     28-10-2019
# Copyright:   (c) Isabelle 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import dms_converter
reload(dms_converter)

def main():
    """main()"""
    expected = 'W'
    dms_record = '075 45 03 w 45 23 05 n/n'
    actual = dms_converter.get_e_or_w(dms_record)
    compare_expected_and_actual(dms_record, expected, actual)

    expected = 'N'
    dms_record = '075 45 03 w 45 23 05 n/n'
    actual = dms_converter.get_n_or_s(dms_record)
    compare_expected_and_actual(dms_record, expected, actual)

    expected = '-75.75083, 45.38472'
    dms_record = '075 45 03 w 45 23 05 n/n'
    actual = dms_converter.dms2dd(dms_record)
    compare_expected_and_actual(dms_record, expected, actual)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
