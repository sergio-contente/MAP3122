from cmath import tau
from metodos import *

def option(N, L, sigma, K, T, r, t, S0, vetorizar=True):
    M = L * 2

    u = iterador_u_ij(N, L, sigma, K, T, vetorizar)
    tau = get_tau_analitico(t, T)
    x = get_x_analitico(S0, K, r, sigma, tau)
    u_analitico = get_u_analitico_normal(x, sigma, tau, K)
    for j in range(M+1):
        for i in range(N+1):
            print("u_ij numerico = " + u[i][j])
            print("u_ij analitico = " + u_analitico[i][j])

    V_aprox = get_V_aprox(M, N, L, sigma, K, T, r, u, vetorizar)
    V_interpol = get_V_interpol(M, N, L, t, T, K, r, sigma, V_aprox)

    # S = get_S_analitico()


def main():
    N = int(input("Insira o valor de N: "))
    L = int(input("Insira o valor de L: "))
    sigma = float(input("Insira o valor de sigma: "))
    K = float(input("Insira o valor de K: "))
    T = float(input("Insira o valor de T: "))
    r = float(input("Insira o valor de r: "))
    t = float(input("Insira o valor de t: "))
    S0 = float(input("Insira o valor de S0: "))
    St = float((input("Insira o valor de S1: ")))

    option(N, L, sigma, K, T, r, t, S0, St)

if __name__ == '__main__':
    try:
        main()
    except     KeyboardInterrupt:
        print("Algo deu errado.")