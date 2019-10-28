#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Isabelle
#
# Created:     25-10-2019
# Copyright:   (c) Isabelle 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import feature_class_reporter
reload(feature_class_reporter)

def main():
    """main()"""
    expected = 'Polygon'
    fc_name = 'PROVINCES_PLY'
    actual = feature_class_reporter.get_feature_type_name(fc_name)
    compare_expected_and_actual(fc_name, expected, actual)

    expected = 'Line'
    fc_name = 'STREETS_LIN'
    actual = feature_class_reporter.get_feature_type_name(fc_name)
    compare_expected_and_actual(fc_name, expected, actual)

    expected = 'Point'
    fc_name = 'Trees_PNT'
    actual = feature_class_reporter.get_feature_type_name(fc_name)
    compare_expected_and_actual(fc_name, expected, actual)

    expected = 'Unknown'
    fc_name = 'Trees_GGG'
    actual = feature_class_reporter.get_feature_type_name(fc_name)
    compare_expected_and_actual(fc_name, expected, actual)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
