import math
import numpy as np
class Neurona_oculta:
    def __init__(self,pesos,entradas):
        self.pesos=pesos
        self.entradas=entradas
        self.lr=0.2
        
    def obtener_salida(self):
        prod_escalar=np.dot(self.pesos,self.entradas)
        salida_real=self.sigmoidea(prod_escalar)
        return salida_real
    
    def actualizar_pesos(self,error_capa_oculta,peso_capa_oculta):
        salida_real=self.obtener_salida()
        error=salida_real*(1-salida_real)*(error_capa_oculta*peso_capa_oculta)
        for i in range(len(self.pesos)):
            self.pesos[i]=self.pesos[i]+(self.lr*self.entradas[i]*error)
            
            
    def sigmoidea(self,prod_escalar):
        sig = 1 / (1 + math.exp(-prod_escalar))
        return sig