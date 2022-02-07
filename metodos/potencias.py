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
    def autovalor_autovetor_error(self):
        autovalor, autovetor = self.get_autovetor_autovalor()
        error_autovetor = np.linalg.norm(self.get_xk() - autovetor)
        print(f"autovetor_error: {error_autovetor}")
        error_valor =np.abs(self.get_microk() - autovalor[autovalor.size - 1])
        print(f"autovalor_error: {error_valor}")
        print(np.power(autovalor[autovalor.size - 2]/autovalor[autovalor.size - 1], self.itmax))

    def get_autovetor_autovalor(self):
        lambdas, autovetores = np.linalg.eig(self.matriz)
        lambdas = np.sort(np.abs(lambdas))
        return lambdas, autovetores
