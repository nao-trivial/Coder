# Leitura do valor de n (entrada do usuário)
n = int(input().strip())

# Casos base da sequência
if n == 1 or n == 2:
    print(1)
else:
    # Inicialização do array de memoização
    dp = [0] * (n + 1)  # Criamos n+1 posições (0 não utilizado)
    dp[1] = 1  # Q(1) = 1
    dp[2] = 1  # Q(2) = 1
    
    # Preenchimento iterativo do array
    for i in range(3, n + 1):
        # Aplicação da fórmula recursiva usando valores já calculados
        dp[i] = dp[i - dp[i - 1]] + dp[i - dp[i - 2]]
    
    # Saída do resultado
    print(dp[n])