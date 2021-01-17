# -*- coding: cp936 -*-
import arcpy,os
# 在环境临时文件夹下创建临时文件
scratch_name = arcpy.CreateScratchName("temp",data_type="Shapefile",workspace=arcpy.env.scratchFolder)
print scratch_name
# 在环境临时GDB下创建临时文件
scratch_name = arcpy.CreateScratchName("temp",data_type="Shapefile",workspace=arcpy.env.scratchGDB)
print scratch_name




