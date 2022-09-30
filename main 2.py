import numpy as np
import math
import matplotlib.pyplot as plt
class Perceptron:
    def __init__(self,pesos,entradas,salidas):
        self.pesos=pesos
        self.entradas=entradas
        self.salidas=salidas
        self.lr=0.4
        self.tolerancia=4
        self.actualizaciones=0
        
    def obtener_valores(self):
        for i in range(len(self.entradas)):
            for j in range(len(self.entradas[i])):
                if self.entradas[i][j]==0:
                    self.entradas[i][j]=-1
        
        for i in range(len(self.salidas)):
            if self.salidas[i]==0:
                self.salidas[i]=-1
    
    def actualizar(self):
            i=0
            while i in range(len(self.entradas)):        
                salida_obtenida=np.dot(self.pesos,self.entradas[i])
                if salida_obtenida<0:
                    salida_obtenida=-1
                else:
                    salida_obtenida=1
                    
                error=self.salidas[i]-salida_obtenida
                
                if error==0:
                    self.tolerancia-=1
                    i+=1
                    if self.tolerancia==0:
                        print("Nuevos pesos: ",self.pesos)
                        print("Iteraciones: ",self.actualizaciones)
        
                else:
                    for j in range(len(self.entradas[i])):
                        self.pesos[j]=self.pesos[j]+(self.lr*error*self.entradas[i][j])
                    self.actualizaciones+=1
                    self.tolerancia=4
                    i=0
                    
        
np_matrix_pesos=np.array([0.6473185,0.37817776,0.33160055]) 
np_matrix_entradas=np.array([[1,1,1],[1,1,0],[1,0,1],[1,0,0]]) 
np_matrix_salidas=np.array([1,0,0,0]) 
and_perceptor=Perceptron(np_matrix_pesos,np_matrix_entradas,np_matrix_salidas)
if __name__=="__main__":
    
    and_perceptor.obtener_valores()
    and_perceptor.actualizar()