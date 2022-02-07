from metodos.potencias import metodo_potencia
import numpy as np

def main():
	list_x0 = []
	list_B = []
	for i in range(0, 10):
		value_x0 = np.random.rand()
		list_x0.append(value_x0)
		vector_x0 = np.array([[j] for j in list_x0])
		np.transpose(vector_x0)

		#value_B = np.random.rand()
		#list_B.append(value_B)
		A = np.random.rand(10,10)
		A_t = np.transpose(A)
		B = np.add(A, A_t)
	print(A[0])
	print(A_t[0])
	print(B[0])
	print(B.shape)

	metodo = metodo_potencia(vector_x0, A, 10)
	valor, vetor = metodo.get_autovetor_autovalor()
	
	pass
if __name__ == '__main__':
	main()

