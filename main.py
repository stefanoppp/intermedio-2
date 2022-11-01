import cv2
from back_propagation import Back_Propagation

def ppal():
  fotos=['1A57190.jpg',
         '1B57190.jpg',
         '2A57190.jpg',
         '2B57190.jpg']
  
  salidas=[1,0,1,0]
  
  pixeles_fotos=[]
  for foto in fotos:
    intermedio=[]
    image = cv2.imread(foto)
    for pixel in image:
      for value in pixel:
        intermedio.append(value[0])
    pixeles_fotos.append(intermedio)
    # el ultimo valor de cada array es el bias
  entradas=[[1,0,1],[0,1,1],[0,0,1]]
  salidas_2=[1,1,0]
  back=Back_Propagation(pixeles_fotos,salidas)
  back.main()
  
  # back=Back_Propagation(entradas,salidas_2)
  # back.main()
ppal()