import arcpy, os

spatialReference = arcpy.SpatialReference(4326)
out_fc = os.getcwd() + os.sep + "TestReadPolygon.shp"
point1 = arcpy.Point(77.4349451, 37.5408265)
point2 = arcpy.Point(77.4349451, 35.7780943)
point3 = arcpy.Point(78.6384349, 35.7780943)
point4 = arcpy.Point(78.6384349, 37.5408265)
polygon = arcpy.Polygon(arcpy.Array([point1, point2, point3, point4]))
arcpy.CopyFeatures_management(polygon, out_fc)
arcpy.DefineProjection_management(out_fc, spatialReference)

with arcpy.da.SearchCursor(out_fc, ["OID@", "SHAPE@"]) as cursor:
    for row in cursor:
        print "Feature {0}".format(row[0])
        for array in row[1]:
            for pnt in array:
                print pnt.X, pnt.Y
