from math import sqrt
import numpy as np

from metodos.common import *

class metodo_potencias_inversas:
	def __init__(self, x_0, A):
		self.n = len(A)
		self.x_k = x_0
		self.mu_k = 0.0
		self.inv_matrix_x_k_product = np.zeros_like(x_0)
		self.matrix = A
		self.omega = 1.0

	def update_x_k(self):#chamar antes de update_mu_k!!!
		self.inv_matrix_x_k_product = SOR(self.matrix, self.x_k, self.omega)
		self.x_k = self.inv_matrix_x_k_product/np.linalg.norm(self.inv_matrix_x_k_product)
		return self.x_k

	def update_mu_k(self):
		x_k_transp = np.transpose(self.x_k)[0]
		#print(f"prod: {self.inv_matrix_x_k_product}")
		#print(f"transp: {x_k_transp} prod: {self.inv_matrix_x_k_product} prod2: {np.dot(x_k_transp, self.inv_matrix_x_k_product)[0]}")
		self.mu_k = np.dot(x_k_transp, self.inv_matrix_x_k_product)[0]/np.dot(x_k_transp, self.x_k)[0]
		#print(f"muk: {self.mu_k} prodt: {np.dot(x_k_transp, self.x_k)[0]}")
		return self.mu_k

	# def gauss_seidel(A, b, tolerance=1e-10, max_iterations=10000):

	# 	x = np.zeros_like(b, dtype=np.double)

	# 	#Iterate
	# 	for k in range(max_iterations):
			
	# 		x_old  = x.copy()
			
	# 		#Loop over rows
	# 		for i in range(A.shape[0]):
	# 			x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) / A[i ,i]
				
	# 		#Stop condition 
	# 		if np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf) < tolerance:
	# 			break
			
	# 	return x

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
			#print(beta)
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

	def optimal_omega(self, lambda1):
		print(f"mu_k: {self.mu_k} l1: {lambda1}")
		# if self.mu_k == 0:
		# 	return self.omega
		self.omega = 1 + (self.mu_k/(1 + sqrt(np.abs(1.0 - lambda1**2))))**2
		return self.omega

	# def SOR(self):
	# 	for i in range(len(self.x_k)):
	# 		sum = 0
	# 		for j in range(len(self.x_k)):
	# 			if j != i:
	# 				sum += self.matrix[i][j]
	# 		self.x_k[i] += self.omega*((self.x_k[i] - sum)/self.matrix[i][i] - self.x_k[i])
	# 	return self.x_k