import numpy as np
import matplotlib.pyplot as plt
class metodo_potencia:
    def __init__(self, x_0, A, it_max, n):
        self.x_k = x_0
        self.mu_k = 0.0
        self.matrix = A
        self.it_max = it_max
        self.n = n

    def update_x_k(self):
        self.x_k = np.dot(self.matrix, self.x_k)/np.linalg.norm(np.dot(self.matrix, self.x_k))
        return self.x_k

    def update_mu_k(self):
        x_k_transp = np.transpose(self.x_k)
        self.mu_k = np.dot(x_k_transp, np.dot(self.matrix, self.x_k))/np.dot(x_k_transp, self.x_k)
        return self.mu_k
    
    def get_eigenvalues_eigenvectors(self):
        lambdas_unsorted, eigenvectors_unsorted = np.linalg.eig(self.matrix)
        lambdas_sorted = np.sort(np.abs(lambdas_unsorted))
        eigenvectors_sorted = np.empty(eigenvectors_unsorted.shape)
        for lambda_sorted in lambdas_sorted:
            for lambda_unsorted in lambdas_unsorted:
                if lambda_sorted == np.abs(lambda_unsorted):
                    eigenvector_sorted_index = np.where(lambdas_sorted == lambda_sorted)
                    eigenvector_unsorted_index = np.where(lambdas_unsorted == lambda_unsorted)
                    eigenvectors_sorted[:, eigenvector_sorted_index] = eigenvectors_unsorted[:, eigenvector_unsorted_index]
        return lambdas_sorted, eigenvectors_sorted
