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
import phone_utils
reload(phone_utils)

def main():
    """main()"""
    expected = True
    phone_number = '203-269-9796'
    actual = phone_utils.is_valid_phone_number(phone_number)
    compare_expected_and_actual(phone_number, expected, actual)

    expected = False
    phone_number = '2032699798'
    actual = phone_utils.is_valid_phone_number(phone_number)
    compare_expected_and_actual(phone_number, expected, actual)

    expected = False
    phone_number = '203-26A-9796'
    actual = phone_utils.is_valid_phone_number(phone_number)
    compare_expected_and_actual(phone_number, expected, actual)

    expected = True
    phone_number = '203-AAA-979A'
    actual = phone_utils.phone_number_has_letter(phone_number)
    compare_expected_and_actual(phone_number, expected, actual)

    expected = False
    phone_number = '2AA-26A-9796'
    actual = phone_utils.phone_number_has_letter(phone_number)
    compare_expected_and_actual(phone_number, expected, actual)



def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
