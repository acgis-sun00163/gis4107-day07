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


def get_initials(full_name):

    x = []
    for i in full_name.split():
        x.append(i[0])
    result = '.' .join(x) + '.'
    return result
