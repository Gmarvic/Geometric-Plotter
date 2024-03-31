import numpy as np

estetica={'marca':'*'}

class Punto3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def distancia(self, otro):
        return np.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2 + (self.z - otro.z)**2  )


    def __str__(self):
        mistr = 'Punto 2D' + str(self.x)
        mistr = 'Punto 2D(%f,%s,%s)' % (self.x, self.y, self.z)

        return mistr  

    def pintar_xy(self, ax0, marca='*'):
        ax0.plot(self.x, self.y, 'r.', marker=marca, label='Punto')

    def pintar_xz(self, ax0, marca='*'):
        ax0.plot(self.x, self.z, 'r.',marker=marca, label='Punto')
        

    def pintar_yz(self, ax0, marca='*'):
        ax0.plot(self.y, self.z, 'r.', marker=marca, label='Punto')

    def pintar_xyz(self, ax0, marca='*'):
        ax0.plot(self.x, self.y, self.z, marker=marca, label='Punto')    
         


class Punto2D(Punto3D, object):
    def __init__(self, x0, x1):
        super().__init__(x0, x1, 0)

class Vector3D(Punto3D):
    def modulo(self):
        self.distancia(self, Vector3D(0,0,0))

    def pintar_xy(self, ax0, *arg):
        super().pintar_xy(ax0)
        ax0.plot([0, self.x], [0, self.y], label='Vector')   

    def pintar_xz(self, ax0, *args):
        super().pintar_xz(ax0)
        ax0.plot([0, self.x], [0, self.z], label='Vector')

    def pintar_yz(self, ax0, *args):
        super().pintar_yz(ax0)
        ax0.plot([0, self.y], [0, self.z], label='Vector')    

    def pintar_xyz(self, ax0, *args):
        super().pintar_xyz(ax0)
        ax0.plot([0, self.x],[0, self.y],[0, self.z], label='Vector')



class CirculoCR(object):
    def __init__(self, centro: Punto3D, radio: np.float64):
        self.centro = centro
        self.radio = radio
        self.__secreto = '0'

    def pintar_xy(self, ax0, marca='o'):
        theta = np.linspace(0, 2*np.pi, 100)  
        x = self.centro.x + self.radio * np.cos(theta)  
        y = self.centro.y + self.radio * np.sin(theta)  
        ax0.plot(x, y, marker=marca, label='Circulo')
       
    
    def pintar_xz(self, ax0, marca='o'):
        theta = np.linspace(0, 2*np.pi, 100)  
        x = self.centro.x + self.radio * np.cos(theta)  
        z = np.full_like(x, self.centro.z)  
        ax0.plot(x, z, marker=marca, label='Circulo')
     

    def pintar_yz(self, ax0, marca='o'):
        theta = np.linspace(0, 2*np.pi, 100)  
        y = self.centro.y + self.radio * np.sin(theta)  
        z = np.full_like(y, self.centro.z)  
        ax0.plot(y, z, marker=marca, label='Circulo')
       

    def pintar_xyz(self, ax0, marca='o'):
        theta = np.linspace(0, 2*np.pi, 100)  
        x = self.centro.x + self.radio * np.cos(theta)  
        y = self.centro.y + self.radio * np.sin(theta)  
        z = np.full_like(x, self.centro.z) 
        ax0.plot(x, y, z, marker=marca, label='Circulo') 
      

    @property
    def radio(self):
        return self._R
    
    @radio.setter
    def radio(self, r):
        if r >0:
            self._R = r
        elif r< 0:
            self._R = -r    
        else:
            print("Necesito un radio positivo")  
            self._R = 1  



