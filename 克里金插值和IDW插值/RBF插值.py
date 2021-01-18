#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：dongyi
# datetime： 2021/1/16 20:28 
# ide： PyCharm
# env:python3.8
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeat
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from cartopy.io.shapereader import Reader
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy.interpolate import Rbf#引入径向基函数
import pandas as pd
import maskout2
from cartopy.mpl.ticker import LongitudeFormatter,LatitudeFormatter
from matplotlib import rcParams
config={"font.family":'Times New Roman',"font.size":16,"mathtext.fontset":'stix'}
rcParams.update(config)
plt.rcParams['figure.figsize']=(12,10)
shp_path=r'F:/Rpython/lp17/data/xinjiang0819.shp'
proj= ccrs.PlateCarree()  # 简写投影
filename=r'F:/Rpython/lp28/data/XJ1224.xlsx'
df=pd.read_excel(filename)#读取文件
lon=df['lon']#读取站点经度
lat=df['lat']#读取站点纬度
tem=df['h']#读取站点气温
# 创建画布
fig = plt.figure(figsize=(12,10),dpi=600)
olon=np.linspace(70,100,90)
olat=np.linspace(30,55,75)
olon,olat=np.meshgrid(olon,olat)#网格化
func=Rbf(lon,lat,tem,function='cubic')#定义径向基函数插值
tem_new=func(olon,olat)#获得插值后的网格气温
ax = fig.subplots(1, 1, subplot_kw={'projection': proj})  # 创建子图
extent=[73,97,34,50]#限定绘图范围
reader = Reader(shp_path)
enshicity = cfeat.ShapelyFeature(reader.geometries(), proj, edgecolor='k', facecolor='none')
ax.add_feature(enshicity, linewidth=0.7)#添加市界细节
ax.set_extent(extent,crs=proj)
ax.set_xticks(np.arange(extent[0],extent[1]+1,3),crs=proj)
ax.set_yticks(np.arange(extent[-2],extent[-1]+1,2),crs=proj)
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())
cs1= ax.contourf(olon,olat,tem_new,levels=np.arange(0,2000,200),cmap='gist_rainbow',extend='both')#画图cmap='Spectral_r',
cs2= ax.contour(olon,olat,tem_new,colors='red',linewidths=0.6)#画图
b=plt.colorbar(cs1,shrink=0.65,orientation='vertical',extend='both',pad=0.035,aspect=20) #orientation='horizontal'
clip1=maskout2.shp2clip(cs1,ax,r'F:/Rpython/lp17/data/xinjiang0819.shp') #白化1
clip2=maskout2.shp2clip(cs2,ax,r'F:/Rpython/lp17/data/xinjiang0819.shp') #白化2
font3={'family':'SimHei','size':8,'color':'k'}
plt.scatter(df['lon'].values,df['lat'].values,marker='o',s=6,color ="k")
for i, j, k in list(zip(df['lon'].values, df['lat'].values, df['name'].values)):
    plt.text(i-0.2,j-0.3,k,fontdict=font3)
plt.savefig('F:/Rpython/lp28/plot7.2.png',dpi=600)
plt.show()