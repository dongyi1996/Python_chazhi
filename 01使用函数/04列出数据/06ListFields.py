# -*- coding: cp936 -*-
import arcpy, os, csv

arcpy.CreateFeatureclass_management(os.getcwd(), "testListFields.shp")
in_fc = os.getcwd() + os.sep + "testListFields.shp"
arcpy.AddField_management(in_fc, "Short_T", "SHORT")
arcpy.AddField_management(in_fc, "Long_T", "LONG")
arcpy.AddField_management(in_fc, "Float_T", "FLOAT", "7", "4")
arcpy.AddField_management(in_fc, "Double_T", "DOUBLE", "18", "4")
arcpy.AddField_management(in_fc, "Text_T", "TEXT", "", "", 100)

out_csv = os.getcwd() + os.sep + "a.csv"
header = ["字段名", "类型", "长度", "精度", "小数位数"]
rows = []
try:
    for field in arcpy.ListFields(in_fc):
        row = [field.name, field.type, field.length, field.precision, field.scale]
        # 因列举字段信息获取到的字段类型和创建字段的字段类型并不一致，存在映射关系
        # 在此判断并转换后获得到的信息可以直接用于创建字段
        if row[1] == "Integer":
            row[1] = "LONG"
        elif row[1] == "SmallInteger":
            row[1] = "SHORT"
        print row
        rows.append(row)
    with open(out_csv, "wb") as f:
        f_csv = csv.writer(f)
        f_csv.writerow(header)
        f_csv.writerows(rows)
except arcpy.ExecuteError:
    print arcpy.GetMessages()

# arcpy.Delete_management(in_fc)
# arcpy.Delete_management(out_csv)
