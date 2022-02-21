from metodos.potencias import metodo_potencia
from metodos.common import *
import numpy as np
import matplotlib.pyplot as plt

epsilon = 10**(-15)

def matrix_1(n):
	B = np.random.rand(n,n)
	B_t = np.transpose(B)
	A = B + B_t
	return A

def matrix_2(n):
	B = np.random.rand(n,n)
	B_inv = np.linalg.inv(B)
	autovalores_proximos = [10.71, 12.64, 14.86,  4.07, 11.29,  3.05, 10.12, 3.51,  6.35, 13.02]
	autovalores_distantes = [ 1.53,  9.26, 18.75, 13.88,  5.41, 10.77, 12.31, 9.78, 11.35, 10.92]
	D_prox = np.diag(np.array(autovalores_proximos))
	D_dist = np.diag(np.array(autovalores_distantes))
	A = np.matmul(np.matmul(B, D_prox),B_inv)
	return A

def main():
	while True:
		try:
			print("SELECIONE QUAL A MATRIZ DESEJA-SE APLICAR O MÉTODO: ")
			modo = int(input("1 ou 2: "))
			if modo == 1:
				n = 10
				A = matrix_1(n)
				break
			elif modo == 2:
				n = 10
				A = matrix_2(n)
				break
			else:
				raise ValueError("Entrada inválida!")
		except ValueError as ve:
			print(ve)

	it_max = 69
	converged = False
	x_values = [] #vetor com indices do eixo x do gráfico
	eigenvalue_error_vector = []
	eigenvector_error_vector = []
	vector_x0 = np.random.rand(n,1)

	true_eigenvalues, true_eigenvectors = get_sorted_eigenvalues_eigenvectors(A)

	lambda1 = true_eigenvalues[n-1]
	lambda2 = true_eigenvalues[n-2]
	x_true = true_eigenvectors[:,[n-1]]
	
	metodo = metodo_potencia(vector_x0, A)
	
	for i in range(1, it_max):
		x_values.append(i)
		mu_k = metodo.update_mu_k()
		x_k = metodo.update_x_k()

		eigenvalue_error = get_eigenvalue_error(mu_k, lambda1)
		eigenvector_error = get_eigenvector_error(x_k, x_true)
		eigenvalue_error_vector.append(eigenvalue_error)
		eigenvector_error_vector.append(eigenvector_error)
		
		if eigenvector_error <= epsilon:
			converged = True
			break

	assint_values, assint_values_squared = get_assintotico(lambda1, lambda2, x_values[len(x_values) - 1])
	
	print(f"Matrix: \n{A}\nmu_k: {mu_k} x_k:\n{x_k}")
	print(f"l1: {lambda1} l2: {lambda2} l2/l1: {lambda2/lambda1}")
	if converged:
		print(f"\nConverged before reaching it_max")
	else:
		print(f"\nDid not converge before reaching it_max")

	plot_aproximations(x_values, eigenvalue_error_vector, eigenvector_error_vector, assint_values, assint_values_squared)
	
if __name__ == '__main__':
	main()
