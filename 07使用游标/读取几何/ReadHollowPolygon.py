# -*- coding: cp936 -*-
import arcpy, os

spatialReference = arcpy.SpatialReference(4326)
out_fc = os.getcwd() + os.sep + "TestReadHollowPolygon.shp"
point1 = arcpy.Point(77.4349451, 37.5408265)
point2 = arcpy.Point(77.4349451, 35.7780943)
point3 = arcpy.Point(78.6384349, 35.7780943)
point4 = arcpy.Point(78.6384349, 37.5408265)
point5 = arcpy.Point(77.8349451, 36.6408265)
point6 = arcpy.Point(77.8349451, 36.0780943)
point7 = arcpy.Point(78.2384349, 36.0780943)
point8 = arcpy.Point(78.2384349, 36.6408265)
#   经测试创建孔洞多边形，只需将多个闭合环组合到一起即可，而不必刻意强调内外环点顺序和内外环顺序
#   环必须闭合
hollowPolygon = arcpy.Polygon(
    arcpy.Array([point1, point4, point3, point2, point1, point5, point6, point7, point8, point5]))
# polygon = arcpy.Polygon(
#     arcpy.Array([point1, point2, point3, point4, point1, point5, point6, point7, point8, point5]))
# polygon = arcpy.Polygon(
#     arcpy.Array([point5, point6, point7, point8, point5, point1, point4, point3, point2, point1]))
arcpy.CopyFeatures_management(hollowPolygon, out_fc)
arcpy.DefineProjection_management(out_fc, spatialReference)

with arcpy.da.SearchCursor(out_fc, ["OID@", "SHAPE@"]) as cursor:
    for row in cursor:
        print "Feature {0}".format(row[0])
        for array in row[1]:
            for pnt in array:
                #   因孔洞多边形会返回外环、空点对象、内环，这里采判断对象是否为空
                if pnt:
                    print pnt.X, pnt.Y
                else:
                    print "Empty point object!"
                    print "Interior Ring:"
