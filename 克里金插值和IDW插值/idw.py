import geopandas
from math import radians, sin, cos, asin, sqrt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.basemap import Basemap
import fiona
from shapely.geometry import Polygon, Point


def caldis(lon1, lat1, lon2, lat2):
    a = radians(lat1-lat2)
    b = radians(lon1-lon2)
    lat1,lat2 = radians(lat1),radians(lat2)
    t = sin(a/2)**2 + cos(lat1)*cos(lat2)*sin(b/2)**2
    d = 2*asin(sqrt(t))*6378.137
    return d

def idw(lon, lat, pm, x, y):
    lstz = []
    for i in range(len(x)):
        lstd = []
        for j in range(len(lon)):
            d = caldis(lon[j],lat[j],x[i],y[i])
            lstd.append(d)
        sqdis = list(1/np.power(lstd,2))
        sumdis = np.sum(sqdis)

        z = np.sum(np.array(pm)*np.array(sqdis))/sumdis
        lstz.append(z)
    return lstz

workbook = pd.read_excel("pmdata.xlsx")
lon,lat,pm = workbook['lon'],workbook['lat'],workbook['PM2.5']

#116.362   30.7578 121.9752  35.1245
un_lon = np.linspace(116.362,121.9752,400)
un_lat = np.linspace(30.7578,35.1245,400)

xgrid,ygrid = np.meshgrid(un_lon,un_lat)

x ,y = xgrid.flatten(),ygrid.flatten()

lstz = idw(lon,lat,pm,x,y)

zgrid = np.array(lstz).reshape(xgrid.shape)

shp = fiona.open('shp/江苏省_行政边界.shp')
pol = shp.next()
polygon = Polygon(pol['geometry']['coordinates'][0][0])

#np.nan
for i in range(xgrid.shape[0]):
    for j in range(xgrid.shape[1]):
        plon = xgrid[i][j]
        plat = ygrid[i][j]
        if not polygon.contains(Point(plon,plat)):
            zgrid[i][j] = np.nan

fig,ax = plt.subplots(figsize=(6,4.5),dpi=130,facecolor='white')

base_map = Basemap(
    llcrnrlon=116.362,
    urcrnrlon=121.9752,
    llcrnrlat=30.7578,
    urcrnrlat=35.1245,
    lon_0=119,
    lat_0=33,
    ax=ax
)

base_map.drawparallels(np.arange(30,36,1),labels=[1,0,0,0],fontsize=12,ax=ax)
base_map.drawmeridians(np.arange(116,122,1),labels=[0,0,0,1],fontsize=12,ax=ax)

base_map.readshapefile('shp/江苏省_行政边界','Js',True,default_encoding='ISO-8859-1')
cp = base_map.pcolormesh(xgrid,ygrid,zgrid,cmap='Spectral_r',shading='auto')
colorbar = base_map.colorbar(cp,label='IDW')
base_map.contour(xgrid,ygrid,zgrid,colors='w')
colorbar.outline.set_edgecolor('none')
plt.axis('off')
plt.show()