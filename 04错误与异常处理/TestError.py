class NoFeatures(Exception):
    pass


import arcpy
import os
import sys
import traceback

try:
    ## part1    Test ExecuteError
    #arcpy.GetCount_management("")

    ## part2    Test raise
    # arcpy.CreateFeatureclass_management(os.getcwd(), "testError.shp")
    # result = arcpy.GetCount_management(os.getcwd() + os.sep + "testError.shp")
    # if result[0] == "0":
    #     raise NoFeatures()
    # arcpy.Delete_management(os.getcwd() + os.sep + "testError.shp")

    ##  part3   Test traceback
    x = "a" + 1
except arcpy.ExecuteError:
    msgs = arcpy.GetMessages(2)
    print(msgs)
except NoFeatures:
    print "There is no features!"
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    print(pymsg)
