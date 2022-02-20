import numpy as np
import matplotlib.pyplot as plt

from metodos.common import *

class metodo_potencia:
    def __init__(self, x_0, A):
        self.x_k = x_0
        self.mu_k = 0.0
        self.matrix = A

    def update_x_k(self):
        #print(f"x_k b4: {self.x_k}")
        self.x_k = np.dot(self.matrix, self.x_k)/np.linalg.norm(np.dot(self.matrix, self.x_k))
        #print(f"x_k after: {self.x_k}")
        return self.x_k

    def update_mu_k(self):
        x_k_transp = np.transpose(self.x_k)
        self.mu_k = (np.dot(x_k_transp, np.dot(self.matrix, self.x_k))/np.dot(x_k_transp, self.x_k))[0][0]
        return self.mu_k
