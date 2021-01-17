import arcpy, os

arcpy.CreateFeatureclass_management(os.getcwd(), "testAddFields.shp")
in_fc = os.getcwd() + os.sep + "testAddFields.shp"
in_field_csv = os.getcwd() + os.sep + "a.csv"
try:
    with open(in_field_csv) as f:
        f.readline()
        lines = f.readlines()
        for line in lines:
            field = line.rstrip("\n").split(",")
            print field
            if field[1].upper() == "SINGLE" or field[1].upper() == "FLOAT" or field[1].upper() == "DOUBLE":
                arcpy.AddField_management(in_fc, field[0], field[1], field[3], field[4])
            elif field[1].upper() == "SHORT" or field[1].upper() == "LONG":
                arcpy.AddField_management(in_fc, field[0], field[1], field[2])
            elif field[1].upper() == "STRING" or field[1].upper() == "TEXT":
                arcpy.AddField_management(in_fc, field[0], field[1], "", "", field[2])
            elif field[1].upper() == "OID" or field[1].upper() == "GEOMETRY":
                pass
            else:
                arcpy.AddField_management(in_fc, field[0], field[1])
except arcpy.ExecuteError:
    arcpy.GetMessages()
