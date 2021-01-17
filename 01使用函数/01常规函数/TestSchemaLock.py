# -*- coding: cp936 -*-
import arcpy,os
# 创建测试要素类
arcpy.CreateFeatureclass_management(os.getcwd(),"test.shp","POLYGON")

# 如果要素在Gis中打开会得到else的结果
if arcpy.TestSchemaLock(os.getcwd()+os.sep+"test.shp"):
    print "可以获取方案锁，可为要素添加字段！"
    arcpy.AddField_management(os.getcwd()+os.sep+"test.shp","TESTFIELD","TEXT")
else :
    print "无法获取方案锁！！！"

# 删除用于测试的要素类
#arcpy.Delete_management(os.getcwd()+os.sep+"test.shp")
