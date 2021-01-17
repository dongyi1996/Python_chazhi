# -*- coding: cp936 -*-
import arcpy,os
# 在环境临时文件夹下创建唯一的临时文件名
scratch_name = arcpy.CreateUniqueName("temp.shp",arcpy.env.scratchFolder)
print scratch_name
arcpy.CreateFeatureclass_management(arcpy.env.scratchFolder,"temp.shp","POLYGON")
scratch_name = arcpy.CreateUniqueName("temp.shp",arcpy.env.scratchFolder)
print scratch_name
# 在环境临时GDB下创建唯一的临时文件名
scratch_name = arcpy.CreateUniqueName("temp",arcpy.env.scratchGDB)
print scratch_name




