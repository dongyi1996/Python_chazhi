import arcpy, os

print "Not defined scratchWorkspace:"
print arcpy.env.scratchWorkspace
print arcpy.env.scratchFolder
print arcpy.env.scratchGDB

print "Defined folder as scratchWorkspace:"
desktopFolder = os.path.join(os.path.expanduser("~"), 'Desktop')
arcpy.env.scratchWorkspace = desktopFolder
print arcpy.env.scratchWorkspace
print arcpy.env.scratchFolder
print arcpy.env.scratchGDB

print "Defined GDB as scratchWorkspace:"
arcpy.CreateFileGDB_management(desktopFolder, "TestScratchWorkspace.gdb")
arcpy.env.scratchWorkspace = desktopFolder + os.sep + "TestScratchWorkspace.gdb"
print arcpy.env.scratchWorkspace
print arcpy.env.scratchFolder
print arcpy.env.scratchGDB
arcpy.Delete_management(desktopFolder + os.sep + "TestScratchWorkspace.gdb")
