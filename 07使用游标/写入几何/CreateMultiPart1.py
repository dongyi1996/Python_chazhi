import arcpy, os

spatialReference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(os.getcwd(), "TestCreateMultiPart1.shp", "POLYGON",
                                    spatial_reference=spatialReference)
in_fc = os.getcwd() + os.sep + "TestCreateMultiPart1.shp"
cursor = arcpy.da.InsertCursor(in_fc, ["SHAPE@"])
point1 = arcpy.Point(77.4349451, 37.5408265)
point2 = arcpy.Point(77.4349451, 35.7780943)
point3 = arcpy.Point(78.6384349, 35.7780943)
point4 = arcpy.Point(78.6384349, 37.5408265)
point5 = arcpy.Point(78.8349451, 36.6408265)
point6 = arcpy.Point(78.8349451, 36.0780943)
point7 = arcpy.Point(79.2384349, 36.0780943)
point8 = arcpy.Point(79.2384349, 36.6408265)
polygon1 = arcpy.Array([point1, point2, point3, point4])
polygon2 = arcpy.Array([point5, point6, point7, point8])
multiPart = arcpy.Polygon(arcpy.Array([polygon1, polygon2]))
cursor.insertRow([multiPart])
del cursor
