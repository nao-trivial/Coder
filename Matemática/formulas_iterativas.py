import math

# Progressão Aritmética (PA)
def progressao_aritmetica(a1, n, r):
    """
    Calcula o n-ésimo termo e a soma dos n primeiros termos de uma PA.
    
    Args:
        a1 (float): Primeiro termo
        n (int): Número de termos
        r (float): Razão da PA
    
    Returns:
        tuple: (n-ésimo termo, soma dos termos)
    """
    an = a1 + (n - 1) * r
    sn = n * (a1 + an) / 2
    return an, sn

# Progressão Geométrica (PG)
def progressao_geometrica(a1, n, q):
    """
    Calcula o n-ésimo termo e a soma dos n primeiros termos de uma PG.
    
    Args:
        a1 (float): Primeiro termo
        n (int): Número de termos
        q (float): Razão da PG
    
    Returns:
        tuple: (n-ésimo termo, soma dos termos)
    """
    an = a1 * (q ** (n - 1))
    if q == 1:
        sn = n * a1
    else:
        sn = a1 * (1 - q ** n) / (1 - q)
    return an, sn

# Método de Newton-Raphson
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Encontra uma raiz da função f usando o método de Newton-Raphson.
    
    Args:
        f (function): Função alvo
        df (function): Derivada da função
        x0 (float): Palpite inicial
        tol (float): Tolerância (default: 1e-6)
        max_iter (int): Número máximo de iterações (default: 100)
    
    Returns:
        float: Aproximação da raiz
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivada zero. Não foi possível continuar.")
        x = x - fx / dfx
    return x

# Exemplo de uso do Newton-Raphson
def exemplo_newton():
    # Encontrar raiz quadrada de 2 (f(x) = x² - 2)
    f = lambda x: x**2 - 2
    df = lambda x: 2*x
    raiz = newton_raphson(f, df, 1.0)
    return raiz

# Método da Bisseção
def bisseccao(f, a, b, tol=1e-6, max_iter=100):
    """
    Encontra uma raiz da função f no intervalo [a,b] usando o método da bisseção.
    
    Args:
        f (function): Função contínua
        a (float): Limite inferior do intervalo
        b (float): Limite superior do intervalo
        tol (float): Tolerância (default: 1e-6)
        max_iter (int): Número máximo de iterações (default: 100)
    
    Returns:
        float: Aproximação da raiz
    """
    if f(a) * f(b) >= 0:
        raise ValueError("A função deve ter sinais opostos nos pontos a e b.")
    
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

# Método das Secantes
def secantes(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Encontra uma raiz da função f usando o método das secantes.
    
    Args:
        f (function): Função alvo
        x0 (float): Primeiro palpite inicial
        x1 (float): Segundo palpite inicial
        tol (float): Tolerância (default: 1e-6)
        max_iter (int): Número máximo de iterações (default: 100)
    
    Returns:
        float: Aproximação da raiz
    """
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1) < tol:
            return x1
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0, x1 = x1, x2
    return x1

# Exemplos de uso
if __name__ == "__main__":
    print("Progressão Aritmética (a1=2, n=5, r=3):")
    an, sn = progressao_aritmetica(2, 5, 3)
    print(f"Termo a5: {an}, Soma S5: {sn}\n")

    print("Progressão Geométrica (a1=2, n=5, q=3):")
    an, sn = progressao_geometrica(2, 5, 3)
    print(f"Termo a5: {an}, Soma S5: {sn}\n")

    print("Método de Newton-Raphson (raiz quadrada de 2):")
    raiz = exemplo_newton()
    print(f"Raiz aproximada: {raiz}\n")

    print("Método da Bisseção (raiz de x³ - x - 2 no intervalo [1,2]):")
    f = lambda x: x**3 - x - 2
    raiz_b = bisseccao(f, 1, 2)
    print(f"Raiz aproximada: {raiz_b}\n")

    print("Método das Secantes (raiz de x³ - x - 2):")
    raiz_s = secantes(f, 1, 2)
    print(f"Raiz aproximada: {raiz_s}")