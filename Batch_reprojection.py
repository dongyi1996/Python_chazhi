#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import arcpy
from arcpy import env

# 允许覆盖地理处理操作
env.overwriteOutput = False

# 从外界获取的参数
raster_path = arcpy.GetParameterAsText(0)
out_coor_system = arcpy.GetParameterAsText(1)
rs_type = arcpy.GetParameterAsText(2)
c_size = arcpy.GetParameterAsText(3)
d_dir_name = arcpy.GetParameterAsText(4)

new_path_name = d_dir_name
os.makedirs(raster_path + "\\"+ new_path_name)
arcpy.AddMessage("Step1:Creating new folder named " + str(d_dir_name))
arcpy.AddMessage("Step1:Completed")


def project_batch():
    env.workspace = raster_path
    rafters = arcpy.ListRasters("*", "tif")
    for raster in rafters:
        out = "\\" + new_path_name + "\\" + "Pr_" + raster[:]
        arcpy.ProjectRaster_management(raster, out, out_coor_system, rs_type, c_size, "#", "#", "#")
        arcpy.AddMessage("Step2:Pr_"+raster[:]+"has done.")
        arcpy.SetProgressorPosition()
    arcpy.AddMessage("Step2:Completed")


arcpy.ResetProgressor()
if arcpy.CheckExtension("Spatial") == "Available":
    project_batch()
else:
    arcpy.AddMessage("Error!!! Spatial Analyst is unavailable")
