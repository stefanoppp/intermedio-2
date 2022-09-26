import numpy as np
import math
import matplotlib.pyplot as plt
class Perceptron:
    def __init__(self,pesos,entradas,salidas):
        self.pesos=pesos
        self.entradas=entradas
        self.salidas=salidas
        self.lr=0.1

    def balanceo_peso(self):
        errores=[]
        cant_errores=4
        iteraciones=0
        while cant_errores!=0:
            for i in range(len(self.entradas)):
                prod_escalar=np.dot(self.entradas[i],self.pesos)
                salida_obtenida=self.sigmoidea(prod_escalar)
                error=(self.salidas[i]-salida_obtenida)

                if error<=0.1:
                    cant_errores=cant_errores-1
                else:
                    delta=salida_obtenida*(1-salida_obtenida)*error
                    delta_peso=self.lr*self.entradas[i]*delta
                    self.pesos=self.pesos+delta_peso
                    cant_errores=4
                iteraciones+=1
        print("Pesos finales") 
        print(self.pesos)
        print("Errores")
        print(errores)
                                              
            
    def sigmoidea(self,salida_obtenida):
        sig = 1/(1 + math.exp(-salida_obtenida))
        return sig

np_matrix_pesos=np.array([0.9,0.66,-0.2])
np_matrix_entradas=np.array([[1,0,1],[1,1,1],[0,1,0],[0,1,1]])
np_matrix_salidas=np.array([0,1,0,0])
and_perceptor=Perceptron(np_matrix_pesos,np_matrix_entradas,np_matrix_salidas)
if __name__=="__main__":
    
    print(and_perceptor.balanceo_peso())
    
    # contador=0
    # pesos=[]
    # peso1=[]
    # peso2=[]
    # peso3=[]
    # while contador<100:
    #     print(and_perceptor.balanceo_peso())
    #     # pesos_balanceados=and_perceptor.balanceo_peso()
    #     # pesos.append(pesos_balanceados)
    #     contador+=1
        
        
    # for peso in pesos:
    #     for j in peso:
    #         count=0
    #         for k in j:
    #             if count==0:
    #                 peso1.append(k)
    #             if count==1:
    #                 peso2.append(k)
    #             if count==2:
    #                 peso3.append(k)
    #             count+=1 
    # print(peso1)
    # print(peso2) 
    # plt.plot(peso1,'g')
    # plt.plot(peso2,'r')
    # plt.plot(peso3,'k')
    # plt.show()