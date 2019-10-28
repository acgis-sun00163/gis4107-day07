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

def get_feature_type_name(fc_name):
   if fc_name.endswith('_ply'):
    return('Polygon')
   if fc_name.endswith('_PLY'):
    return('Polygon')
   if fc_name.endswith('_LIN'):
    return('Line')
   if fc_name.endswith('_lin'):
    return('Polygon')
   if fc_name.endswith('_PNT'):
    return('Point')
   if fc_name.endswith('_pnt'):
    return('Point')
   else:
    return('Unknown')