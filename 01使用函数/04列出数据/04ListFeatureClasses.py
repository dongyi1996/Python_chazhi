import arcpy,os

# 创建个人地理数据库
arcpy.CreatePersonalGDB_management (os.getcwd(), "test.mdb")
# 创建MyFeatureclass1、Featureclass2、Featureclass3要素数据集
arcpy.CreateFeatureclass_management (os.getcwd()+os.sep+"test.mdb", "MyFeatureclass1","POLYGON")
arcpy.CreateFeatureclass_management (os.getcwd()+os.sep+"test.mdb", "Featureclass2","POLYGON")
arcpy.CreateFeatureclass_management (os.getcwd()+os.sep+"test.mdb", "Featureclass3","POINT")

# 列举创建的个人地理数据库中的要素类
arcpy.env.workspace = os.getcwd()+os.sep+"test.mdb"
fcs = arcpy.ListFeatureClasses()
print("All Featureclasses :")
for fc in fcs :
    print(fc)

# 列举创建的个人地理数据库中的要素类（使用通配符，只列举以My开头，要素类型为面的）
fcs = arcpy.ListFeatureClasses("My*","Polygon")
print("Starts with My and Polygon :")
for fc in fcs :
    print(fc)


# 列举创建的个人地理数据库中的点要素类 
fcs = arcpy.ListFeatureClasses("","Point")
print("Point Featureclasses :")
for fc in fcs :
    print(fc)
arcpy.Delete_management(os.getcwd()+os.sep+"test.mdb")
