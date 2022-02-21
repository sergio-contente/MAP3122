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
	eigenvalue_error = np.abs(np.abs(mu_k) - np.abs(lambda1))
	return eigenvalue_error

def get_eigenvector_error(x_k, x_true):
	#print(f"x_k: {x_k}")
	#print(f"lambda1: {l1}")
	eigenvector_error = np.linalg.norm(np.abs(x_k) - np.abs(x_true))
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
                    #print(f"columns: {eigenvector_unsorted_index}")
                    #print(f"to {eigenvector_sorted_index}")
                    #print(f"eigenvectors_sorted b4: {eigenvectors_sorted}")
                    #print(f"eigenvectors_unsorted b4: {eigenvectors_unsorted}")
                    eigenvectors_sorted[:, [eigenvector_sorted_index]] = eigenvectors_unsorted[:, [eigenvector_unsorted_index]]
                    #print(f"eigenvectors_sorted after: {eigenvectors_sorted}")
        for i in range(0,len(lambdas_sorted)):
            for lambda_unsorted in lambdas_unsorted:
                if lambdas_sorted[i] == np.abs(lambda_unsorted):
                    lambdas_sorted[i] = lambda_unsorted
                    break

        #print(f"lambdas unsorted: {lambdas_unsorted}\n eigenvectors_unsorted:\n{eigenvectors_unsorted}")
        #print(f"lambdas sorted: {lambdas_sorted}\n eigenvectors_sorted:\n{eigenvectors_sorted}")
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
	x = np.zeros_like(b)
	residual = 1
	iterations = 0
	while residual > 10e-5 and iterations < 50:
		for i in range(len(b)):
			sum = 0
			for j in range(len(b)):
				if j != i:
					sum += matrix[i][j] * x[j][0]
					#print(f"sum: {sum} aij: {matrix[i][j]} omega: {omega} bi: {b[i][0]} b: {b}\n i,j: {i},{j}===================================================================================================")
			x[i][0] = (1-omega) * x[i][0] + (omega / matrix[i][i]) * (b[i][0] - sum)
		residual = np.linalg.norm(np.dot(matrix,x) - b)
		#print(f"x:\n{x}\nresidual: {residual}")
		iterations += 1
	#print(iterations)
	#print(f"")
	return x

# def SOR(A, b, omega):
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
#     b = np.transpose(b)[0]
#     print(b)
#     phi = np.zeros(len(b))[:]
#     residual = np.linalg.norm(np.matmul(A, phi) - b)  # Initial residual
#     while residual > 10e-5:
#         print(phi)
#         for i in range(A.shape[0]):
#             sigma = 0
#             for j in range(A.shape[1]):
#                 if j != i:
#                     sigma += A[i, j] * phi[j]
#             phi[i] = (1 - omega) * phi[i] + (omega / A[i, i]) * (b[i] - sigma)
#         residual = np.linalg.norm(np.matmul(A, phi) - b)
#         step += 1
#         print("Step {} Residual: {:10.6g}".format(step, residual))
#     print(f"phi: {phi} phit: {np.transpose(phi)}")
#     return np.transpose(phi)
