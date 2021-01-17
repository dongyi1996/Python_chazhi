# -*- coding: cp936 -*-
import arcpy, os

spatialReference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(os.getcwd(), "TestCreateHollowPolygon1.shp", "POLYGON",
                                    spatial_reference=spatialReference)
in_fc = os.getcwd() + os.sep + "TestCreateHollowPolygon1.shp"
cursor = arcpy.da.InsertCursor(in_fc, ["SHAPE@"])
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
cursor.insertRow([hollowPolygon])
del cursor
