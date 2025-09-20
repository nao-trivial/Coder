# Nome do arquivo: Metodo_Ponto_Fixo.py
# Resolve equações usando o método iterativo de ponto fixo

def metodo_ponto_fixo(g, x0, tolerancia=1e-6, max_iter=100):
    """
    Encontra a raiz de uma equação usando o método do ponto fixo.

    Parâmetros:
    g (função): Função de iteração g(x)
    x0 (float): Palpite inicial
    tolerancia (float): Precisão desejada
    max_iter (int): Número máximo de iterações

    Retorna:
    float: Aproximação da raiz
    int: Número de iterações utilizadas
    """
    print("Iteração |   x       |   Erro    ")
    print("---------|-----------|-----------")
    
    for i in range(max_iter):
        x1 = g(x0)
        erro = abs(x1 - x0)
        
        print(f"{i:9} | {x1:.6f} | {erro:.6f}")
        
        if erro < tolerancia:
            return x1, i+1
        
        x0 = x1
    
    raise ValueError("O método não convergiu após {} iterações".format(max_iter))

# Exemplo de uso:
if __name__ == "__main__":
    # Exemplo: encontrar a raiz de x = cos(x)
    import math
    g = math.cos
    raiz, iteracoes = metodo_ponto_fixo(g, x0=0.5)
    print(f"\nRaiz aproximada: {raiz:.6f}")
    print(f"Iterações: {iteracoes}")