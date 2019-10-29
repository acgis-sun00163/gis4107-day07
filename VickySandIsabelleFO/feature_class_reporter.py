#----------------------------------------------------------------------------
# Name:    feature_class_reporter.py
#
# Purpose: add suffix to feature class name
#
# Created by Chengjiaqi Sun
#
# Created: 25/10/2019
#-------------------------------------------------------------------------------



''' fc_name (for the feature class name)  '''

'''return point, pointline, polygon or unknown'''


def main():

    def get_feature_type_from_name(fc_name):
        fc= fc_name.split('_')

        if fc[1].upper() == "PNT":
            print "Point"
        elif fc[1].upper() == "LIN":
            print "Polyline"
        elif fc[1].upper() == "PLY":
            print "Polygon"
        else:
            print "Unkown"



if __name__ == '__main__':
    main()


