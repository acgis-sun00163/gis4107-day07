#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Isabelle
#
# Created:     15-10-2019
# Copyright:   (c) Isabelle 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def is_valid_phone_number(phone_number):
    if len(phone_number) !=12:
        return False
    for i in range(12):
        if i in [3,7]:
            if phone_number[i] != '-':
                return False
        elif not phone_number[i].isdigit():
            return False
    return True


def phone_number_has_letter(phone_number):
    if len(phone_number) !=12:
        return False
    for i in range(12):
        if i in [3,7]:
            if phone_number[i] != '-':
                return False
        if i in [0,1,2]:
            if not phone_number[i].isdigit():
                return False
        if i in [4,5,6,8,9,10,11]:
            if not phone_number[i].isalnum():
                return False
    return True