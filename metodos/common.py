import numpy as np
import matplotlib.pyplot as plt

def get_assintotico(lambda1, lambda2, it_max):
	vector = []
	squared = []
	base = 1
	assint = np.abs(lambda2/lambda1)
	for i in range(0, it_max):
		base = base * assint
		base_squared = base**2
		vector.append(base)
		squared.append(base_squared)
	return vector, squared

def get_eigenvalue_error(mu_k, lambda1):
	eigenvalue_error = float(np.abs(mu_k-lambda1))
	#print(f"autovalor erro: \n{eigenvalue_error}")
	return eigenvalue_error

def get_eigenvector_error(x_k, x_true):
	#print(f"x_k: {x_k}")
	#print(f"lambda1: {l1}")
	eigenvector_error = np.linalg.norm(x_k - x_true)
	#print(f"autovetor erro: \n{eigenvector_error}")
	#print(f"subtraction: {sub}\nerror: {eigenvector_error}")
	return eigenvector_error

def get_sorted_eigenvalues_eigenvectors(matrix):
        lambdas_unsorted, eigenvectors_unsorted = np.linalg.eig(matrix)
        lambdas_sorted = np.sort(np.abs(lambdas_unsorted))
        eigenvectors_sorted = np.empty(eigenvectors_unsorted.shape)
        for lambda_sorted in lambdas_sorted:
            for lambda_unsorted in lambdas_unsorted:
                if lambda_sorted == np.abs(lambda_unsorted):
                    eigenvector_sorted_index = np.where(lambdas_sorted == lambda_sorted)[0][0]
                    eigenvector_unsorted_index = np.where(lambdas_unsorted == lambda_unsorted)[0][0]
                    eigenvectors_sorted[:, [eigenvector_sorted_index]] = eigenvectors_unsorted[:, [eigenvector_unsorted_index]]
        for i in range(0,len(lambdas_sorted)):
            for lambda_unsorted in lambdas_unsorted:
                if lambdas_sorted[i] == np.abs(lambda_unsorted):
                    lambdas_sorted[i] = lambda_unsorted
                    break
        return lambdas_sorted, eigenvectors_sorted

def plot_aproximations(iterations, eigenvalue_error, eigenvector_error, error_assintotico, error_assintotico_quadrado):
	plt.yscale("log")
	plt.plot(iterations, error_assintotico, label=r'$\left|\frac{\lambda_1}{\lambda_2}\right|^k $')
	plt.plot(iterations, error_assintotico_quadrado, label=r'$\left|\frac{\lambda_1}{\lambda_2}\right|^{2k} $')
	plt.plot(iterations, eigenvalue_error, label="erro autovalor")
	plt.plot(iterations, eigenvector_error, label="erro autovetor")
	plt.legend()
	plt.show()
pass

def SOR(matrix, b, omega):
	x = np.transpose(np.random.randn(b.shape[0]))
	print(f"b:\n{b}\nx:\n{x}")
	residual = 1
	iterations = 0
	while residual > 10e-15 and iterations < 50:
		for i in range(len(b)):
			sum = 0
			for j in range(len(b)):
				if j != i:
					sum += matrix[i][j] * x[j]
					#print(f"sum: {sum} aij: {matrix[i][j]} omega: {omega} bi: {b[i][0]} b: {b}\n i,j: {i},{j}")
					#print(f"sum: {sum}")
			x[i] = (1-omega) * x[i] + (omega / matrix[i][i]) * (b[i] - sum)
		residual = np.linalg.norm(np.dot(matrix, x) - b)
		#print(f"x:\n{x}\nresidual: {residual}")
		iterations += 1
	#print(f"iterations: {iterations} matriz: {matrix}")	#p")
	return x
	# A=matrix
	# valores_x = []
	# n = matrix.shape[0]
	# x0 = np.random.rand(n)
	# valores_x.append(x0)

	# for k in range(50):
	# 	x_ant = valores_x[-1]
	# 	x_at = np.zeros(n)
	# 	for i in range(n):
	# 		xi = b[i]
	# 		for j in range(i):
	# 			xi=xi-A[i][j]*x_at[j]


	# 		for j in range(i+1, n):
	# 			xi=xi-A[i][j]*x_ant[j]

	# 		xi=xi/A[i][i]
	# 		print(f"ai: {xi}")
	# 		x_at[i] = (1-omega)*x_ant[i] + omega*xi
	# 	valores_x.append(x_at)    
	# return valores_x[-1]

def is_symmetrical(matrix):
	#print(matrix)
	for i in range(matrix.shape[0]):
		for j in range(matrix.shape[1]):
			if i != j and matrix[i][j] != matrix[j][i]:
				print(f"NÃO É SIMÉTRICA!")
				return False
	return True

def grau_med_max(eps):
	vector = np.zeros(16)
	total = 0
	grau_max = 0
	for i in range(16):
		for line in eps:
			for vec in line:
				if i == vec:
					vector[i] += 1
					total += 1
	avg = total/16
	for grau in vector:
		if grau > grau_max:
			grau_max = grau
	return avg, grau_max

# def sor_solver(A, b, omega, initial_guess, convergence_criteria):
#     """
#     This is an implementation of the pseudo-code provided in the Wikipedia article.
#     Arguments:
#         A: nxn numpy matrix.
#         b: n dimensional numpy vector.
#         omega: relaxation factor.
#         initial_guess: An initial solution guess for the solver to start with.
#         convergence_criteria: The maximum discrepancy acceptable to regard the current solution as fitting.
#     Returns:
#         phi: solution vector of dimension n.
#     """
#     step = 0
#     phi = initial_guess[:]
#     residual = np.linalg.norm(np.matmul(A, phi) - b)  # Initial residual
#     while residual > convergence_criteria:
#         for i in range(A.shape[0]):
#             sigma = 0
#             for j in range(A.shape[1]):
#                 if j != i:
#                     sigma += A[i, j] * phi[j]
#             phi[i] = (1 - omega) * phi[i] + (omega / A[i, i]) * (b[i] - sigma)
#         residual = np.linalg.norm(np.matmul(A, phi) - b)
#         step += 1
#         print("Step {} Residual: {:10.6g}".format(step, residual))
#     return phi
