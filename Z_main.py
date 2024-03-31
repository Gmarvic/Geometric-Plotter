import E_representador as rp
import D_Geometria as geo

pt0 = geo.Punto3D(0, 1, 2)
vc0 = geo.Vector3D(1, 2, 3)
cr0 = geo.CirculoCR(pt0, 10)

lista1 = [pt0, vc0, cr0]

fig1 = rp.Representador(lista1)

rp.plt.show()