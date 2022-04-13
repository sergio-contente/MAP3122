from metodos.fatoracao_qr import fatoracao_qr
from metodos.common import *
import ex1 as ex1
import numpy as np
import matplotlib.pyplot as plt
'''
Nome: Sergio Magalhães Contente NUSP: 10792087
Nome: Jonas Gomes de Morais NUSP: 10893805
'''
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
	while True:
		try:
			print("SELECIONE A QUAL CASO DO EX3 DESEJA-SE APLICAR O MÉTODO:")
			modo = int(input("1. Ex 3.1\n2. Ex 3.2\n3. Ex 3.3\n4. Ex 3.4.1 (Matriz 1 do Ex 1)\n5. Ex 3.4.2 (Matriz 2 do Ex 1)\nCaso: "))
			if modo == 1:
				A = np.array([[6. , -2., -1],[-2., 6., -1.],[-1., -1., 5.]])
				break
			elif modo == 2:
				A = np.array([[1.,1.],[-3., 1.]])
				break
			elif modo == 3:
				A = np.array([[3.,-3.],[0.33333, 5.]])
				break
			elif modo == 4:
				A = ex1.matrix_1(n)
				break
			elif modo == 5:
				A = ex1.matrix_2(n)
				break
			else:
				raise ValueError("Entrada inválida!")
		except ValueError as ve:
			print(ve)

	x_values = []
	values_errors_vector = []
	vectors_errors_vector = []
	autovalores = []
	V_k = np.identity(A.shape[1])
	A_copy = np.array(A, copy=True)
	autovalor, autovetor = get_sorted_eigenvalues_eigenvectors(A)
	A_k = np.array(A, copy=True)
	it_max = 69
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
			if i == (A_k.shape[0] - 1) and failed_conversion == False: #Se percorreu matriz inteira e nao falhou a conversao, convergiu
				converged = True
				print("CONVERGIU!")
		erro_valor = get_eigenvalue_error(A_k[0][0], autovalor[-1])
		erro_vetor = get_eigenvector_error(V_k[-1], autovetor[-1])
		values_errors_vector.append(erro_valor)
		vectors_errors_vector.append(erro_vetor)
		if converged:
			break
	for i in range(A_k.shape[0]):
		for j in range(A_k.shape[1]):
			if i == j:
				autovalores.append(A_k[i,j])
				break
	lambda1 = max(autovalores)
	index = int(np.where(autovalores == lambda1)[0])
	x_star = V_k[index]
	erro_valor = get_eigenvalue_error(lambda1, autovalor[-1])
	erro_vetor = get_eigenvector_error(x_star, autovetor[-1])
	print(f"Autovalores reais:\n{autovalor}")
	print(f"Autovalores aproximados:\n{autovalores}")
	print(f"Autovetores reais:\n{autovetor}")
	if symmetrical:
		print(f"Autovetores aproximados:\n{V_k}")
	else:
		print("A matriz nao simetrica nao permite o calculo dos autovetores pelo metodo QR")
	print(f"Erro do autovalor: {erro_valor}")
	print(f"Erro do autovetor: {erro_vetor}")

	assint_values, assint_values_squared = get_assintotico(autovalor[-1], autovalor[-2], x_values[len(x_values) - 1])
	plot_aproximations(x_values, values_errors_vector, vectors_errors_vector, assint_values, assint_values_squared)

if __name__ == '__main__':
	main()

