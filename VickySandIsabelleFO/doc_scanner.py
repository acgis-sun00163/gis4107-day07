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
def main():
    """main()"""

def has_x_code(in_text):
    return 'Tx6op3' in in_text

def get_X_code_position(in_text):
    ## returns the position starting count with 1
    if in_text.find("Tx6op3") ==-1:
        return -1
    else:
        return (in_text.find("Tx6op3"))+1


def get_pattern_position (pattern, in_text):
    if in_text.find (pattern)==-1:
        return -1
    else:
        return (in_text.find("Tx6op3"))+1



if __name__ == '__main__':
    main()

