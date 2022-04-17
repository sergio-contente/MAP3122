import statistics
import numpy as np
import matplotlib.pyplot as plt

def get_tau_analitico(t, T):
    tau = T-t
    return tau

def get_delta_x_analitico(L, N):
    delta_x = 2*L/N
    return delta_x

def get_delta_tau_analitico(T, M):
    delta_tau = T/M
    return delta_tau

def get_x_analitico(S, K, r, sigma, tau): # ou update?
    x = np.log(S/K) + (r - sigma**2/2) * tau
    return x

def get_u_analitico_normal(x, sigma, tau, K):
    d1 = (x + sigma**2 * (tau/2))/(sigma * np.sqrt(tau))
    d2 = x/(sigma * np.sqrt(tau))
    N_d1 = statistics.NormalDist.cdf(d1)
    N_d2 = statistics.NormalDist.cdf(d2)
    u_analitico = K * np.e**(x+sigma**2 * tau/2) * N_d1 - K * N_d2
    return u_analitico

def get_u_analitico(K, L, sigma, tau):  
    u_analitico = K * np.e**(L + sigma**2 * tau/2)
    return u_analitico

def get_S_analitico(x, tau, sigma, K, r):
    S = K * np.e**(x - (r - sigma**2 / 2) * tau)
    return S

def get_V_analitico(r, T, t, sigma, S, K, metodo_u="1"): # Fazer com u da dist normal ou outro metodo analitico?
    tau = get_tau_analitico(t, T)
    x = get_x_analitico(S, K, r, sigma, tau)
    if metodo_u == "1":
        u = get_u_analitico
    elif metodo_u == "2":
        u = get_u_analitico_normal
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

def get_V_aprox(M, N, L, sigma, K, T, r, u, vetorizar=True):
    V = np.zeros((N+1, M+1))
    for j in range(M+1):
        tau = update_tau_j(j, T, M)
        V[:, j] = u[:, j] * np.e**(-r * tau)
    return V

def get_V_interpol(M, N, L, t, T, K, r, sigma, V_aprox):
    V = np.zeros((N+1, M+1))
    tau = get_tau_analitico(t, T)
    for j in range(M+1):
        tau_j = update_tau_j(j, T, M)
        for i in range(N+1):
            x_i = update_x_i(i, L, N)
            S = update_S_ij(K, x_i, tau_j, r, sigma)
            x = get_x_analitico(S, K, r, sigma, tau)
            V[i, j] = ((x_i[i+1] - x) * V_aprox[i][j] - (x_i[i] - x) * V_aprox[i+1][j])/(x_i[i+1] - x_i[i]) # np.divide ou soh '/'?
    return V

def update_u_ij(u_ij, sigma, u_iant_j, u_iprox_j, T, M, L, N):
    u_ij_prox = u_ij * get_delta_tau_analitico(T, M)/get_delta_x_analitico(L, N)**2 * sigma**2/2 * (u_iant_j - 2 * u_ij + u_iprox_j)
    return u_ij_prox

def update_u_ij_vetorizado(u_ij_vetor, T, M, L, N, sigma, u_iant_j_vetor, u_iprox_j_vetor):
    u_ij_prox_vetor = u_ij_vetor + np.matmul((get_delta_tau_analitico(T, M)/get_delta_x_analitico(L, N)**2 * sigma**2/2), (u_iant_j_vetor - 2 * u_ij_vetor + u_iprox_j_vetor))
    return u_ij_prox_vetor

def iterador_u_ij(N, L, sigma, K, T, vetorizar=True):
    M = N/L
    u  = np.zeros((N+1, M+1))
    if vetorizar == False:
        for j in range(-1, M):
            tau = update_tau_j(j, T, M)
            for i in range(0, N+1):
                x = update_x_i(i, L, N)
                if i == 0:
                    u[i][j+1] = 0
                elif i == N:
                    u[i][j+1] = K * np.e**(L + sigma**2 * tau/2)
                elif j==0:
                    u[i][j+1] = K * max(np.e**x - 1, 0)
                else:
                    u[i][j+1] = update_u_ij(u[i][j], sigma, u[i-1][j], u[i+1][j], T, M, L, N)
    else:
        for i in range(N+1):
            x = update_x_i(i, L, N)
            u[i][0] = K * max(np.e**x - 1, 0)

        for j in range(M+1):
            tau = update_tau_j(j, T, M)
            u[N][j] = K * np.e**(L + sigma**2 * tau/2)
            u[0][j] = 0

        for j in range(1, M):
            tau = update_tau_j(j, T, M)

            u_iant_j_vetor = u[0:N-2, j]
            u_ij_vetor = u[1:N-1, j]
            u_iprox_j_vetor = u[2:N, j]

            u[1:N-1, j+1] = update_u_ij_vetorizado(u_ij_vetor, T, M, L, N, sigma, u_iant_j_vetor, u_iprox_j_vetor)
    return u
