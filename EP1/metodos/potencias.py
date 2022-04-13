import numpy as np
import matplotlib.pyplot as plt
'''
Nome: Sergio Magalhães Contente NUSP: 10792087
Nome: Jonas Gomes de Morais NUSP: 10893805
'''
class metodo_potencia:
    def __init__(self, x_0, A):
        self.x_k = x_0
        self.mu_k = 0.0
        self.matrix = A

    def update_x_k(self):
        self.x_k = np.dot(self.matrix, self.x_k)/np.linalg.norm(np.dot(self.matrix, self.x_k))
        return self.x_k

    def update_mu_k(self):
        x_k_transp = np.transpose(self.x_k)
        self.mu_k = np.dot(x_k_transp, np.dot(self.matrix, self.x_k))/np.dot(x_k_transp, self.x_k)
        return self.mu_k
    
