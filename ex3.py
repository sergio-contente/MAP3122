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
	#A = np.array([[1,-1,4],[1,4,-2],[1,4,2]])
	#A = np.array([[2. , 5., 11.],[5. , 4., 17.],[11., 17., 6.]])
	A = np.array([[6. , -2., -1.],[-2. , 6., -1.],[-1., -1., 5.]])

	V_k = np.identity(A.shape[1])
	A_k = A
	it_max = 10
	symmetrical = is_symmetrical(A)
	converged = False
	for iteration in range(1, it_max):
		qr = fatoracao_qr(A_k)
		Q_k, R_k = qr.get_qr()
		if symmetrical:
			print(f"V_k * Q_k:\n{V_k}\n{Q_k}")
			V_k = np.matmul(V_k,Q_k)
			print(f"V_k:\n{V_k}")
		A_k = np.matmul(R_k,Q_k)
		failed_conversion = False
		for i in range(A_k.shape[0]):
			for j in range(A_k.shape[1]):
				if i > j and np.abs(A_k[i][j]) > epsilon:
					failed_conversion = True
					break
			if i == (A_k.shape[0] - 1) and failed_conversion == False:
				converged = True
		if converged:
			break
	autovalor, autovetor = np.linalg.eig(A_k)
	for c in range(V_k.shape[1]):
		V_k[:,[c]] = V_k[:,[c]]/np.linalg.norm(V_k[:,[c]])
		#autovetor[:, [c]] = autovetor[:, [c]]/np.linalg.norm(autovetor[:, [c]])
	
	print(f"Autovalores reais:\n{autovalor}\nAutovalores aproximados:\n{A_k}")
	print(f"Autovetores reais:\n{autovetor}\nAutovetores aproximados:\n{V_k}")
if __name__ == '__main__':
	main()

