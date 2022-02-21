from metodos.potencias_inversas import metodo_potencias_inversas
from metodos.common import *
import numpy as np

epsilon = 10**(-15)

def matrix_1(n):
	B = np.random.rand(n,n)
	B_t = np.transpose(B)
	A = B + B_t + n*np.identity(n)
	return A

def matrix_2(n):
	p = n+2
	B_0 = np.random.rand(n,n)
	B = B_0 + p*np.identity(n)
	B_inv = np.linalg.inv(B)
	D = np.diag(np.random.random_sample(n))
	A = np.dot(np.dot(B, D),B_inv)
	return A

def main():
	while True:
		try:
			print("SELECIONE QUAL A MATRIZ DESEJA-SE APLICAR O MÉTODO: ")
			modo = int(input("1 ou 2: "))
			if modo == 1:
				n = 7
				A = matrix_1(n)#np.array([[-2,-4,2],[-2,1,2],[4,2,5]])
				break
			elif modo == 2:
				n = 5 #np.random.randint(5, 11)
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
	it_max = 50
	while True:
		vector_x0 = np.random.rand(n,1)
		if modo == 1:
			A = matrix_1(n)
			metodo = metodo_potencias_inversas(vector_x0, A)
		else:
			A = matrix_2(n)
			metodo = metodo_potencias_inversas(vector_x0, A)
		if metodo.sassenfeld_criteria() or metodo.lines_criteria():
			break
	true_eigenvalues, true_eigenvectors = get_sorted_eigenvalues_eigenvectors(np.linalg.inv(A))
	lambda1 = true_eigenvalues[n-1]
	lambda2 = true_eigenvalues[n-2]
	x_true = true_eigenvectors[:,[n-1]]
	for i in range(1, it_max):
		x_values.append(i)
		omega = metodo.optimal_omega(lambda1)
		x_k = metodo.update_x_k()
		mu_k = metodo.update_mu_k()
		eigenvalue_error = get_eigenvalue_error(mu_k, lambda1)
		#print(f"valerr: {eigenvalue_error} = {mu_k} - {lambda1}")
		eigenvector_error = get_eigenvector_error(x_k, x_true)
		#print(f"vec_error: {eigenvector_error}\nxk:\n{x_k}\nxtrue\n{x_true}")
		eigenvalue_error_vector.append(eigenvalue_error)
		eigenvector_error_vector.append(eigenvector_error)
		if eigenvector_error <= epsilon:
			converged = True
			break
	assint_values, assint_values_squared = get_assintotico(lambda1, lambda2, x_values[len(x_values) - 1])
	# if x_k[0][0] * true_eigenvectors[n-1][0] < 0:	
	# 	x_k *= -1
	
	# print(f"Matrix: \n{A}\nx_0:\n{vector_x0}\nmu_k: {mu_k} l1: {lambda1}\nx_k:\n{x_k}\nx*:\n{x_true}")
	# print(f"l1: {lambda1} l2: {lambda2} l2/l1: {lambda2/lambda1}")
	# print(f"omega: {omega} mu_k: {mu_k} lambda1: {lambda1}")
	if converged:
		print(f"\nConverged before reaching it_max")
	else:
		print(f"\nDid not converge before reaching it_max")

	plot_aproximations(x_values, eigenvalue_error_vector, eigenvector_error_vector, assint_values, assint_values_squared)
	#print(f"vals: {true_eigenvalues}\nvecs: {true_eigenvectors} ======================================================================================================")
	
if __name__ == '__main__':
	main()
