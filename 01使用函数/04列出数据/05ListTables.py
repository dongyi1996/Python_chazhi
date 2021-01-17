import arcpy, os

for i in range(5):
    arcpy.CreateTable_management(os.getcwd(), "a" + str(i))
    arcpy.CreateTable_management(os.getcwd(), "b" + str(i) + ".dbf")
arcpy.env.workspace = os.getcwd()
print "These are all tables:"
for table in arcpy.ListTables():
    print table
print "These are all dbfTables:"
for table in arcpy.ListTables("", "dBASE"):
    print table
for table in arcpy.ListTables():
    arcpy.Delete_management(os.getcwd() + os.sep + table)
