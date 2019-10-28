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

def get_coods_from_gpx(gpx):
    if 'trkpt' in gpx:
        split = gpx.split (" ")
        lat= split[1]
        lon= split[2]
        lat2 = filter(lambda x: x in '-.0123456789', lat)
        lon2 = filter(lambda x: x in '-.0123456789', lon)
        return float(lon2), float(lat2)

    else:
       return None
##
##    #return (gpx.split ('"'))

##    lat =[]
####    lon=[]
##    for trkpt in gpx:
##        print trkpt, gpx.attrib['lon'], gpx.attrib['lat']

