
import arcpy
arcpy.CheckOutExtension("spatial")

arcpy.env.workspace = r"E:\my_data\data"#���ù����ռ�
inRas = arcpy.Raster("test.tif")desc = arcpy.Describe(inRas)#դ�����������Ϣ
sr = desc.SpatialReference#��ȡ�ռ�ο�
cell_size = inRas.meanCellWidth#һ��դ��Ϊ�����Σ����դ��ߴ���meanCellWidth��ʾlowerLeft = arcpy.Point(inRas.extent.XMin, inRas.extent.YMin)
lowerLeft = arcpy.Point(inRas.extent.XMin, inRas.extent.YMin)#��ȡ���½ǵ�����
Raster_Array = arcpy.RasterToNumPyArray(inRas)#��դ��������飬һ��д�㷨�Ļ�������ô��
row = DEM_Array.shape[0]#դ������
col = DEM_Array.shape[1]#դ������
#������Raster_Arrayд��դ������
out_raster = arcpy.NumPyArrayToRaster(Raster_Array, lowerLeft, cell_size, cell_size, -9999)
arcpy.DefineProjection_management(out_raster, sr)#д��ռ�ο�
out_raster.save("shuchu.tif")#����������
