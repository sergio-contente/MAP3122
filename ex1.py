from metodos.potencias import metodo_potencia
from metodos.common import *
import numpy as np
import matplotlib.pyplot as plt

def matrix_1():
	B = np.random.rand(10,10)
	B_t = np.transpose(B)
	A = np.add(B, B_t)
	return A
def matrix_2(n):
	B = np.random.rand(n,n)
	B_inv = np.linalg.inv(B)
	D = np.tril(np.random.random((n,n)), 0)
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
				n = 3
				A = matrix_1()
				break
			elif modo == 2:
				n = np.random.randint(5, 11)
				A = matrix_2(n)
				break
			else:
				raise ValueError("Entrada inválida!")
		except ValueError as ve:
			print(ve)

	x_values = []
	eigenvalue_error_vector = []
	eigenvector_error_vector = []
	it_max = np.random.randint(30, 71)
	vector_x0 = np.random.rand(n,1)
	metodo = metodo_potencia(vector_x0, A, it_max, n)
	true_eigenvalues, true_eigenvectors = metodo.get_eigenvalues_eigenvectors()
	for i in range(1, it_max):
		x_values.append(i)
		mu_k = metodo.update_mu_k()
		x_k = metodo.update_x_k()
		eigenvalue_error = get_eigenvalue_error(n, mu_k, true_eigenvalues)
		eigenvector_error = get_eigenvector_error(n, x_k, true_eigenvectors)
		eigenvalue_error_vector.append(eigenvalue_error)
		eigenvector_error_vector.append(eigenvector_error)
	assint_values, assint_values_squared = get_assintotico(n, true_eigenvalues, it_max)

	plot_aproximations(x_values, eigenvalue_error_vector, eigenvector_error_vector, assint_values, assint_values_squared)
	pass
if __name__ == '__main__':
	main()

