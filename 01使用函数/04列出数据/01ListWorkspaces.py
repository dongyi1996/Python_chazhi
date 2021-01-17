import arcpy, os

arcpy.CreatePersonalGDB_management(os.getcwd(), "testListWorkspaces0.mdb")
arcpy.CreatePersonalGDB_management(os.getcwd(), "testListWorkspaces1.mdb")
arcpy.CreateFolder_management(os.getcwd(), "testListWorkspaces2")
arcpy.CreateFileGDB_management(os.getcwd(), "testListWorkspaces3.gdb")
arcpy.CreateFileGDB_management(os.getcwd(), "testListWorkspaces4.gdb")
arcpy.env.workspace = os.getcwd()
workSpaces = arcpy.ListWorkspaces()
print "This is all workSpaces:"
workSpaces = arcpy.ListWorkspaces()
for workSpace in workSpaces:
    print  workSpace
print "This is all gdb:"
workSpaces = arcpy.ListWorkspaces("*", "FileGDB")
for workSpace in workSpaces:
    print  workSpace

workSpaces = arcpy.ListWorkspaces()
for workSpace in workSpaces:
    arcpy.Delete_management(workSpace)
