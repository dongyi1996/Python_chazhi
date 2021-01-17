import arcpy

arcpy.ImportToolbox(r"C:\Users\Admin\Desktop\GetParameter\GetParameter.tbx")
print(arcpy.GetParameterCount("TestGetParameter"))
params = arcpy.GetParameterInfo("TestGetParameter")
i = 0
for param in params:
    print("Name: {}, Type: {}, Value: {}".format(
        param.name.encode('gb2312'), param.parameterType, param.value))
    print(arcpy.GetParameterValue("TestGetParameter", i))
    i = i + 1
