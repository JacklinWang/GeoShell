import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import geopandas as gpd
# .shp文件：包含实际的几何图形数据，例如点、线和面等。
# .dbf文件：包含与几何图形数据相关联的属性数据，例如名称、地址和人口等。
# .shx文件：包含了.shp文件的索引信息，以便快速访问记录。
# .prj文件：包含了坐标系和投影信息。
class readfile(object):

    def connect(self, filename):
        # 连接 SQLite 数据库
        sqlite_file = filename  # 给定的 SQLite 文件绝对路径
        conn = sqlite3.connect(sqlite_file)

        # 读取地图数据
        cur = conn.cursor()
        cur.execute("SELECT AsText(geometry) FROM your_table_name")  # 从数据表中获取几何数据
        geometry = cur.fetchone()[0]
        conn.close()

        # 提取多边形坐标
        # coords = geometry.replace('POLYGON ((', '').replace('))', '').split(',')
        # coords = [c.split(' ') for c in coords]
        # coords = [[float(c[0]), float(c[1])] for c in coords]

    def read_excel(self, filename):
        # 读取Excel文件
        data = pd.read_excel(filename)
        # 绘制地图
        fig = px.scatter_mapbox(data, lat="latitude", lon="longitude", zoom=10)
        fig.update_layout(mapbox_style="open-street-map")
        fig.show()

    def read_shp(self, filename):
        file_path = filename
        gdf = gpd.read_file(file_path)
        #fig = gdf.plot()
        # 获取绘图的Axes对象
        ax = gdf.plot(edgecolor='white', facecolor='#C8F7C5')
        # 隐藏坐标轴
        ax.set_axis_off()
        # # 获取Figure对象
        # fig = ax.get_figure()
        print(gdf.head())
        return ax, gdf
