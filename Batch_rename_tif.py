# -*- coding: utf-8 -*-
import re
import os
import sys
import arcpy

reload(sys)
sys.setdefaultencoding('utf-8')


def num_cvt_day_and_month(year, num):
# 输入年份year和第num天返回该天对应的月和日
    t_0 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    t_1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 != 0:
        t = t_0[:]
    else:
        t = t_1[:]
    month_r = 1
    day_r = 1
    while True:
        if num - sum(t[:month_r]) <= 0:
            day_r = num - sum(t[:month_r - 1])
            month_r = month_r
            break
        else:
            month_r += 1
            continue
    return day_r, month_r


class RenameModisFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def breakup_file_name(self):
        parts = self.file_name.split('.')
        # a = parts[0] # MOD13A3
        b = parts[1]  # A2000032
        c = parts[2]  # h26v05
        d = parts[-2]  # 1_km_monthly_NDVI
        e = parts[-1]  # .hdf or .tif
        return b, c, d, e

    def split_year_and_num(self, str_time):
        if re.match(r'A\d{4}[0-9][0-9][0-9]', str_time):
            return str_time[1:5], str_time[-3:]
        else:
            arcpy.AddMessage("请检查文件名格式是否正确")
            raise IndexError

    def cvt_new_form(self):
        data_time, data_position, others, suffix = self.breakup_file_name()
        in_year, in_num = self.split_year_and_num(data_time)
        out_day, out_month = num_cvt_day_and_month(int(in_year), int(in_num))
        new_form = 'A%sM%02dD%02d_%s_%s.%s' % (in_year, out_month, out_day, data_position, others, suffix)
        return new_form


in_rasters = arcpy.GetParameterAsText(0) 
"""
file_pahts：由全部栅格完整路径组成的列表
file_dirs:由栅格文件所在目录组成的列表
full_neams:由栅格名字组成的列表
"""
file_paths = in_rasters.split(';')  # type:list
file_dirs = []
full_names = []
for file_path in file_paths:
    file_dir, full_name = os.path.split(file_path)
    file_dirs.append(file_dir)
    full_names.append(full_name)
old_names = full_names

"""
old_names：待进行重命名的栅格文件名组成的列表
new_names：重命名后的栅格文件名组成的列表
"""
new_names = []
for old_name in old_names:
    rename = RenameModisFile(old_name)
    new_name = rename.cvt_new_form()
    new_names.append(new_name)
for i in range(len(new_names)):
    os.rename(file_dirs[i] + '\\' + old_names[i], file_dirs[i] + '\\' + new_names[i])
