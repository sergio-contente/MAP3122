import statistics
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def get_tau_analitico(t, T):
    tau = T-t
    return tau

def get_delta_x_analitico(L, N):
    delta_x = float(2*L/N)
    return delta_x

def get_delta_tau_analitico(T, M):
    delta_tau = float(T/M)
    return delta_tau

def get_x_analitico(S, K, r, sigma, tau): # ou update?
    x = np.log(S/K) + (r - sigma**2/2) * tau
    return x

def get_u_analitico_normal(sigma, K, M, N, T, L):
    u_analitico = np.zeros((N+1, M+1))
    for j in range(M+1):
        tau_j = update_tau_j(j, T, M)
        for i in range(N+1):
            x_i = update_x_i(i, L, N)
            if j==0:
                u_analitico[i][j] = K*max(np.e**x_i-1, 0)
            else:
                d1 = (x_i + sigma**2 * tau_j)/(sigma * np.sqrt(tau_j))
                d2 = x_i/(sigma * np.sqrt(tau_j))
                # N_d1 = statistics.NormalDist().cdf(d1)
                # N_d2 = statistics.NormalDist().cdf(d2)
                N_d1 = norm.cdf(d1)
                N_d2 = norm.cdf(d2)
                u_analitico[i][j] = K * np.e**(x_i+sigma**2 * tau_j/2) * N_d1 - K * N_d2
                print(f"N_d1 = {N_d1} e N_d2 = {N_d2} e u_anal_ij = {u_analitico[i][j]}")
    return u_analitico

# def get_u_analitico(K, L, sigma, tau):  
#     u_analitico = K * np.e**(L + sigma**2 * tau/2)
#     return u_analitico

def get_S_analitico(x, tau, sigma, K, r):
    S = K * np.e**(x - (r - sigma**2 / 2) * tau)
    return S

def get_V_analitico(r, T, t, sigma, S, K, M, N, L): # Fazer com u da dist normal ou outro metodo analitico?
    u = get_u_analitico_normal(sigma, K, M, N, T, L)
    V = u * np.e**(-r * (T-t))
    return V

def get_Vc_analitico(x, sigma, tau, S, K, e, r, T, t):
    d1 = (x + sigma**2 * tau)/(sigma * np.sqrt(tau))
    d2 = x/(sigma * np.sqrt(tau))
    N_d1 = statistics.NormalDist.cdf(d1)
    N_d2 = statistics.NormalDist.cdf(d2)
    Vc = S * N_d1 - K * e**(-r(T-t)) * N_d2
    return Vc

def get_Vp_analitico(x, sigma, tau, S, K, e, r, T, t):
    d1 = (x + sigma**2 * tau)/(sigma * np.sqrt(tau))
    d2 = x/(sigma * np.sqrt(tau))
    N_min_d1 = statistics.NormalDist.cdf(-d1)
    N_min_d2 = statistics.NormalDist.cdf(-d2)
    Vp = -S * N_min_d1 + K * e**(-r(T-t)) * N_min_d2
    return Vp

def update_x_i(i, L, N):
    delta_x = get_delta_x_analitico(L, N)
    x_i = i * delta_x - L
    return x_i

def update_tau_j(j, T, M):
    delta_tau = get_delta_tau_analitico(T, M)
    tau_j = j * delta_tau
    return tau_j

def update_S_ij(K, x_i, tau_j, r, sigma):
    S_ij = K * np.e**(x_i - (r - sigma**2/2) * tau_j)
    return S_ij

def get_V_ij(N, M, T, r, u):
    V = np.zeros((N+1, M+1))
    for j in range(M+1):
        tau_j = update_tau_j(j, T, M)
        V[:, j] = u[:, j] * np.e**(-r * tau_j)
    return V

def get_V_dado_S(T, M, L, N, t, S, K, r, sigma, V):
    delta_tau = get_delta_tau_analitico(T, M)
    delta_x = get_delta_x_analitico(L, N)
    tau = get_tau_analitico(t, T)
    x = get_x_analitico(S, K, r, sigma, tau)

    indice_i = round((x + L)/delta_x)
    indice_j = round(tau/delta_tau)

    x_i = update_x_i(indice_i, L, N)
    x_i_prox = update_x_i(indice_i+1, L, N)

    V_aprox = V[indice_i][indice_j]
    V_interpol = ((x_i_prox - x) * V[indice_i][indice_j] - (x_i - x) * V[indice_i+1][indice_j])/(x_i_prox - x_i)
    return V_aprox, V_interpol

def preenche_conds_contorno(u, N, L, K, T, M, sigma):
    for i in range(N+1):
        x_i = update_x_i(i, L, N)
        u[i][0] = K * max(np.e**x_i - 1, 0)
    for j in range(M+1):
        tau_j = update_tau_j(j, T, M)
        u[N][j] = K * np.e**(L + sigma**2 * tau_j/2)
        u[0][j] = 0
    return u

def iterador_S_ij(N, M, T, L, K, r, sigma):
    S = np.zeros((N+1, M+1))
    for j in range(M+1):
        tau_j = update_tau_j(j, T, M)
        for i in range(N+1):
            x_i = update_x_i(i, L, N)
            S[i][j] = update_S_ij(K, x_i, tau_j, r, sigma)
    return S

def iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar=1):
    u = np.zeros((N+1, M+1))
    u = preenche_conds_contorno(u, N, L, K, T, M, sigma)
    delta_tau = get_delta_tau_analitico(T, M)
    delta_x = get_delta_x_analitico(L, N)
    if vetorizar == 0:
        for j in range(1, M+1):
            for i in range(1, N):
                u[i][j] = u[i][j-1] + (delta_tau /delta_x**2)*(sigma**2/2)*(u[i-1][j-1]-2*u[i][j-1]+u[i+1][j-1])
    else:
        for j in range(M):
            u_iant_j_vetor = u[0:-2, j]
            u_ij_vetor = u[1:-1, j]
            u_iprox_j_vetor = u[2: , j]

            u[1:-1, j+1] = u_ij_vetor + (delta_tau/delta_x**2) * (sigma**2/2) * (u_iant_j_vetor -2 * u_ij_vetor + u_iprox_j_vetor)
    return u

def gera_lucro(V, t, N, M, L, sigma, K, T, r, valor_comprado, custo_inicial):
    k       = 100
    S_min   = K/2
    S_max   = 3*K/2   
    delta_S = (S_max-S_min)/k
    k_i     = np.arange(k)
    S_list  = k_i*delta_S+S_min 
    cenarios = []
    for S in S_list:
        resultado = get_V_dado_S(T, M, L, N, t, S, K, r, sigma, V)[1]*valor_comprado - custo_inicial
        cenarios.append(resultado)
    return cenarios, S_list

def gera_preco_ativo(V, t, N, M, L, sigma, K, T, r):
    k       = 10000
    S_min   = 2*K/3
    S_max   = 4*K/3   
    delta_S = (S_max-S_min)/k
    k_i     = np.arange(k)
    S_list  = k_i*delta_S+S_min 
    cenarios = []
    for S in S_list:
        resultado = get_V_dado_S(T, M, L, N, t, S, K, r, sigma, V)[1]
        cenarios.append(resultado)
    return cenarios, S_list