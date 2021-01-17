# -*- coding: cp936 -*-
import arcpy,os
## 创建测试要素类
arcpy.CreateFeatureclass_management(os.getcwd(),"test.shp","POLYGON")
## 由于字段名不规范，下面语句会报错：ERROR 000310: 字段名称不能以数字开头，可自行尝试
##arcpy.AddField_management(os.getcwd()+os.sep+"test.shp","111","TEXT")

validateFieldName=arcpy.ValidateFieldName("x-45",os.getcwd()+os.sep+"test.shp")
arcpy.AddField_management(os.getcwd()+os.sep+"test.shp",validateFieldName,"TEXT")

validateFieldName=arcpy.ValidateFieldName("111",os.getcwd()+os.sep+"test.shp")
arcpy.AddField_management(os.getcwd()+os.sep+"test.shp",validateFieldName,"TEXT")

# 删除用于测试的要素类
#arcpy.Delete_management(os.getcwd()+os.sep+"test.shp")
