import arcpy,os
scratch_name = arcpy.CreateUniqueName("temp.shp",arcpy.env.scratchFolder)
print arcpy.Exists(scratch_name)
scratch_filename = os.path.basename(scratch_name)
arcpy.CreateFeatureclass_management(arcpy.env.scratchFolder,scratch_filename,"POLYGON")
print arcpy.Exists(scratch_name)
