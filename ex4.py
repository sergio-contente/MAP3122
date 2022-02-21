from metodos.fatoracao_qr import fatoracao_qr
from metodos.common import *
import numpy as np
import matplotlib.pyplot as plt

epsilon = 10**(-15)

def main():
    eps1 = np.array([[0,1],[1,2],[2,3],[2,4],[2,5],[3,6],[4,7],[5,8],[6,9],[7,8],[8,10],[10,14],[14,11],[11,12],[12,13],[13,15]])
    eps2 = np.array([[0,1],[1,2],[2,5],[2,6],[6,4],[3,4],[4,7],[5,8],[8,11],[8,9],[9,10],[7,10],[9,12],[12,13],[13,14],[14,15]])

    #gera matrizes de adjacencia a partir de matrizes de arestas
    A1 = np.zeros((16,16))
    A2 = np.zeros((16,16))
    for edge1 in eps1:
        A1[edge1[0],edge1[1]] = 1
        A1[edge1[1],edge1[0]] = 1
    for edge2 in eps2:
        A2[edge2[0],edge2[1]] = 1
        A2[edge2[1],edge2[0]] = 1
    grau_med1, grau_max1 = grau_med_max(eps1)
    grau_med2, grau_max2 = grau_med_max(eps2)
    print(f"gmed1: {grau_med1} gmax1: {grau_max1}\ngmed2: {grau_med2} gmax2: {grau_max2}")

    while True:
        try:
            print("SELECIONE QUAL A MATRIZ DESEJA-SE APLICAR O MÉTODO: ")
            modo = int(input("1 ou 2: "))
            if modo == 1:
                A = np.array(A1)
                break
            elif modo == 2:
                A = np.array(A2)
                break
            else:
                raise ValueError("Entrada inválida!")
        except ValueError as ve:
            print(ve)
    
    eigenvalues, eigenvectors = get_sorted_eigenvalues_eigenvectors(A)
    print(f"vals:\n{eigenvalues}\n\nvecs:\n{eigenvectors}\n")
    sorted = np.sort(np.abs(eigenvalues))
    l1 = eigenvalues[15]
    x_star = eigenvectors[15]
    print(f"l1: {l1}\nx*:\n{x_star}")

    # V_k = np.identity(A.shape[1])
    # A_copy = np.array(A, copy=True)
    # autovalor, autovetor = np.linalg.eig(A_copy)
    # A_k = np.array(A, copy=True)
    # it_max = 700
    # symmetrical = is_symmetrical(A_copy)
    # converged = False
    # for iteration in range(1, it_max):
    #     qr = fatoracao_qr(A_k)
    #     Q_k, R_k = qr.get_qr()
    #     if symmetrical:
    #         V_k = np.matmul(V_k, Q_k)
    #     A_k = np.matmul(R_k,Q_k)
    #     failed_conversion = False
    #     for i in range(A_k.shape[0]):
    #         for j in range(A_k.shape[1]):
    #             if i > j and np.abs(A_k[i][j]) > epsilon:
    #                 failed_conversion = True
    #                 break
    #     # 	if i == (A_k.shape[0] - 1) and failed_conversion == False:
    #     # 		converged = True
    #     # 		print("CONVERGIU!")
    #     # if converged:
    #     # 	break
    # l1 = 0
    # eigenvals = np.zeros(A_k.shape[0])
    # for i in range(A_k.shape[0]):
    #     for j in range(A_k.shape[1]):
    #         if i == j:
    #             eigenvals[i] = A_k[i,j]
    #             if np.abs(eigenvals[i]) > l1:
    #                 l1 = eigenvals[i]

    # print(f"Autovalores reais:\n{autovalor}\nAutovalores aproximados:\n{A_k}")
    # print(f"Autovetores reais:\n{autovetor}\nAutovetores aproximados:\n{V_k}\nA:\n{A}")
    # print(f"Return da eig:\n{np.linalg.eig(A)}")
    # print(f"autovalores:\n{eigenvals}\nlambda1: {l1}")


if __name__ == '__main__':
    main()
