import arcpy, os

spatialReference = arcpy.SpatialReference(4326)
out_fc = os.getcwd() + os.sep + "TestReadPoint.shp"
point1 = arcpy.Point(77.434, 37.540)
point2 = arcpy.Point(77.434, 35.778)
point3 = arcpy.Point(78.638, 35.778)
point4 = arcpy.Point(78.638, 37.540)
point_list = [point1, point2, point3, point4]
pointGeometryList = []
for point in point_list:
    pointGeometryList.append(arcpy.PointGeometry(point))
arcpy.CopyFeatures_management(pointGeometryList, out_fc)
arcpy.DefineProjection_management(out_fc, spatialReference)

with arcpy.da.SearchCursor(out_fc, ["SHAPE@XY"]) as cursor:
    for row in cursor:
        print row[0]
