from metodos.fatoracao_qr import fatoracao_qr
from metodos.potencias_inversas import metodo_potencias_inversas
from metodos.common import *
import numpy as np
import matplotlib.pyplot as plt
from metodos.potencias import metodo_potencia
'''
Nome: Sergio Magalhães Contente NUSP: 10792087
Nome: Jonas Gomes de Morais NUSP: 10893805
'''
epsilon = 10**(-15)

def potencias(it_max, A, n):
        it_max = 69
        vector_x0 = np.random.rand(n,1)
        true_eigenvectors = get_sorted_eigenvalues_eigenvectors(np.array(A))[1]
        x_true = true_eigenvectors[:,[n-1]]
        metodo = metodo_potencia(vector_x0, np.array(A))
        for i in range(1, it_max):
            mu_k = metodo.update_mu_k()
            x_k = metodo.update_x_k()
            eigenvector_error = get_eigenvector_error(x_k, x_true)
            if eigenvector_error <= epsilon:
                break
        return mu_k, x_k

def metodo_fatoracao_qr(A):
    V_k = np.identity(A.shape[1])
    A_copy = np.array(A, copy=True)
    autovalores = []
    autovetores = []
    A_k = np.array(A, copy=True)
    it_max = 69
    symmetrical = is_symmetrical(A_copy)
    converged = False
    for i in range(1, it_max):
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
            if i == (A_k.shape[0] - 1) and failed_conversion == False:
                converged = True
                break
        if converged:
            break
    for i in range(A_k.shape[0]):
            for j in range(A_k.shape[1]):
                if i == j:
                    lambda_value = A_k[i][j]
                    autovalores.append(lambda_value)
    for i in range(V_k.shape[1]):
            x_estrela = V_k[:, [i]]
            autovetores.append(x_estrela)
    l1 = max(autovalores)
    index = int(np.where(autovalores == l1)[0])
    x_star = autovetores[index]
    return l1, x_star

def potencias_inversas(A):
    n = len(A)
    while True:
        vector_x0 = np.random.rand(n,1)
        metodo = metodo_potencias_inversas(vector_x0, A)
        if metodo.sassenfeld_criteria() or metodo.lines_criteria():
            break
    it_max = 69
    true_eigenvectors = get_sorted_eigenvalues_eigenvectors(np.linalg.inv(A))[1]
    x_true = true_eigenvectors[:,[n-1]]

    for i in range(1, it_max):
        x_k = metodo.update_x_k()
        mu_k = metodo.update_mu_k()
        eigenvector_error = get_eigenvector_error(x_k, x_true)
        if eigenvector_error <= epsilon:
            break
    return mu_k, x_k


def main():
    eps1 = np.array([[0,1],[1,2],[2,3],[2,4],[2,5],[3,6],[4,7],[5,8],[6,9],[7,8],[8,10],[10,14],[14,11],[11,12],[12,13],[13,15]])
    eps2 = np.array([[0,1],[1,2],[2,3],[3,4],[2,5],[5,6],[5, 12],[6,7],[7,11],[7,13],[7,8],[6,7],[7,8],[7,11],[7, 13],[9,10],[10,11],[12,14],[13,14],[14,15]])

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
    l1_orig = eigenvalues[15]
    x_star_orig = eigenvectors[:, [15]]
    x_star_orig = x_star_orig/np.linalg.norm(x_star_orig)
    print(f"Matriz A = \n {A}")    
    if modo == 1:
        l1, x_star= potencias(70, A, len(A))
        vertice_max_central = int(np.where(x_star == max(x_star))[0])
        print(f"Com o metodo das potencias (Ex 1):")
        print(f"gmed < lambda1 < gmax:\n{grau_med1} < {l1} < {grau_max1}\nx*:\n{x_star}")
        print(f"Vértice com maior grau de centralidade de autovetor: {vertice_max_central}\n")
        # l1, x_star = potencias_inversas(A)
        # vertice_max_central = int(np.where(x_star == max(x_star))[0])
        # print(f"Com o metodo das potencias inversas (Ex 2):")
        # print(f"gmed_2 < lambda1 < gmax2:\n{grau_med2} < {l1} < {grau_max2}\nx*:\n{x_star}")
        # print(f"Vértice com maior grau de centralidade de autovetor: {vertice_max_central}\n")
        l1, x_star= metodo_fatoracao_qr(A)
        vertice_max_central = int(np.where(x_star == max(x_star))[0])
        print(f"Com o metodo da fatoracao QR (Ex 3):")
        print(f"gmed_2 < lambda1 < gmax2:\n{grau_med2} < {l1} < {grau_max2}\nx*:\n{x_star}")
        print(f"Vértice com maior grau de centralidade de autovetor: {vertice_max_central}")
    else:
        l1, x_star= potencias(70, A, len(A))
        vertice_max_central = int(np.where(x_star == max(x_star))[0])
        print(f"Com o metodo das potencias (Ex 1):")
        print(f"gmed < lambda1 < gmax:\n{grau_med2} < {l1} < {grau_max2}\nx*:\n{x_star}")
        print(f"Vértice com maior grau de centralidade de autovetor: {vertice_max_central}\n")
        # l1, x_star = potencias_inversas(A)
        # vertice_max_central = int(np.where(x_star == max(x_star))[0])
        # print(f"Com o metodo das potencias inversas (Ex 2):")
        # print(f"gmed_2 < lambda1 < gmax2:\n{grau_med2} < {l1} < {grau_max2}\nx*:\n{x_star}")
        # print(f"Vértice com maior grau de centralidade de autovetor: {vertice_max_central}\n")
        l1, x_star= metodo_fatoracao_qr(A)
        vertice_max_central = int(np.where(x_star == max(x_star))[0])
        print(f"Com o metodo da fatoracao QR (Ex 3):")
        print(f"gmed < lambda1 < gmax:\n{grau_med2} < {l1} < {grau_max2}\nx*:\n{x_star}")
        print(f"Vértice com maior grau de centralidade de autovetor: {vertice_max_central}")

if __name__ == '__main__':
    main()
