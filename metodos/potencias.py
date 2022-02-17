import numpy as np
import matplotlib.pyplot as plt
class metodo_potencia:
    def __init__(self, x_0, A, it_max, n):
        self.x_k = x_0
        self.mu_k = 0.0
        self.matrix = A
        self.it_max = it_max
        #print(f"it_max: {self.it_max}")
        self.n = n
        self.eta = self.get_assintotico()[0]

    def update_x_k(self):
        self.x_k = np.dot(self.matrix, self.x_k)/np.linalg.norm(np.dot(self.matrix, self.x_k))
        return self.x_k

    def update_mu_k(self):
        x_k_transp = np.transpose(self.x_k)
        #print(f"xktransp: {x_k_transp}")
        #A_x_k = np.dot(self.matrix, self.x_k)
        self.mu_k = np.dot(x_k_transp, np.dot(self.matrix, self.x_k))/np.dot(x_k_transp, self.x_k)
        return self.mu_k
    
    def eigenvalue_error(self):
        self.mu_k = self.update_mu_k()
        eigenvalues = self.get_eigenvector_eigenvalue()[0]
        eigenvalue_error = np.abs(self.mu_k - np.round(eigenvalues[self.n - 1])).reshape(-1)
        #print(f"eigenvalue_error: {eigenvalue_error}")
        return eigenvalue_error

    def eigenvector_error(self):
        self.x_k = self.update_x_k()
        eigenvectors = self.get_eigenvector_eigenvalue()[1]
        #print(f"eigenvector_transp: {np.transpose(eigenvectors[:, self.n - 1])}")
        #print(f"eigenvector_reshaped: {eigenvectors[:, self.n - 1].reshape(self.n,1)}")
        #print(f"x_k: {self.x_k}")
        #print(f"eigenvector-x_k: {eigenvectors[:, self.n - 1].reshape(3,1) - self.x_k}")
        eigenvector_error = np.linalg.norm(self.x_k - eigenvectors[:, self.n - 1].reshape(self.n,1)).reshape(-1)
        #print(f"eigenvector_error: {eigenvector_error}")
        return eigenvector_error

    def get_assintotico(self):
        vector = []
        squared = []
        base = 1
        eigenvalues = self.get_eigenvector_eigenvalue()[0]
        assint = np.abs(eigenvalues[self.n - 2]/eigenvalues[self.n - 1])
        for i in range(1, self.it_max):
            #print(base)
            base = base * assint
            base_squared = base**2
            vector.append(base)
            squared.append(base_squared)
        return vector, squared

    def get_eigenvector_eigenvalue(self):
        lambdas_unsorted, eigenvectors_unsorted = np.linalg.eig(self.matrix)
        #print("lunsort: ")
        #print(lambdas_unsorted)
        #print("vunsort: ")
        #print(eigenvectors_unsorted)
        lambdas_sorted = np.sort(np.abs(lambdas_unsorted))
        eigenvectors_sorted = np.empty(eigenvectors_unsorted.shape)
        for lambda_sorted in lambdas_sorted:
            for lambda_unsorted in lambdas_unsorted:
                if lambda_sorted == np.abs(lambda_unsorted):
                    eigenvector_sorted_index = np.where(lambdas_sorted == lambda_sorted)
                    eigenvector_unsorted_index = np.where(lambdas_unsorted == lambda_unsorted)
                    eigenvectors_sorted[:, eigenvector_sorted_index] = eigenvectors_unsorted[:, eigenvector_unsorted_index]
        #print("lsort: ")
        #print(lambdas_sorted)
        #print("vsort: ")
        #print(eigenvectors_sorted)
        return lambdas_sorted, eigenvectors_sorted
