import arcpy, os

spatialReference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(os.getcwd(), "TestCreateMultiPoint1.shp", "MULTIPOINT",
                                    spatial_reference=spatialReference)
in_fc = os.getcwd() + os.sep + "TestCreateMultiPoint1.shp"
cursor = arcpy.da.InsertCursor(in_fc, ["SHAPE@"])
point1 = (77.4349451, 37.5408265)
point2 = (77.4349451, 35.7780943)
point3 = (78.6384349, 35.7780943)
point4 = (78.6384349, 37.5408265)
multiPoint1 = (point1, point2)
multiPoint2 = (point3, point4)
cursor.insertRow([multiPoint1])
cursor.insertRow([multiPoint2])
del cursor
