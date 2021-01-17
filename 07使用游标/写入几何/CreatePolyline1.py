import arcpy, os

spatialReference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(os.getcwd(), "TestCreatePolyline1.shp", "POLYLINE",
                                    spatial_reference=spatialReference)
in_fc = os.getcwd() + os.sep + "TestCreatePolyline1.shp"
cursor = arcpy.da.InsertCursor(in_fc, ["SHAPE@"])
point1 = arcpy.Point(77.4349451, 37.5408265)
point2 = arcpy.Point(77.4349451, 35.7780943)
point3 = arcpy.Point(78.6384349, 35.7780943)
point4 = arcpy.Point(78.6384349, 37.5408265)
polyLine1 = arcpy.Polyline(arcpy.Array([point1, point2]))
polyLine2 = arcpy.Polyline(arcpy.Array([point2, point3]))
polyLine3 = arcpy.Polyline(arcpy.Array([point3, point4]))
polyLine4 = arcpy.Polyline(arcpy.Array([point4, point1]))
cursor.insertRow([polyLine1])
cursor.insertRow([polyLine2])
cursor.insertRow([polyLine3])
cursor.insertRow([polyLine4])
del cursor
