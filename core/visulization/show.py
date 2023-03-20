import matplotlib.pyplot as plt
class visualization(object):
    def __init__(self):
        self.gdf = None
    def show_shp(self, gdf_obj):
        self.gdf = gdf_obj
        self.gdf.plot(color='green')
        return plt
