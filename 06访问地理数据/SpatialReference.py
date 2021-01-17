# -*- coding:cp936 -*-
import arcpy, os

#   测试地理坐标系
print u"测试地理坐标系"
spatialReference = arcpy.SpatialReference(4326)
arcpy.CreateFeatureclass_management(os.getcwd(), "TestGeographicSpatialReference.shp",
                                    spatial_reference=spatialReference)
desc = arcpy.Describe(os.getcwd() + os.sep + "TestGeographicSpatialReference.shp")
desc_spatialReference = desc.spatialReference
print u"空间参考名称：{0}\n空间参考类型：{1}\n工厂代码：{2}".format(desc_spatialReference.name, desc_spatialReference.type,
                                                 desc_spatialReference.factoryCode)

#   测试投影坐标系
print u"测试投影坐标系"
spatialReference = arcpy.SpatialReference(4545)
arcpy.CreateFeatureclass_management(os.getcwd(), "TestProjectedSpatialReference.shp",
                                    spatial_reference=spatialReference)
desc = arcpy.Describe(os.getcwd() + os.sep + "TestProjectedSpatialReference.shp")
desc_spatialReference = desc.spatialReference
print u"空间参考名称：", desc_spatialReference.name
print u"空间参考类型：", desc_spatialReference.type
print u"工厂代码：", desc_spatialReference.factoryCode
print u"地理坐标系代码：", desc_spatialReference.GCSCode
print u"地理坐标系名称：", desc_spatialReference.GCSName
print u"投影坐标系代码：", desc_spatialReference.PCSCode
print u"投影坐标系名称：", desc_spatialReference.PCSName
print u"投影坐标系中央经线：", desc_spatialReference.centralMeridian
print u"投影代码：", desc_spatialReference.projectionCode
print u"投影名称：", desc_spatialReference.projectionName
