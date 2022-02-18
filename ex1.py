from metodos.potencias import metodo_potencia
import numpy as np
import matplotlib.pyplot as plt

def plot_aproximations(iterations, eigenvalue_error, eigenvector_error, error_assintotico, error_assintotico_quadrado):
	pass

def main():
	n = 3
	x_values = []
	eigenvalue_error_vector = []
	eigenvector_error_vector = []
	list_B = []
	it_max = 31 #np.random.randint(30, 71)
	vector_x0 = np.random.rand(n,1)
		#value_B = np.random.rand()
		#list_B.append(value_B)
		#A = np.random.rand(10,10)
		#A_t = np.transpose(A)
		#B = np.add(A, A_t)
	A = np.array([[-2, -4, 2], [-2, 1, 2], [4, 2, 5]])
	metodo = metodo_potencia(vector_x0, A, it_max, n)
	for i in range(1, it_max):
		x_values.append(i)
		eigenvalue_error = metodo.eigenvalue_error()
		eigenvector_error = metodo.eigenvector_error()
		#eigenvalue_error = eigenvalue_error.reshape(-1)
		#eigenvector_error = eigenvector_error.reshape(-1)
		eigenvalue_error_vector.append(eigenvalue_error)
		eigenvector_error_vector.append(eigenvector_error)
	assint_values = metodo.get_assintotico()
	plt.yscale("log")
	plt.plot(x_values, assint_values, label=r'$\left|\frac{\lambda_1}{\lambda2}\right|^k $')
	plt.plot(x_values, eigenvalue_error_vector, label="erro autovalor")
	plt.plot(x_values, eigenvector_error_vector, label="erro autovetor")
	plt.legend()
	plt.show()

	print(f"Erro: {metodo.eta}")
	#print(metodo.get_microk())
	pass
if __name__ == '__main__':
	main()

