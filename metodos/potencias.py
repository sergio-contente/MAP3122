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
        #error_autovetor = np.linalg.norm(self.get_xk() - autovetor[autovalor.size - 1])
        #print(autovetor[autovalor.size - 1])
        #print(f"iterator: {self.itmax}")
        #print(f"autovetor_error: {error_autovetor}")
        error_autovalor =np.abs(self.get_microk() - np.round(autovalor[autovalor.size - 1]))
        #error_autovalor_list = error_autovalor.tolist()
        #print(f"autovalor_error: {error_valor}")
        #print(f"microk: {self.get_microk()}")
        return error_autovalor# error_autovetor

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
        lambdas_old, autovetores = np.linalg.eig(self.matriz)
        print(f"ANTIGO LAMBDA: {lambdas_old}")
        print(f"ANTIGO VETORES: {autovetores}")
        lambdas = np.sort(np.abs(lambdas_old))
        vetores = np.empty(autovetores.shape)
        for j in range(0, lambdas_old.size):
            for i in range(0, autovetores[j].size):
                if (np.dot(self.matriz, autovetores[j][i]) - np.dot(lambdas_old[j], autovetores[j][i]) == 0).all():
                    index_lambda = lambdas.np.where(lambdas == np.abs(lambdas_old[j]))
                    vetores[index_lambda] = autovetores[i]
        print(f"NOVO LAMBDA: {lambdas}")
        print(f"NOVO VETORES: {vetores}")
        return lambdas, vetores

        #lambda_1 = lambdas[lambdas.size-1]
        #for autovetor in autovetores:
        #   if (np.dot(self.matriz, autovetor) - np.dot(lambda_key, autovetor) == 0).all():
        #       
        #
        #
        #
        #
        #
