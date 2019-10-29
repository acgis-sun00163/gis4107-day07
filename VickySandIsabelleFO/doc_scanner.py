#-------------------------------------------------------------------------------
# Name:        doc_scanner.py
# Purpose:     check the string inside the parameter or not
#
# Create by Chengjiaqi Sun
#
# Dated:     15/10/2019
#-------------------------------------------------------------------------------

global in_text

global pattern

def main():
    pass


def has_x_code(in_text):
    return 'Tx6op3' in in_text


'''return the bollean value, using signle line to replace
  if  :
    return True
 else
 return False'''



'''to return the position in the string
This function will associate 1 with the first character in in_text
If the code is not found, this function will return -1'''


'''element t is searched, using index function
find the pattern if exists in the text, if it exists, start count from 1
if not return -1'''
def get_x_code_position(in_text):
    if in_text.find('Tx6op3') > -1:
        return in_text.find('Tx6op3') + 1
    else:
        return -1




'''this function will associate 1 with the first character in in_text.
If the pattern is not found, this function will return -1'''

'''find function will return number and position

passed means the code are correcct'''

def get_pattern_position(pattern,in_text):
    if in_text.find(pattern) > -1:
        return in_text.find('Tx6op3') + 1
    else:
        return -1


if __name__ == '__main__':
    main()



