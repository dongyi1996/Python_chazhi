import arcpy, os

arcpy.SetSeverityLevel(1)
#   Test ExecuteError
try:
    arcpy.GetCount_management("")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))

#   Test ExecuteWarning
try:
    arcpy.CreateFeatureclass_management(os.getcwd(), "TestExecuteShp.shp")
    arcpy.DeleteFeatures_management(os.getcwd() + os.sep + "TestExecuteShp.shp")
except arcpy.ExecuteWarning:
    print(arcpy.GetMessages(1))
arcpy.Delete_management(os.getcwd() + os.sep + "TestExecuteShp.shp")
