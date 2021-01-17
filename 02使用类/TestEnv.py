import arcpy, os

print "Not defined scratchWorkspace:"
print arcpy.env.scratchWorkspace

print("Defined folder as scratchWorkspace:")
desktopFolder = os.path.join(os.path.expanduser("~"), 'Desktop')
arcpy.env.scratchWorkspace = desktopFolder
print(arcpy.env.scratchWorkspace)
