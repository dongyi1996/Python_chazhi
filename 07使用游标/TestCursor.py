import arcpy, os

arcpy.CreateTable_management(os.getcwd(), "TestCursor.dbf")
in_table = os.getcwd() + os.sep + "TestCursor.dbf"
arcpy.AddField_management(in_table, "REMARKS", "TEXT", field_length=20)
#   Test InsertCursor
cursor = arcpy.da.InsertCursor(in_table, "Field1")
for i in range(1, 16):
    cursor.insertRow([i])
del cursor

#   Test SearchCursor
field_addDelimiters = arcpy.AddFieldDelimiters(os.getcwd(), "Field1")
sql_clause = field_addDelimiters + " < 7"
print sql_clause
sum_number = 0
with arcpy.da.SearchCursor(in_table, "*", sql_clause) as cursor:
    for row in cursor:
        sum_number += row[1]
print "The sum of 1 to 7 is " + str(sum_number)

#   Test UpdateCursor
print sql_clause
with arcpy.da.UpdateCursor(in_table, "*", sql_clause) as cursor:
    for row in cursor:
        print row[1]
        row[2] = str(row[1]) + " is smaller than 7"
        cursor.updateRow(row)

sql_clause = field_addDelimiters + " > 7"
print sql_clause
with arcpy.da.UpdateCursor(in_table, ["Field1", "REMARKS"], sql_clause) as cursor:
    for row in cursor:
        print row[0]
        row[1] = str(row[1]) + " is bigger than 7"
        cursor.updateRow(row)
