from re import A
from xmlrpc.client import MAXINT
from metodos.potencias import metodo_potencia
from metodos.common import *
import numpy as np
import matplotlib.pyplot as plt

epsilon = 10**(-15)

def matrix_1(n):
	B = np.random.rand(n,n)
	B_t = np.transpose(B)
	A = np.add(B, B_t)
	return A
def matrix_2(n):
	B = np.random.rand(n,n)
	B_inv = np.linalg.inv(B)
	D = np.tril(np.abs(np.random.random((n,n))), 0)
	D = np.triu(D, 0)
	A = np.dot(B, D)
	A = np.dot(A, B_inv)
	return A
def main():
	while True:
		try:
			print("SELECIONE QUAL A MATRIZ DESEJA-SE APLICAR O MÉTODO: ")
			modo = int(input("1 ou 2: "))
			if modo == 1:
				n = 10
				A = matrix_1(n)#np.array([[-2,-4,2],[-2,1,2],[4,2,5]])
				break
			elif modo == 2:
				n = np.random.randint(5, 11)
				A = matrix_2(n)
				break
			else:
				raise ValueError("Entrada inválida!")
		except ValueError as ve:
			print(ve)

	converged = False
	x_values = []
	eigenvalue_error_vector = []
	eigenvector_error_vector = []
	it_max = 69
	vector_x0 = np.random.rand(n,1)
	true_eigenvalues, true_eigenvectors = get_sorted_eigenvalues_eigenvectors(A)
	metodo = metodo_potencia(vector_x0, A)
	for i in range(1, it_max):
		x_values.append(i)
		mu_k = metodo.update_mu_k()
		x_k = metodo.update_x_k()
		eigenvalue_error = get_eigenvalue_error(n, mu_k, true_eigenvalues)
		eigenvector_error = get_eigenvector_error(x_k, true_eigenvectors[:,[n-1]])
		print(f"vec_error: {eigenvector_error}")
		eigenvalue_error_vector.append(eigenvalue_error)
		eigenvector_error_vector.append(eigenvector_error)
		if eigenvector_error <= epsilon:
			converged = True
			break
	assint_values, assint_values_squared = get_assintotico(n, true_eigenvalues, x_values[len(x_values) - 1])
	if x_k[0][0] * true_eigenvectors[0][0] < 0:
		x_k *= -1
	
	print(f"Matrix: \n{A}\nx_0:\n{vector_x0}\nmu_k: {mu_k} l1: {true_eigenvalues[n-1]}\nx_k:\n{x_k}\nx*:\n{true_eigenvectors[:,[n-1]]}")
	print(f"l1: {true_eigenvalues[n-1]} l2: {true_eigenvalues[n-2]} l2/l1: {true_eigenvalues[n-2]/true_eigenvalues[n-1]}")
	if converged:
		print(f"\nConverged before reaching it_max")
	else:
		print(f"\nDid not converge before reaching it_max")

	plot_aproximations(x_values, eigenvalue_error_vector, eigenvector_error_vector, assint_values, assint_values_squared)
	
if __name__ == '__main__':
	main()

