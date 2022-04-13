import numpy as np
import matplotlib.pyplot as plt
class fatoracao_qr:
	def __init__(self, A):
		self.A_0 = np.array(A, copy=True)
		self.A_k = np.array(A, copy=True)
		self.tamanho = A.shape[1]
		self.q_teste = np.array(self.A_0)
		self.R = np.array(A, copy=True)
		self.Q = np.identity(self.A_0.shape[1])

	def get_v(self, A_k):
		x = np.array(A_k[:, [0]], copy=True)
		if x[0][0] < 0:
			delta = -1
		else:
			delta = 1
		x = np.transpose(x)
		norm_x = np.linalg.norm(x)
		e = np.zeros_like(x)
		e[0][0] = 1 #retorna base canonica (1,0,0,0)
		v = x + delta*norm_x*e
		v = np.transpose(v)
		return np.array(v)

	def get_H_k(self, v):
		vt = np.transpose(v)
		vvt = np.dot(v, vt)
		vvt = vvt/(np.linalg.norm(v)**2)
		identidade = np.identity(v.shape[0])
		H = identidade - 2*vvt
		return np.array(H)

	def update_A_k(self):
		self.A_k = np.matmul(self.Q, self.R)
		return np.array(self.A_k)

	def update_Q_k(self, H_k):
		size = H_k.shape[1]
		i = self.tamanho - size
		temp = np.matmul(self.Q[i:, i:], H_k)
		self.Q[i:,i:] = np.array(temp, copy=True)
		return np.array(self.Q)

	def update_R_k(self, H_k):
		size = H_k.shape[1]
		i = self.tamanho - size
		temp = np.matmul(H_k, self.R[i:, i:])
		self.R[i:,i:] = np.array(temp, copy=True)
		return np.array(self.R)

	def get_qr(self):
		R = np.array(self.A_0, copy=True)
		for i in range(self.A_0.shape[1] - 1):
			v = self.get_v(R[i:, i:])
			H = self.get_H_k(v)
			Q = self.update_Q_k(H)
			R = self.update_R_k(H)
		return np.array(Q), np.array(R)
		