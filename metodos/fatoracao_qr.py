import numpy as np
import matplotlib.pyplot as plt

class fatoracao_qr:
	def __init__(self, A):
		self.A_k = A
		self.tamanho = len(self.A_k)
		self.H_k = 0.0
	# def update_H_k(self):
	# 	return None
	def get_v(self, A_k):
		x = A_k[:, [0]]
		x = np.transpose(x)
		#print(x)
		norm_x = np.linalg.norm(x)
		#print(norm_x)
		y = np.eye(1, self.tamanho, 0)
		#print(y)
		v = (norm_x * y) - x
		#print(v)
		return v
	def get_vvt(self, v):
		vt = np.transpose(v)
		#print(vt)
		vt_v = np.dot(vt, v)
		vt_v = vt_v/np.linalg.norm(vt_v)
		#print(vt_v)
		return vt_v
	def get_H_k(self, A_k):
		v = self.get_v(A_k)
		vvt = self.get_vvt(v)
		identidade = np.identity(self.tamanho)
		H = identidade - 2*vvt
		return H
	def get_A_anterior(self, Q):
		R = np.dot(Q ,self.A_k)
		print(R)
		return R
	def get_Q(self, H):
		q = 1
		for H_k in H:
			q = q * H_k
		return q
	def update_A_k(self, A_ant):
		self.A_k = np.delete(A_ant, [0], 1)
		return self.A_k
