import arcpy, os

spatialReference = arcpy.SpatialReference(4326)
out_fc = os.getcwd() + os.sep + "TestReadMultiPoint.shp"
point1 = arcpy.Point(77.434, 37.540)
point2 = arcpy.Point(77.434, 35.778)
point3 = arcpy.Point(78.638, 35.778)
point4 = arcpy.Point(78.638, 37.540)
multiPoint1 = arcpy.Multipoint(arcpy.Array([point1, point2]))
multiPoint2 = arcpy.Multipoint(arcpy.Array([point3, point4]))
features = [multiPoint1, multiPoint2]
arcpy.CopyFeatures_management(features, out_fc)
arcpy.DefineProjection_management(out_fc, spatialReference)

with arcpy.da.SearchCursor(out_fc, ["OID@", "SHAPE@"]) as cursor:
    for row in cursor:
        print "Feature {0}".format(row[0])
        for pnt in row[1]:
            print pnt.X, pnt.Y
