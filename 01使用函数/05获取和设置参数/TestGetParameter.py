import arcpy

print(arcpy.GetParameterCount("Buffer_analysis"))
params = arcpy.GetParameterInfo("Buffer_analysis")
i = 0
for param in params:
    print("Name: {}, Type: {}, Value: {}".format(
        param.name, param.parameterType, param.value))
    print(arcpy.GetParameterValue("Buffer_analysis", i))
    i = i + 1