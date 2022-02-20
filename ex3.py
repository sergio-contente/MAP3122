from metodos.fatoracao_qr import fatoracao_qr
from metodos.common import *
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
	#A = np.array([[12,-51,4], [6,167,-68], [-4,24,-41]])
	#A = np.array([[4.,-14.,-12.],[-14.,10.,17.],[-12.,17.,1.]])
	A = np.array([[5. , -2.],[-2. , 8.]])
	#A = np.array([[3.,2., 4.],[2.,0.,2.],[4.,2.,3.]]) #lambdas iguais
	#A = np.array([[6. , -2., -1.],[-2. , 6., -1.],[-1., -1., 5.]])

	V_k = np.identity(A.shape[1])
	A_copy = np.array(A, copy=True)
	autovalor, autovetor = np.linalg.eig(A_copy)
	A_k = np.array(A, copy=True)
	it_max = 700
	symmetrical = is_symmetrical(A_copy)
	converged = False
	for iteration in range(1, it_max):
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
		# 	if i == (A_k.shape[0] - 1) and failed_conversion == False:
		# 		converged = True
		# 		print("CONVERGIU!")
		# if converged:
		# 	break
	
	print(f"Autovalores reais:\n{autovalor}\nAutovalores aproximados:\n{A_k}")
	print(f"Autovetores reais:\n{autovetor}\nAutovetores aproximados:\n{V_k}\nA:\n{A_copy}\nA_k:\n{A_k}")
	print(f"Return da eig:\n{np.linalg.eig(A)}")


if __name__ == '__main__':
	main()

