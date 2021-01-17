import arcpy
# Get the spatial reference from the tool dialog.
txt_param = arcpy.GetParameterAsText(1)
spatial_ref = arcpy.GetParameter(0)
option_param = arcpy.GetParameterAsText(2)

# Display ArgumentCount
arcpy.AddMessage("ArgumentCount is: {0}".format(arcpy.GetArgumentCount()))
# Display txt_param
arcpy.AddMessage("txt_param is: {0}".format(txt_param))
# Display the Spatial Reference properties
arcpy.AddMessage("Name is: {0}".format(spatial_ref.name))
arcpy.AddMessage("Type is: {0}".format(spatial_ref.type))
arcpy.AddMessage("Factory code is: {0}".format(spatial_ref.factoryCode))
