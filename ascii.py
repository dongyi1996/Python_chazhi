import arcpy
import os
raster_path='E:/vic_output/sm1_tif/'
out_path='E:/vic_output/sm1_ascii/'
files = [f for f in os.listdir(raster_path) if f.endswith('TIF')]
for file in files:
    arcpy.RasterToASCII_conversion(raster_path+file, out_path+file+'.txt')
    




