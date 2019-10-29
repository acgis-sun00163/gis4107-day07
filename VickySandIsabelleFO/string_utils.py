#-------------------------------------------------------------------------------
# Name:    string_utils.py
#
# Purpose:  Get initials function
#
# Created by Chengjiaqi Sun
#
# Dated:     15/10/2019
#-------------------------------------------------------------------------------


'''Using function split and append to get the initials,
append function igore the number of names,three words or two words'''

def get_initials(full_name):

    l = []
    for i in full_name.split():
        l.append(i[0])
    result = '.'.join(l) +'.'
    return result


