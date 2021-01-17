# -*- coding: cp936 -*-
import arcpy,os

if arcpy.Exists(os.getcwd()+os.sep+"test.shp") :
    print "文件已存在"
else :
    arcpy.CreateFeatureclass_management(os.getcwd(),"test.shp","POLYGON")
    
desc = arcpy.Describe(os.getcwd()+os.sep+"test.shp")

# 输出文件基本名称（不含后缀，只是文件名）
print desc.baseName
# 输出数据路径（全路径+文件名+后缀）
print desc.catalogPath
# 输出文件数据类型
print desc.dataType
# 输出文件后缀
print desc.extension
# 输出文件名称（文件名+后缀）
print desc.file
# 输出文件的路径（只是路径）
print desc.path
