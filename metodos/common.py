import numpy as np
import matplotlib.pyplot as plt

def get_assintotico(n, eigenvalues, it_max):
	vector = []
	squared = []
	base = 1
	assint = np.abs(eigenvalues[n - 2]/eigenvalues[n - 1])
	for i in range(0, it_max):
		base = base * assint
		base_squared = base**2
		vector.append(base)
		squared.append(base_squared)
	return vector, squared

def get_eigenvalue_error(n, mu_k, eigenvalues):
	eigenvalue_error = np.abs(mu_k - np.round(eigenvalues[n - 1])).reshape(-1)
	return eigenvalue_error

def get_eigenvector_error(n, x_k, eigenvectors):
	eigenvector_error = np.linalg.norm(x_k - eigenvectors[:, n - 1].reshape(n,1)).reshape(-1)
	return eigenvector_error

def get_sorted_eigenvalues_eigenvectors(matrix):
        lambdas_unsorted, eigenvectors_unsorted = np.linalg.eig(matrix)
        lambdas_sorted = np.sort(np.abs(lambdas_unsorted))
        eigenvectors_sorted = np.empty(eigenvectors_unsorted.shape)
        for lambda_sorted in lambdas_sorted:
            for lambda_unsorted in lambdas_unsorted:
                if lambda_sorted == np.abs(lambda_unsorted):
                    eigenvector_sorted_index = np.where(lambdas_sorted == lambda_sorted)
                    eigenvector_unsorted_index = np.where(lambdas_unsorted == lambda_unsorted)
                    eigenvectors_sorted[:, eigenvector_sorted_index] = eigenvectors_unsorted[:, eigenvector_unsorted_index]
        return lambdas_sorted, eigenvectors_sorted

def plot_aproximations(iterations, eigenvalue_error, eigenvector_error, error_assintotico, error_assintotico_quadrado):
	plt.yscale("log")
	plt.plot(iterations, error_assintotico, label=r'$\left|\frac{\lambda_1}{\lambda_2}\right|^k $')
	plt.plot(iterations, error_assintotico_quadrado, label=r'$\left|\frac{\lambda_1}{\lambda_2}\right|^{2k} $')
	plt.plot(iterations, eigenvalue_error, label="erro autovalor")
	plt.plot(iterations, eigenvector_error, label="erro autovetor")
	plt.legend()
	plt.show()
pass

def is_symmetrical(matrix):
	print(matrix)
	for i in range(matrix.shape[0]):
		for j in range(matrix.shape[1]):
			if i != j and matrix[i][j] != matrix[j][i]:
				print(f"NÃO É SIMÉTRICA!")
				return False
	return True

def grau_med_max(eps):
	vector = np.zeros(16)
	total = 0
	grau_max = 0
	for i in range(16):
		for line in eps:
			for vec in line:
				if i == vec:
					vector[i] += 1
					total += 1
	avg = total/16
	for grau in vector:
		if grau > grau_max:
			grau_max = grau
	return avg, grau_max