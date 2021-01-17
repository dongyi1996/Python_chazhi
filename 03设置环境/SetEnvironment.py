# -*- coding: cp936 -*-
import arcpy, os

#  获取到的结果可能为空
print arcpy.GetSystemEnvironment("TEMP")
print arcpy.GetSystemEnvironment("TMP")
print arcpy.GetSystemEnvironment("MW_TMPDIR")

# 获取默认的overwriteOutput环境值，并将overwriteOutput设为True
print arcpy.env.overwriteOutput
arcpy.env.overwriteOutput = True
print arcpy.env.overwriteOutput

# 保存当前环境设置，并将overwriteOutput设为False
arcpy.SaveSettings(os.path.join(os.path.expanduser("~"), "Desktop", "MyCustomSettings.xml"))
arcpy.env.overwriteOutput = False
print arcpy.env.overwriteOutput

# 重新读取导出的环境设置文件
arcpy.LoadSettings(os.path.join(os.path.expanduser("~"), "Desktop", "MyCustomSettings.xml"))
print arcpy.env.overwriteOutput
