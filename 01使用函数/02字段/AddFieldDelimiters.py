import arcpy,os
field_name="Id"

#工作空间为文件夹
workspace=os.getcwd()
print arcpy.AddFieldDelimiters(workspace,field_name)

##实际证明添加分割方法时，只与文件的路径和后缀有关，不论是否存在。可以自行尝试。
# 工作空间为个人地理数据库，注释掉的为创建一个个人地理数据库
#arcpy.CreatePersonalGDB_management (os.getcwd(), "test.mdb")
workspace=os.getcwd()+os.sep+"test.mdb"
print arcpy.AddFieldDelimiters(workspace,field_name)

# 工作空间为文件地理数据库，注释掉的为创建一个文件地理数据库
#arcpy.CreateFileGDB_management (os.getcwd(), "test.gdb")
workspace=os.getcwd()+os.sep+"test.gdb"
print arcpy.AddFieldDelimiters(workspace,field_name)

