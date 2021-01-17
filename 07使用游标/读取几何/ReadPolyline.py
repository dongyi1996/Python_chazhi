import arcpy, os

spatialReference = arcpy.SpatialReference(4326)
out_fc = os.getcwd() + os.sep + "TestReadPolyline.shp"
point1 = arcpy.Point(77.4349451, 37.5408265)
point2 = arcpy.Point(77.4349451, 35.7780943)
point3 = arcpy.Point(78.6384349, 35.7780943)
point4 = arcpy.Point(78.6384349, 37.5408265)
polyLine1 = arcpy.Polyline(arcpy.Array([point1, point2]))
polyLine2 = arcpy.Polyline(arcpy.Array([point2, point3]))
polyLine3 = arcpy.Polyline(arcpy.Array([point3, point4]))
polyLine4 = arcpy.Polyline(arcpy.Array([point4, point1]))
features = [polyLine1, polyLine2, polyLine3, polyLine4]
arcpy.CopyFeatures_management(features, out_fc)
arcpy.DefineProjection_management(out_fc, spatialReference)

with arcpy.da.SearchCursor(out_fc, ["OID@", "SHAPE@"]) as cursor:
    for row in cursor:
        print "Feature {0}".format(row[0])
        for array in row[1]:
            for pnt in array:
                print pnt.X, pnt.Y
