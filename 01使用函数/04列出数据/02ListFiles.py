import arcpy, os

arcpy.env.workspace = os.getcwd()
for py_file in arcpy.ListFiles("*.py"):
    print py_file
