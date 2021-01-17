import arcpy, os, random

point_list = []
for i in range(0, 100):
    point_list.append(arcpy.Point(random.randint(73, 135), random.randint(0, 90)))
out_fc = os.getcwd() + os.sep + "TestSQLPoint.shp"
pointGeometryList = []
for point in point_list:
    pointGeometryList.append(arcpy.PointGeometry(point))
arcpy.CopyFeatures_management(pointGeometryList, out_fc)
spatialReference = arcpy.SpatialReference(4326)
arcpy.DefineProjection_management(out_fc, spatialReference)
arcpy.AddField_management(out_fc, "Y", "SHORT")
arcpy.CalculateField_management(out_fc, "Y", "!shape.centroid.Y!", "PYTHON_9.3")
field_delimiters = arcpy.AddFieldDelimiters(os.getcwd(), "Y")
arcpy.AddField_management(out_fc, "CLASS", "TEXT", field_length=50)
where_clause = field_delimiters + "<=30"
with arcpy.da.UpdateCursor(out_fc, ["CLASS"], where_clause) as cursor:
    for row in cursor:
        row[0] = "Low latitude"
        cursor.updateRow(row)
