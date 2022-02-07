import numpy as np

class metodo_potencia:
    def __init__(self, autovetor, A, n):
        self.autovetor = autovetor
        self.matriz = A
        self.itmax = np.random.randint(30, 71)
        self.n = n

    def get_xk(self):
        for i in range(1, self.itmax):
            self.autovetor = np.dot(self.matriz, self.autovetor)/np.linalg.norm((np.dot(self.autovetor, self.matriz)))
        return self.autovetor
        
    def get_autovetor_autovalor(self):
        lambdas, autovetores = np.linalg.eig(self.matriz)
        return lambdas, autovetores
