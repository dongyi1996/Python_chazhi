import arcpy, os

arcpy.CreateFolder_management(os.getcwd(), "TestFcBatch")
in_folder = os.getcwd() + os.sep + "TestFcBatch"
for i in range(20):
    arcpy.CreateTable_management(in_folder, "tt" + str(i) + ".dbf")
arcpy.env.workspace = in_folder
table_list = arcpy.ListTables()
for table in table_list:
    print table
    arcpy.AddField_management(table, "TableName", "TEXT")
    rows = arcpy.InsertCursor(table)
    for i in range(1, 26):
        row = rows.newRow()
        row.setValue('TableName', table)
        rows.insertRow(row)
    del row
    del rows
# arcpy.Delete_management(in_folder)
