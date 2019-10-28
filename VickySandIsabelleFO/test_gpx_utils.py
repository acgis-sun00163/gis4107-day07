#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Isabelle
#
# Created:     25-10-2019
# Copyright:   (c) Isabelle 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import gpx_utils
reload(gpx_utils)

def main():
    """main()"""
    expected = (-75.7472631,45.3888995)
    gpx = '<trkpt lat="45.3888995" lon="-75.7472631"> '
    actual = gpx_utils.get_coods_from_gpx(gpx)
    compare_expected_and_actual(gpx, expected, actual)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()

