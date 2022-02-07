import numpy as np

class metodo_potencia:
    def __init__(self, x_0, A, n):
        self.x_k = x_0
        self.matriz = A
        self.itmax = np.random.randint(30, 71)
        self.n = n

    def get_xk(self):
        for i in range(1, self.itmax):
            self.x_k = np.dot(self.matriz, self.x_k)/np.linalg.norm((np.dot(self.matriz, self.x_k)))
        return self.x_k
    def get_microk(self):
        xk_t = np.transpose(self.get_xk())
        A_xk = np.dot(self.matriz, self.x_k)
        microk = np.dot(xk_t, A_xk)/np.dot(xk_t, self.x_k)
        return microk

    def get_autovetor_autovalor(self):
        lambdas, autovetores = np.linalg.eig(self.matriz)
        return lambdas, autovetores
