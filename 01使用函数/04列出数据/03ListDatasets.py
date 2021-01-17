import arcpy,os

# 创建个人地理数据库
arcpy.CreatePersonalGDB_management (os.getcwd(), "test.mdb")
# 创建MyFeatureDataset1、MyFeatureDataset2、FeatureDataset3要素数据集
arcpy.CreateFeatureDataset_management (os.getcwd()+os.sep+"test.mdb", "MyFeatureDataset1")
arcpy.CreateFeatureDataset_management (os.getcwd()+os.sep+"test.mdb", "MyFeatureDataset2")
arcpy.CreateFeatureDataset_management (os.getcwd()+os.sep+"test.mdb", "FeatureDataset3")
# 在MyFeatureDataset1要素数据集中创建拓扑
arcpy.CreateTopology_management (os.getcwd()+os.sep+"test.mdb"+os.sep+"MyFeatureDataset1", "MyTopology")

# 列举创建的个人地理数据库中的要素数据集
arcpy.env.workspace = os.getcwd()+os.sep+"test.mdb"
datasets = arcpy.ListDatasets("","Feature")
for dataset in datasets :
    print(dataset)
print("")

# 列举创建的个人地理数据库中的要素数据集（使用通配符，只列举以My开头的）
datasets = arcpy.ListDatasets("My*","Feature")
for dataset in datasets :
    print(dataset)
print("")

# 列举MyFeatureDataset1要素数据集中的拓扑    
arcpy.env.workspace = os.getcwd()+os.sep+"test.mdb"+os.sep+"MyFeatureDataset1"
datasets = arcpy.ListDatasets("","Topology")
for dataset in datasets :
    print(dataset)
arcpy.Delete_management(os.getcwd()+os.sep+"test.mdb")
