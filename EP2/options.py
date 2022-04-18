from metodos import *

def cenario_1(vetorizar):
    N = 10000    
    L = 10       
    sigma = 0.01
    K = 1.0      
    T = 1.0      
    r = 0.01  
    M = round((sigma**2/(2*L/N)**2)*T) # condicao de estabilidade
       
    arquivo = open("cenario_1.txt", "w")

    '''
        Exercício 1
    '''

    t = 0.0   
    S0 = 1.0  

    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    escreve_arquivo(arquivo, N, L, M, K, sigma, T, r, S0, t, precificacao)
    escreve_terminal( N, L, M, K, sigma, T, r, S0, t, precificacao)

    print("Precificação da opção de compra: R${:.2f}".format(precificacao * 1000))

    '''
        Exercício 2
    '''
    M = 50 # condicao de estabilidade
    #Grafico 1 - t = 0.5
    t = 0.5
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    print("Precificação da opção de compra: R${:.2f}".format(precificacao * 1000))

    cenarios, S_list = gera_lucro(V_ij, t, N, M, L, sigma, K, T, r, qtd_comprada, gasto_inicial)
    escreve_grafico(S_list, cenarios, "Lucro e Prejuízo em t = 6 meses", "cenario_1_ex_2_g1.png")

    #Grafico 2 - t = 0.25
    t = 0.25
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 3 meses", "cenario_1_ex_2_g2.png")

    #Grafico 3 - t = 0.75
    t = 0.75
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 9 meses", "cenario_1_ex_2_g3.png")
    
    #Grafico 4 - t = 0.0
    t = 0.0
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 0 meses", "cenario_1_ex_2_g4.png")

    #Grafico 5 - t = T
    t = T
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 12 meses", "cenario_1_ex_2_g5.png")

    '''
    Exercicio 3
    '''
    sigma = 0.02
    M = round((sigma**2/(2*L/N)**2)*T) # condicao de estabilidade
    t = 0.5    

    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    print("Precificação da opção de compra: R${:.2f}".format(precificacao * 1000))

    escreve_arquivo(arquivo, N, L, M, K, sigma, T, r, S0, t, precificacao)
    escreve_terminal( N, L, M, K, sigma, T, r, S0, t, precificacao)

    #Grafico 1 - t = 0.5
    t = 0.5
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_lucro(V_ij, t, N, M, L, sigma, K, T, r, qtd_comprada, gasto_inicial)
    escreve_grafico(S_list, cenarios, "Lucro e Prejuízo em t = 6 meses", "cenario_1_ex_3_g1.png")

    #Grafico 2 - t = 0.25
    t = 0.25
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 3 meses", "cenario_1_ex_3_g2.png")

    #Grafico 3 - t = 0.75
    t = 0.75
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 9 meses", "cenario_1_ex_3_g3.png")
    
    #Grafico 4 - t = 0.0
    t = 0.0
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 0 meses", "cenario_1_ex_3_g4.png")

    #Grafico 5 - t = T
    t = T
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 12 meses", "cenario_1_ex_3_g5.png")

    '''
    Exercicio 4
    '''
    r = 0.1
    sigma = 0.1
    M = round((sigma**2/(2*L/N)**2)*T) # condicao de estabilidade

    #Grafico 1 - t = 0.5
    t = 0.5
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    print("Precificação da opção de compra: R${:.2f}".format(precificacao * 1000))

    cenarios, S_list = gera_lucro(V_ij, t, N, M, L, sigma, K, T, r, qtd_comprada, gasto_inicial)
    escreve_grafico(S_list, cenarios, "Lucro e Prejuízo em t = 6 meses", "cenario_1_ex_4_g1.png")

    #Grafico 2 - t = 0.25
    t = 0.25
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 3 meses", "cenario_1_ex_4_g2.png")

    #Grafico 3 - t = 0.75
    t = 0.75
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 9 meses", "cenario_1_ex_4_g3.png")
    
    #Grafico 4 - t = 0.0
    t = 0.0
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 0 meses", "cenario_1_ex_4_g4.png")

    #Grafico 5 - t = T
    t = T
    qtd_comprada = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 12 meses", "cenario_1_ex_4_g5.png")
    
    #Fim cenario 1
    arquivo.close()
    return
def cenario_2(vetorizar):
    arquivo = open("cenario_2.txt", "w")
    N = 10000
    L       = 10
    K       = 5.7
    sigma   = 0.1692
    T       = 3/12
    r       = 0.1075
    S0 = 5.6376
    t = 0
    M = round((sigma**2/(2*L/N)**2)*T) # condicao de estabilidade
    qtd_comprada = 100000

    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao_dezembro = V_presente_interpol * qtd_comprada + S0 * qtd_comprada
    gasto_inicial = precificacao_dezembro
    premio = V_presente_interpol * qtd_comprada
    print(f"Premio: {premio}")
    cenarios, S_list = gera_lucro(V_ij, t, N, M, L, sigma, K, T, r, qtd_comprada, gasto_inicial)
    escreve_grafico(S_list, cenarios, "Lucro e Prejuízo em t = 0 meses", "cenario_2_g1.png")
    escreve_terminal( N, L, M, K, sigma, T, r, S0, t, precificacao_dezembro)

    # Sabendo o valor do dolar em 1 de janeiro de 2022
    S = 5.578
    t = 1/12
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao_janeiro = V_presente_interpol * qtd_comprada 
    escreve_arquivo(arquivo, N, L, M, K, sigma, T, r, S, t, precificacao_janeiro)
    saldo = (precificacao_janeiro-precificacao_dezembro)
    print("Prejuízo da compra: R${:.2f}".format(saldo))

    # Sabendo o valor do dolar em 1 de marco de 2022
    S = 5.1604718519
    t = 3/12
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao_marco = V_presente_interpol * qtd_comprada 
    escreve_arquivo(arquivo, N, L, M, K, sigma, T, r, S, t, precificacao_marco)
    saldo = (precificacao_marco-precificacao_dezembro)
    print("Prejuízo da compra: R${:.2f}".format(saldo))

    arquivo.close()
    return 


def escreve_arquivo(arquivo, N, L, M, K, sigma, T, r, S, t, V):
    arquivo.write("Parâmetros:\n")
    arquivo.write("N        = {}\n".format(N))
    arquivo.write("L        = {}\n".format(L))
    arquivo.write("M        = {}\n".format(M))
    arquivo.write("K        = {:.2f}\n".format(K))
    arquivo.write("sigma    = {:.2f}\n".format(sigma))
    arquivo.write("T        = {:.2f}\n".format(T))
    arquivo.write("r        = {:.2f}\n".format(r))
    arquivo.write("S0       = {:.2f}\n".format(S))
    arquivo.write("t        = {:.2f}\n".format(t))
    arquivo.write("Preço da opção:\n")
    arquivo.write("V        = {:.2f}\n".format(V))
    arquivo.write("\n\n")
    return

def escreve_terminal(N, L, M, K, sigma, T, r, S, t, V):
    print("Parâmetros:\n")
    print("N        = {}\n".format(N))
    print("L        = {}\n".format(L))
    print("M        = {}\n".format(M))
    print("K        = {:.2f}\n".format(K))
    print("sigma    = {:.2f}\n".format(sigma))
    print("T        = {:.2f}\n".format(T))
    print("r        = {:.2f}\n".format(r))
    print("S0       = {:.2f}\n".format(S))
    print("t        = {:.2f}\n".format(t))
    print("Preço da opção:\n")
    print("V        = {:.2f}\n".format(V))
    print("\n\n")
    return

def escreve_grafico(S_list, cenarios, titulo, nome):
    fig, ax = plt.subplots(figsize = (11, 6))
    ax.plot(S_list, cenarios)
    ax.grid(visible = True, axis = "y", linestyle = "--")
    ax.set_title(titulo)
    ax.set_xlabel("Preço do ativo")
    ax.set_ylabel("Valor da opção")
    plt.savefig(nome)
    plt.show()

def compara_tempos_vetorizar():
    N = 10000    
    L = 10       
    sigma = 0.01
    K = 1.0      
    T = 1.0      
    r = 0.01  
    M = round((sigma**2/(2*L/N)**2)*T)
    inicio = time.process_time()
    u = iterador_u_ij(M, N, L, sigma, K, T, r, False)
    fim = time.process_time()
    sem_vetorizar = (fim - inicio)*1000
    inicio = time.process_time()
    u = iterador_u_ij(M, N, L, sigma, K, T, r, True)
    fim = time.process_time()
    vetorizando = (fim - inicio)*1000
    print("Tempo de execução do método sem vetorização {:.2f} ms".format(sem_vetorizar))
    print("Tempo de execução do método com vetorização {:.2f} ms".format(vetorizando))
    return

def main():
    compara_tempos_vetorizar()

    print("#####    Escolha um cenário  #######")
    print("##### (1) Cenário fictício   #######")
    print("##### (2) Cenário câmbio     #######")
    print("(###################################")
    cenario = int(input("Cenário: "))
    print("#####    Deseja vetorizar?   #######")
    print("##### (1) Sim                #######")
    print("##### (0) Não                #######")
    print("(###################################")
    vetorizar = int(input("Escolha: "))

    if cenario == 1:
        cenario_1(vetorizar)
    elif cenario == 2:
        cenario_2(vetorizar)
    else:
        print("Entrada inválida!")

    

if __name__ == '__main__':
    try:
        main()
    except     KeyboardInterrupt:
        print("Keyboard interrupt.")
