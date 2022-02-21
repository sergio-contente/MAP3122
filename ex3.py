from metodos.fatoracao_qr import fatoracao_qr
from metodos.common import *
import ex1
import numpy as np
import matplotlib.pyplot as plt

epsilon = 10**(-15)

def matrix_1():
	B = np.random.rand(10,10)
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
	n = 8
	#A = np.array([[5.,-2.],[-2, 8.]])
	#A = np.array([[6. , -2., -1],[-2., 6., -1.],[-1., -1., 5.]])
	#A = np.array([[1.,1.],[-3., 1.]])
	#A = np.array([[3.,-3.],[0.33333, 5.]])
	#A = matrix_1()
	A = ex1.main()
	x_values = []
	values_errors_vector = []
	vectores_errors_vector = []
	V_k = np.identity(A.shape[1])
	A_copy = np.array(A, copy=True)
	autovalor, autovetor = get_sorted_eigenvalues_eigenvectors(A)
	A_k = np.array(A, copy=True)
	it_max = 70
	symmetrical = is_symmetrical(A_copy)
	converged = False
	for iteration in range(1, it_max):
		x_values.append(iteration)
		qr = fatoracao_qr(A_k)
		Q_k, R_k = qr.get_qr()
		if symmetrical:
			V_k = np.matmul(V_k, Q_k)
		A_k = np.matmul(R_k,Q_k)
		failed_conversion = False
		for i in range(A_k.shape[0]):
			for j in range(A_k.shape[1]):
				if i > j and np.abs(A_k[i][j]) > epsilon:
					failed_conversion = True
					break
			if i == (A_k.shape[0] - 1) and failed_conversion == False:
				converged = True
				print("CONVERGIU!")
		erro_valor = get_eigenvector_error(A_k[0][0], autovalor[-1])
		erro_vetor = get_eigenvector_error(V_k, autovetor)
		values_errors_vector.append(erro_valor)
		vectores_errors_vector.append(erro_vetor)
		if converged:
			break
	erro_valor = get_eigenvector_error(A_k[0][0], autovalor[-1])
	erro_vetor = get_eigenvector_error(V_k, autovetor)
	print(f"Autovalores reais:\n{autovalor}\nAutovalores aproximados:\n{A_k}")
	print(f"Autovetores reais:\n{autovetor}\nAutovetores aproximados:\n{V_k}")
	print(f"Erro autovalores: {erro_valor}")
	print(f"erro_vetor: {erro_vetor}")

	assint_values, assint_values_squared = get_assintotico(autovalor[-1], autovalor[-2], x_values[len(x_values) - 1])
	plot_aproximations(x_values, values_errors_vector, vectores_errors_vector, assint_values, assint_values_squared)


if __name__ == '__main__':
	main()

