from re import L, X
import statistics
import numpy as np
import matplotlib.pyplot as plt

def get_tao(t, T):
    tao = T-t
    return tao

def get_delta_x(L, N):
    delta_x = 2*L/N
    return delta_x

def get_delta_tao(T, M):
    delta_tao = T/M
    return delta_tao

def update_x_i(i, L, N):
    delta_x = get_delta_x(L, N)
    x_i = i * delta_x - L
    return x_i

def update_tao_j(j, T, M):
    delta_tao = get_delta_tao(T, M)
    tao_j = j * delta_tao
    return tao_j

def get_x(S, K, r, sigma, tao): # ou update?
    x = np.log(S/K) + (r - sigma**2/2) * tao
    return x

def update_S_ij(K, x_i, tao_j, r, sigma):
    S_ij = K * np.e**(x_i - (r - sigma**2/2) * tao_j)
    return S_ij

def update_V_ij(u_ij, tao_j, r):
    V_ij = u_ij * np.e**(-r * tao_j)
    return V_ij

def update_u_ij(u_ij, sigma, u_iant_j, u_iprox_j, T, M, L, N):
    u_ij_prox = u_ij * get_delta_tao(T, M)/get_delta_x(L, N)**2 * sigma**2/2 * (u_iant_j - 2 * u_ij + u_iprox_j)
    return u_ij_prox

def get_u_ij_anal():
    d1 = (x + sigma**2 * tao)/(sigma * np.sqrt(tao))
    d2 = X/(sigma * np.sqrt(tao))
    N_d1 = statistics.NormalDist.cdf(d1)
    N_d2 = statistics.NormalDist.cdf(d2)
    u_ij_anal = 
    return u_ij_anal

def get_V_interpol(S, K, r, sigma, tao, x_iprox, x_i, V_ij, V_iprox_j):
    x = get_x(S, K, r, sigma, tao)
    V = ((x_iprox - x) * V_ij - (x_i - x) * V_iprox_j)/(x_iprox - x_i)
    return V
