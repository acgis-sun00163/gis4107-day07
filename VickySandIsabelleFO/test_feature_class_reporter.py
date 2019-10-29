#-------------------------------------------------------------------------------
# Name:        test_feature_class_reporter.py
# Purpose:     add suffix to feature class name
#
# Create by Chengjiaqi Sun
#
# Created:     25/10/2019
#-------------------------------------------------------------------------------

import feature_class_reporter
reload(feature_class_reporter)


def main():

    expected = 'point'
    fc_name = 'Provinces_PNT'
    actual = feature_class_reporter.get_feature_type_from_name(fc_name)
    compare_expected_and_actual(fc_name, expected, actual)

    expected = 'Polyline'
    fc_name = 'Provinces_LIN'
    actual = feature_class_reporter.get_feature_type_from_name(fc_name)
    compare_expected_and_actual(fc_name, expected, actual)


    expected = 'Polygon'
    fc_name = 'Provinces_PLY'
    actual = feature_class_reporter.get_feature_type_from_name(fc_name)
    compare_expected_and_actual(fc_name, expected, actual)


    expected = 'Unkown'
    fc_name = 'Provinces'
    actual = feature_class_reporter.get_feature_type_from_name(fc_name)
    compare_expected_and_actual(fc_name, expected, actual)



def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()