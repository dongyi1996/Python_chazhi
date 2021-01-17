import arcpy, os

arcpy.CreateFeatureclass_management(os.getcwd(), "TestGetShpPoint.shp", "POINT")
arcpy.CreateFeatureclass_management(os.getcwd(), "TestGetShpPolygon.shp", "POLYGON")
descPoint = arcpy.Describe(os.getcwd() + os.sep + "TestGetShpPoint.shp")
print descPoint.shapeType
descPolygon = arcpy.Describe(os.getcwd() + os.sep + "TestGetShpPolygon.shp")
print descPolygon.shapeType
