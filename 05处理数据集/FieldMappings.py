# -*- coding: cp936 -*-
import arcpy, os, random

#   创建输入表
arcpy.CreateTable_management(os.getcwd(), "TestFieldMap.dbf")
in_table = os.getcwd() + os.sep + "TestFieldMap.dbf"

#   添加RoadID和年度字段
arcpy.AddField_management(in_table, "RoadID", "TEXT", field_length=20)
for i in range(2009, 2020):
    arcpy.AddField_management(in_table, "Y" + str(i), "SHORT")

#   向表中插入行
rows = arcpy.InsertCursor(in_table)
field_list = arcpy.ListFields(in_table, "Y*")
for i in range(1, 100):
    row = rows.newRow()
    row.setValue("RoadID", "Road" + str(i))
    for field in field_list:
        row.setValue(field.name, random.choice(range(30, 1000)))
    rows.insertRow(row)
    del row
del rows

#   创建FieldMap对象，并设置输入字段、合并规则、输出字段
fm1 = arcpy.FieldMap()
fm1.mergeRule = "Mean"
for field in field_list:
    fm1.addInputField(in_table, field.name)
f_name = fm1.outputField
f_name.name = "MeanCount"
fm1.outputField = f_name

#   将fm1和fm1添加到创建的FieldMap对象fms中
fms = arcpy.FieldMappings()
fm2 = arcpy.FieldMap()
fm2.addInputField(in_table, "RoadID")
fms.addFieldMap(fm2)
fms.addFieldMap(fm1)

#   使用表至表工具并利用设置的字段映射将表转出
arcpy.TableToTable_conversion(in_table, os.getcwd(), "TestFieldMapOut.dbf", "", fms)
