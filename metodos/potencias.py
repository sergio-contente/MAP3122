import numpy as np
import matplotlib.pyplot as plt
class metodo_potencia:
    def __init__(self, x_0, A, itmax, n):
        self.x_k = x_0
        self.matriz = A
        self.itmax = itmax
        print(f"itmax: {self.itmax}")
        self.n = n

    def get_xk(self):
        self.x_k = np.dot(self.matriz, self.x_k)/np.linalg.norm((np.dot(self.matriz, self.x_k)))
        return self.x_k
    def get_microk(self):
        xk_t = np.transpose(self.get_xk())
        A_xk = np.dot(self.matriz, self.x_k)
        microk = np.dot(xk_t, A_xk)/np.dot(xk_t, self.x_k)
        return microk
    def autovalor_autovetor_error(self):
        autovalor, autovetor = self.get_autovetor_autovalor()
        error_autovetor = np.linalg.norm(self.get_xk() - autovetor[autovalor.size - 1])
        print(autovetor[autovalor.size - 1])
        #print(f"iterator: {self.itmax}")
        #print(f"autovetor_error: {error_autovetor}")
        error_autovalor =np.abs(self.get_microk() - np.round(autovalor[autovalor.size - 1]))
        #error_autovalor_list = error_autovalor.tolist()
        #print(f"autovalor_error: {error_valor}")
        #print(f"microk: {self.get_microk()}")
        return error_autovalor, error_autovetor

    def get_assintotico(self):
        vetor = []
        base = 1
        autovalores = self.get_autovetor_autovalor()[0]
        assint = np.abs(autovalores[autovalores.size - 2]/autovalores[autovalores.size - 1])
        #print(np.power(assint, self.itmax))
        for i in range(1, self.itmax):
            #print(base)
            base = base * assint
            vetor.append(base)
        return vetor

    def get_autovetor_autovalor(self):
        lambdas, autovetores = np.linalg.eig(self.matriz)
        lambdas = np.sort(np.abs(lambdas))
        return lambdas, autovetores

