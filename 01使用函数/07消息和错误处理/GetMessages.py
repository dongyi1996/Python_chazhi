import arcpy, os

arcpy.CreateFeatureclass_management(os.getcwd(), "testMessage.shp")
fc = os.getcwd() + os.sep + "testMessage.shp"
try:
    arcpy.AddField_management(fc, "TEST", "TEXT")
    arcpy.AddField_management(fc, "TEST", "TEXT")
except arcpy.ExecuteError:
    pass
print "Test GetMessageCount:"
messageCount = arcpy.GetMessageCount()
print messageCount
print "Test GetMessages:"
print  arcpy.GetMessages()
print "Test GetMessage:"
print  "GetMessage(0):",arcpy.GetMessage(0)
print  "GetMessage(1):",arcpy.GetMessage(1)
print  "GetMessage(2):",arcpy.GetMessage(2)
print "Test GetIDMessage:"
print "GetIDMessage(84001):",arcpy.GetIDMessage(84001)
print "GetIDMessage(999999):",arcpy.GetIDMessage(999999)
print "Test GetReturnCode:"
print "Message[1]'s ReturnCode:", arcpy.GetReturnCode(1)
print "Message[2]'s ReturnCode:", arcpy.GetReturnCode(2)
print "Test GetSeverity:"
print "Message[1]'s Severity:", arcpy.GetSeverity(1)
print "Message[2]'s Severity:", arcpy.GetSeverity(2)
print "Test GetSeverityLevel:"
print arcpy.GetSeverityLevel()
arcpy.SetSeverityLevel(1)
print arcpy.GetSeverityLevel()
print "Test GetMaxSeverity:"
print arcpy.GetMaxSeverity()
arcpy.Delete_management(fc)
