import arcpy, os

arcpy.env.workspace = r'D:\huangtu\8km_data\8KM_NDVI\isnull_nodata'


# list all folders in a directory

rasters = arcpy.ListRasters("*.tif")
for raster in rasters:
    print raster

name = r"D:\huangtu\8km_data\8KM_NDVI\NDVI82_15.tif"
arcpy.CompositeBands_management(rasters, name)

print "Processing complete"
