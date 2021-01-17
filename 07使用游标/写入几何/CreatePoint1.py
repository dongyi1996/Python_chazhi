import arcpy, os

spatialReference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(os.getcwd(), "TestCreatePoint1.shp", "POINT", spatial_reference=spatialReference)
in_fc = os.getcwd() + os.sep + "TestCreatePoint1.shp"
cursor = arcpy.da.InsertCursor(in_fc, ["SHAPE@"])
point1 = [(77.4349451, 37.5408265)]
point2 = [(77.4349451, 35.7780943)]
point3 = [(78.6384349, 35.7780943)]
point4 = [(78.6384349, 37.5408265)]
cursor.insertRow(point1)
cursor.insertRow(point2)
cursor.insertRow(point3)
cursor.insertRow(point4)
del cursor
