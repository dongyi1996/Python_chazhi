import arcpy, os

spatialReference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(os.getcwd(), "TestCreatePolygon1.shp", "POLYGON",
                                    spatial_reference=spatialReference)
in_fc = os.getcwd() + os.sep + "TestCreatePolygon1.shp"
cursor = arcpy.da.InsertCursor(in_fc, ["SHAPE@"])
point1 = arcpy.Point(77.4349451, 37.5408265)
point2 = arcpy.Point(77.4349451, 35.7780943)
point3 = arcpy.Point(78.6384349, 35.7780943)
point4 = arcpy.Point(78.6384349, 37.5408265)
polygon = arcpy.Polygon(arcpy.Array([point1, point2, point3, point4]))
cursor.insertRow([polygon])
del cursor
