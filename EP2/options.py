from metodos import *

def option(N, L, sigma, K, T, r, t, S0, vetorizar=True):

    #u_ij = calcula_u(N, M, L, sigma, K, T, vetorizar)
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    print(u_ij[9000][13])
    V_ij = get_V_ij(N, M, T, r, u_ij)
    # u_analitico = get_u_analitico_normal(sigma, K, M, N, T, L)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    print(f"V no presente = {str(V_presente_aprox)} V no presente interpolado = {str(V_presente_interpol)}")

def cenario_1(vetorizar):
    N = 10000    
    L = 10       
    sigma = 0.01
    K = 1.0      
    T = 1.0      
    r = 0.01  
    M = 50 # condicao de estabilidade
       
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

    '''
        Exercício 2
    '''
   
    #Grafico 1 - t = 0.5
    t = 0.5
    valor_comprado = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_lucro(V_ij, t, N, M, L, sigma, K, T, r, valor_comprado, gasto_inicial)
    escreve_grafico(S_list, cenarios, "Lucro e Prejuízo em t = 6 meses", "cenario_1_ex_2_g1.png")

    #Grafico 2 - t = 0.25
    t = 0.25
    valor_comprado = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 3 meses", "cenario_1_ex_2_g2.png")

    #Grafico 3 - t = 0.75
    t = 0.75
    valor_comprado = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 9 meses", "cenario_1_ex_2_g3.png")
    
    #Grafico 4 - t = 0.0
    t = 0.0
    valor_comprado = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 0 meses", "cenario_1_ex_2_g4.png")

    #Grafico 5 - t = T
    t = T
    valor_comprado = 1000
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

    t = 0.5    

    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    escreve_arquivo(arquivo, N, L, M, K, sigma, T, r, S0, t, precificacao)
    escreve_terminal( N, L, M, K, sigma, T, r, S0, t, precificacao)

    #Grafico 1 - t = 0.5
    t = 0.5
    valor_comprado = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_lucro(V_ij, t, N, M, L, sigma, K, T, r, valor_comprado, gasto_inicial)
    escreve_grafico(S_list, cenarios, "Lucro e Prejuízo em t = 6 meses", "cenario_1_ex_3_g1.png")

    #Grafico 2 - t = 0.25
    t = 0.25
    valor_comprado = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 3 meses", "cenario_1_ex_3_g2.png")

    #Grafico 3 - t = 0.75
    t = 0.75
    valor_comprado = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 9 meses", "cenario_1_ex_3_g3.png")
    
    #Grafico 4 - t = 0.0
    t = 0.0
    valor_comprado = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 0 meses", "cenario_1_ex_3_g4.png")

    #Grafico 5 - t = T
    t = T
    valor_comprado = 1000
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

    #Grafico 1 - t = 0.5
    t = 0.5
    valor_comprado = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_lucro(V_ij, t, N, M, L, sigma, K, T, r, valor_comprado, gasto_inicial)
    escreve_grafico(S_list, cenarios, "Lucro e Prejuízo em t = 6 meses", "cenario_1_ex_4_g1.png")

    #Grafico 2 - t = 0.25
    t = 0.25
    valor_comprado = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 3 meses", "cenario_1_ex_4_g2.png")

    #Grafico 3 - t = 0.75
    t = 0.75
    valor_comprado = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 9 meses", "cenario_1_ex_4_g3.png")
    
    #Grafico 4 - t = 0.0
    t = 0.0
    valor_comprado = 1000
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    precificacao = V_presente_interpol * 1000
    gasto_inicial = precificacao
    cenarios, S_list = gera_preco_ativo(V_ij, t, N, M, L, sigma, K, T, r)
    escreve_grafico(S_list, cenarios, "Valor da opção para diferentes preços do ativo em t = 0 meses", "cenario_1_ex_4_g4.png")

    #Grafico 5 - t = T
    t = T
    valor_comprado = 1000
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
    N = 10000
    L = 10
    sigma = 0.1692
    K = 5.7
    T = 0.25
    r = 0.1075
    S0 = 5.6376
    valor = 100000
    M = 50 # condicao de estabilidade
    
    u_ij = iterador_u_ij(M, N, L, sigma, K, T, r, vetorizar)
    V_ij = get_V_ij(N, M, T, r, u_ij)
    V_presente_aprox, V_presente_interpol = get_V_dado_S(T, M, L, N, 0, S0, K, r, sigma, V_ij)
    print(f"V no presente = {str(V_presente_aprox)} V no presente interpolado = {str(V_presente_interpol)}")
    precificacao = V_presente_interpol * valor
    print(f"Precificacao/premio: {precificacao}")

    custo_total = precificacao + valor*S0
    print(f"Custo total: {custo_total}")

    St = 5.1604718519
    valor_total = St * valor

    lucro = valor_total - custo_total
    print(f"Lucro em 1 de Marco com dolar a R$ 5,16: {lucro}")

def cenario_3():
    pass

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

def main():
 

    print("#####    Escolha um cenário  #######")
    print("##### (1) Cenário fictício   #######")
    print("##### (2) Cenário câmbio     #######")
    print("##### (3) Cenário real       #######")
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
    elif cenario == 3:
        cenario_3(vetorizar)
    else:
        print("Entrada inválida!")

if __name__ == '__main__':
    try:
        main()
    except     KeyboardInterrupt:
        print("Keyboard interrupt.")