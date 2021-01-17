# -*- coding: cp936 -*-
import arcpy,os

arcpy.env.overwriteOutput = True

# 坐标列表
coordinates = [[-117.196717216, 34.046944853],
               [-117.186226483, 34.046498438],
               [-117.179530271, 34.038016569],
               [-117.187454122, 34.039132605],
               [-117.177744614, 34.056765964],
               [-117.156205131, 34.064466609],
               [-117.145491191, 34.068261129],
               [-117.170825195, 34.073618099],
               [-117.186784501, 34.068149525],
               [-117.158325598, 34.03489167]]

# 在内存中创建要素类
feature_class = arcpy.CreateFeatureclass_management(
    "in_memory", "tempfc", "POINT")[0]

# 使用插入游标
with arcpy.da.InsertCursor(feature_class, ["SHAPE@XY"]) as cursor:
    # 遍历坐标列表并添加到游标
    for (x, y) in coordinates:
        cursor.insertRow([(x, y)])

# Create a FeatureSet object and load in_memory feature class
feature_set = arcpy.FeatureSet()
feature_set.load(feature_class)
feature_set.save(os.getcwd()+os.sep+"TestFeatureset.shp")


