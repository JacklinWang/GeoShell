import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# 读取.shp文件
data = gpd.read_file('./data/columbus.shp')

# 创建地图对象
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制地图
data.plot(ax=ax, edgecolor='white', facecolor='#C8F7C5')
# 关闭坐标轴
ax.axis('off')
# 初始化变量
last_clicked = None

# 定义鼠标点击事件处理函数
def onclick(event):
    global last_clicked

    # 获取鼠标点击位置的坐标
    x, y = event.xdata, event.ydata
    print("Clicked at x_canvas=%s, y_canvas=%s" % (x, y))
    # 如果点击的位置在地图外，则返回
    if x is None or y is None:
        return

    # 获取被点击的区域
    clicked = data[data.geometry.contains(Point(x, y))]
    print(clicked)
    # 如果没有点击到任何区域，则返回
    if clicked.empty:
        return

    # 清除之前的高亮区域
    if last_clicked is not None:
        last_clicked.plot(ax=ax, edgecolor='white', facecolor='#C8F7C5')

    # 高亮被点击的区域
    clicked.plot(ax=ax, edgecolor='black', facecolor='#004B00')

    # 保存当前点击的区域
    last_clicked = clicked


# 将鼠标点击事件处理函数注册到地图对象上
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# 显示地图
plt.show()
