import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as py

opciones = {
    'x_min': -15,
    'x_max': 15,
    'y_min': -15,
    'y_max': 15,
    'z_min': -15,
    'z_max': 15,
}

class Representador(object):
    def __init__(self, listaElemento: list, opt=opciones) -> None:
        self.fig, self.ax = plt.subplots(2, 2, figsize=(10, 10))
        self.opt = opt
        self.ax[1, 1].axis('off')
        ax_3d = self.fig.add_subplot(2, 2, 4, projection='3d')

        for el in listaElemento:
            if hasattr(el, 'pintar_xy'):
                el.pintar_xy(self.ax[1, 0], '+')
                self.ax[1, 0].set_title("Plano XY")
                #self.ax[1, 0].legend()
            if hasattr(el, 'pintar_xz'):
                el.pintar_xz(self.ax[0, 0], '+')
                self.ax[0, 0].set_title("Plano XZ")
                self.ax[0, 0].legend()
            if hasattr(el, 'pintar_yz'):
                el.pintar_yz(self.ax[0, 1], '+')
                self.ax[0, 1].set_title("Plano YZ")
                #self.ax[0, 1].legend()
            if hasattr(el, 'pintar_xyz'):
                el.pintar_xyz(ax_3d, '+')
                self.ax[1, 1].set_title("3D Plot")
                self.configure_3d_axis(ax_3d)
       
        self.fondo()

    def configure_3d_axis(self, ax):
        if 'x_min' in self.opt and 'x_max' in self.opt:
            ax.set_xlim(self.opt['x_min'], self.opt['x_max'])
        if 'y_min' in self.opt and 'y_max' in self.opt:
            ax.set_ylim(self.opt['y_min'], self.opt['y_max'])
        if 'z_min' in self.opt and 'z_max' in self.opt:
            ax.set_zlim(self.opt['z_min'], self.opt['z_max'])

    def fondo(self):
        for el in self.ax.flatten():
            el.grid()
            el.axis('square')

        if 'x_min' in self.opt and 'x_max' in self.opt:
            self.ax[0, 0].set_xlim(self.opt['x_min'], self.opt['x_max'])   
            self.ax[1, 0].set_xlim(self.opt['x_min'], self.opt['x_max'])    
        if 'y_min' in self.opt and 'y_max' in self.opt:
            self.ax[0, 0].set_ylim(self.opt['y_min'], self.opt['y_max'])   
            self.ax[0, 1].set_xlim(self.opt['y_min'], self.opt['y_max']) 
        if 'z_min' in self.opt and 'z_max' in self.opt:
            self.ax[0, 1].set_ylim(self.opt['z_min'], self.opt['z_max'])
            self.ax[1, 0].set_ylim(self.opt['z_min'], self.opt['z_max'])


