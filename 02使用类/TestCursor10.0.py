import arcpy, os

arcpy.CreateTable_management(os.getcwd(), "TestCursor.dbf")
in_table = os.getcwd() + os.sep + "TestCursor.dbf"
arcpy.AddField_management(in_table, "REMARKS", "TEXT", field_length=20)
#   Test InsertCursor
rows = arcpy.InsertCursor(in_table)
for i in range(1, 16):
    row = rows.newRow()
    row.setValue("Field1", i)
    rows.insertRow(row)
del row
del rows

#   Test SearchCursor
field_addDelimiters = arcpy.AddFieldDelimiters(os.getcwd(), "Field1")
sql_clause = field_addDelimiters + " < 7"
print sql_clause
sum_number = 0
rows = arcpy.SearchCursor(in_table, sql_clause)
for row in rows:
    sum_number += row.getValue("Field1")
print "The sum of 1 to 7 is " + str(sum_number)
del row
del rows

#   Test UpdateCursor
print sql_clause
rows = arcpy.UpdateCursor(in_table, sql_clause)

for row in rows:
    print row.getValue("Field1")
    row.setValue("REMARKS", str(row.getValue("Field1")) + " is smaller than 7")
    rows.updateRow(row)
del row
del rows

sql_clause = field_addDelimiters + " > 7"
print sql_clause
rows = arcpy.UpdateCursor(in_table, sql_clause, ["Field1", "REMARKS"])

row = rows.next()
while row:
    print row.getValue("Field1")
    row.setValue("REMARKS", str(row.getValue("Field1")) + " is bigger than 7")
    rows.updateRow(row)
    row = rows.next()
del row
del rows
