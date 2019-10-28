#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Isabelle
#
# Created:     28-10-2019
# Copyright:   (c) Isabelle 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def get_e_or_w(dms_record):
    dms_one = dms_record.replace('\n', '')
    if 'w' in dms_one or 'W' in dms_one:
        return 'W'
    elif 'e' in dms or 'E' in dms_one:
        return 'E'

def get_n_or_s(dms_record):
    dms_one = dms_record.replace('\n', '')
    if 'n' in dms_one or 'n' in dms_one:
        return 'N'
    elif 's' in dms or 'S' in dms_one:
        return 'S'

def dms2dd(dms_record):
    dmslist = dms_record.split(' ')
    lond = float(dmslist[0])
    lonm = float(dmslist[1])
    lons = float(dmslist[2])
    latd = float(dmslist[4])
    latm = float (dmslist[5])
    lats = float(dmslist[6])

    if (lond <= 180 and lond >=0) and (lonm <= 60 and lonm >= 0) and (lons<= 60 and lons >=0) and (latd <= 180 and latd >=0) and (latm <= 60 and latm >= 0) and (lats<= 60 and lats >=0):
        latdecmin = float(latm/60)
        latdecsec = float(lats/3600)
        londecmin = float (lonm/60)
        londecsec = float (lons/3600)
        BIG_LON = str(round((lond +londecmin + londecsec),5))
        BIG_LAT = str(round((latd +latdecmin + latdecsec), 5))
        BIG_DD = BIG_LAT + ', ' + BIG_LON

        if get_n_or_s(dms_record) == 'S' or get_e_or_w(dms_record) == 'W':
            if get_n_or_s(dms_record) == 'S':
                S_LAT = '-' + BIG_LAT
            else:
                S_LAT = BIG_LAT

            if get_e_or_w(dms_record) == 'W':
                W_LON = '-' + BIG_LON
            else:
                W_LON = BIG_LON
            return W_LON +', ' + S_LAT
        else:
            return BIG_DD
    else:
        return None


