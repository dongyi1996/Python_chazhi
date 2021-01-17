import arcpy, os

spatialReference = arcpy.SpatialReference(4326)
out_fc = os.getcwd() + os.sep + "TestReadMultiPart.shp"
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
arcpy.CopyFeatures_management(multiPart, out_fc)
arcpy.DefineProjection_management(out_fc, spatialReference)

with arcpy.da.SearchCursor(out_fc, ["OID@", "SHAPE@"]) as cursor:
    for row in cursor:
        print "Feature {0}".format(row[0])
        partnum = 0
        for part in row[1]:
            partnum += 1
            print "Part{0}:".format(partnum)
            for pnt in part:
                print pnt.X, pnt.Y
