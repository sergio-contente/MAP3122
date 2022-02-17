from metodos.potencias import metodo_potencia
import numpy as np
import matplotlib.pyplot as plt

def plot_aproximations(iterations, eigenvalue_error, eigenvector_error, error_assintotico, error_assintotico_quadrado):
	plt.yscale("log")
	plt.plot(iterations, error_assintotico, label=r'$\left|\frac{\lambda_1}{\lambda2}\right|^k $')
	plt.plot(iterations, error_assintotico_quadrado, label=r'$\left|\frac{\lambda_1}{\lambda2}\right|^{2k} $')
	plt.plot(iterations, eigenvalue_error, label="erro autovalor")
	plt.plot(iterations, eigenvector_error, label="erro autovetor")
	plt.legend()
	plt.show()
	pass
def matrix_1():
	B = np.random.rand(10,10)
	B_t = np.transpose(B)
	A = np.add(B, B_t)
	#print(A)
	#print(A.shape)
	return A
def matrix_2(n):
	B = np.random.rand(n,n)
	B_inv = np.linalg.inv(B)
	D = np.tril(np.random.random((n,n)), 0)
	D = np.triu(D, 0)
	#print(D)
	A = np.dot(B, D)
	A = np.dot(A, B_inv)
	#valor, vetor = np.linalg.eig(A)
	#print(valor)
	return A
def main():
	while True:
		try:
			print("SELECIONE QUAL A MATRIZ DESEJA-SE APLICAR O MÉTODO: ")
			modo = int(input("1 ou 2: "))
			if modo == 1:
				n = 10
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
		
	#A = np.array([[-2, -4, 2], [-2, 1, 2], [4, 2, 5]])
	metodo = metodo_potencia(vector_x0, A, it_max, n)
	for i in range(1, it_max):
		x_values.append(i)
		eigenvalue_error = metodo.eigenvalue_error()
		eigenvector_error = metodo.eigenvector_error()
		#eigenvalue_error = eigenvalue_error.reshape(-1)
		#eigenvector_error = eigenvector_error.reshape(-1)
		eigenvalue_error_vector.append(eigenvalue_error)
		eigenvector_error_vector.append(eigenvector_error)
	assint_values, assint_values_squared = metodo.get_assintotico()

	plot_aproximations(x_values, eigenvalue_error_vector, eigenvector_error_vector, assint_values, assint_values_squared)
	# plt.yscale("log")
	# plt.plot(x_values, assint_values, label=r'$\left|\frac{\lambda_1}{\lambda2}\right|^k $')
	# plt.plot(x_values, assint_values_squared, label=r'$\left|\frac{\lambda_1}{\lambda2}\right|^{2k} $')
	# plt.plot(x_values, eigenvalue_error_vector, label="erro autovalor")
	# plt.plot(x_values, eigenvector_error_vector, label="erro autovetor")
	# plt.legend()
	# plt.show()

	#print(f"Erro: {metodo.eta}")
	#print(metodo.get_microk())
	pass
if __name__ == '__main__':
	main()

