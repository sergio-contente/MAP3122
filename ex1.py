from metodos.potencias import metodo_potencia
import numpy as np
import matplotlib.pyplot as plt

def plot_aproximations(iterations, error_autovalor, error_autovetor, error_assintotico, error_assintotico_quadrado):
	pass


def main():
	x_values = []
	error_values = []
	assint_values = []
	list_x0 = []
	list_B = []
	itmax = np.random.randint(30, 71)
	for i in range(0, 3):
		value_x0 = np.random.rand()
		list_x0.append(value_x0)
		vector_x0 = np.array([[j] for j in list_x0])
		np.transpose(vector_x0)

		#value_B = np.random.rand()
		#list_B.append(value_B)
		#A = np.random.rand(10,10)
		#A_t = np.transpose(A)
		#B = np.add(A, A_t)
	A = np.array([[-2, -4, 2], [-2, 1, 2], [4, 2, 5]])
	metodo = metodo_potencia(vector_x0, A, itmax, 10)
	for i in range(1, itmax):
		x_values.append(i)
		error_values.append(metodo.autovalor_autovetor_error())
	assint_values = metodo.get_assintotico()
	print(x_values)
	print(assint_values)
	plt.yscale("log")
	plt.plot(x_values, assint_values)
	plt.show()
	#valor, vetor = metodo.get_autovetor_autovalor()
	#print(metodo.get_microk())
	pass
if __name__ == '__main__':
	main()

