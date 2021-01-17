import arcpy
arcpy.AddMessage("This is a Message!")
arcpy.AddWarning("This is an Warning!")
arcpy.AddError("This is an Error!")
arcpy.AddIDMessage("ERROR", 12, "This is an IDMessage!")
try:    
    result = arcpy.GetCount_management("c:/data/rivers.shp")
except:    
    # Return Geoprocessing tool specific errors
    #
    for msg in range(0, arcpy.GetMessageCount()):
        if arcpy.GetSeverity(msg) == 2:
            arcpy.AddReturnMessage(msg)


