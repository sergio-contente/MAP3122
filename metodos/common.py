import numpy as np
import matplotlib.pyplot as plt

def get_assintotico(n, eigenvalues, it_max):
	vector = []
	squared = []
	base = 1
	assint = np.abs(eigenvalues[n - 2]/eigenvalues[n - 1])
	for i in range(1, it_max):
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

def plot_aproximations(iterations, eigenvalue_error, eigenvector_error, error_assintotico, error_assintotico_quadrado):
	plt.yscale("log")
	plt.plot(iterations, error_assintotico, label=r'$\left|\frac{\lambda_1}{\lambda_2}\right|^k $')
	plt.plot(iterations, error_assintotico_quadrado, label=r'$\left|\frac{\lambda_1}{\lambda_2}\right|^{2k} $')
	plt.plot(iterations, eigenvalue_error, label="erro autovalor")
	plt.plot(iterations, eigenvector_error, label="erro autovetor")
	plt.legend()
	plt.show()
pass
