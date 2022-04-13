from math import sqrt
import numpy as np
from metodos.common import *
'''
Nome: Sergio Magalhães Contente NUSP: 10792087
Nome: Jonas Gomes de Morais NUSP: 10893805
'''
class metodo_potencias_inversas:
	def __init__(self, x_0, A):
		self.n = len(A)
		self.x_k = x_0
		self.mu_k = 0.0
		self.inv_matrix_x_k_product = np.zeros_like(x_0)
		self.matrix = np.array(A)
		self.omega = 0.5

	def update_x_k(self):
		self.inv_matrix_x_k_product = SOR(self.matrix, self.x_k, self.omega)
		self.x_k = self.inv_matrix_x_k_product/np.linalg.norm(self.inv_matrix_x_k_product)
		return np.array(self.x_k)
	
	def update_mu_k(self):
		x_k_transp = np.transpose(self.x_k)
		self.mu_k = np.dot(x_k_transp, self.inv_matrix_x_k_product)/np.dot(x_k_transp, self.x_k)
		return np.array(self.mu_k)

	def sassenfeld_criteria(self):
		criteria = True
		betas = []
		n = len(self.matrix)
		for line in range(n):
			beta = 0
			for column in range (n ):
				if (line != column and line == 0) or line < column:
					beta += np.abs(self.matrix[line][column])
				elif line != column and line != 0:
					beta += np.abs(self.matrix[line][column])
			beta /= self.matrix[line][line]
			betas.append(beta)
		max_beta = max(betas)
		if max_beta >= 1:
			criteria = False
		return criteria
		
	def lines_criteria(self):
		satisfied = True
		for line in range(len(self.matrix)):
			line_val = 0
			for column in range(len(self.matrix[0])):
				line_val += self.matrix[line][column]
			line_val = (line_val - self.matrix[line][line])/self.matrix[line][line]
			if line_val >= 1:
				satisfied = False
				break
		return satisfied
