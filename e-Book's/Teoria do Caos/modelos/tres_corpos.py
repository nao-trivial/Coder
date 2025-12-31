import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# SIMULADOR SIMPLIFICADO DO PROBLEMA DOS 3 CORPOS
# Versão otimizada para Pydroid3 em celulares
# ============================================================================

def aceleracao_gravitacional(pos1, pos2, massa2, G=1.0):
    """Calcula a aceleração gravitacional entre dois corpos"""
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    dz = pos2[2] - pos1[2]
    
    # Distância ao quadrado (evitar divisão por zero)
    distancia2 = dx*dx + dy*dy + dz*dz + 1e-10
    distancia = np.sqrt(distancia2)
    
    # Fator gravitacional
    fator = G * massa2 / (distancia2 * distancia)
    
    return np.array([fator * dx, fator * dy, fator * dz])

def integracao_simplificada(cond_iniciais, massas, passos=1000, dt=0.1):
    """
    Integração simplificada usando método de Euler-Cromer
    Mais estável e menos pesado para celulares
    """
    n_corpos = len(massas)
    
    # Inicializa arrays para posições e velocidades
    pos = np.zeros((n_corpos, 3, passos))
    vel = np.zeros((n_corpos, 3, passos))
    
    # Condições iniciais
    for i in range(n_corpos):
        pos[i, :, 0] = cond_iniciais[i*6:i*6+3]
        vel[i, :, 0] = cond_iniciais[i*6+3:i*6+6]
    
    # Loop de integração
    for passo in range(1, passos):
        for i in range(n_corpos):
            # Soma acelerações de todos os outros corpos
            acel = np.zeros(3)
            for j in range(n_corpos):
                if i != j:
                    acel += aceleracao_gravitacional(pos[i, :, passo-1], 
                                                    pos[j, :, passo-1], 
                                                    massas[j])
            
            # Atualiza velocidade e posição (Euler-Cromer)
            vel[i, :, passo] = vel[i, :, passo-1] + acel * dt
            pos[i, :, passo] = pos[i, :, passo-1] + vel[i, :, passo] * dt
    
    return pos, vel

def simular_efeito_borboleta(pos_inicial, massas, perturbacao=1e-6, passos=500, dt=0.1):
    """Simula o efeito borboleta com duas condições iniciais ligeiramente diferentes"""
    # Primeira simulação
    pos1, vel1 = integracao_simplificada(pos_inicial, massas, passos, dt)
    
    # Segunda simulação com pequena perturbação
    pos_perturbado = pos_inicial.copy()
    pos_perturbado[12] += perturbacao  # Perturba a posição x do terceiro corpo
    
    pos2, vel2 = integracao_simplificada(pos_perturbado, massas, passos, dt)
    
    return pos1, pos2

def calcular_lyapunov_simples(pos1, pos2, dt=0.1):
    """Calcula um expoente de Lyapunov aproximado de forma simples"""
    # Distância entre as trajetórias do corpo 3
    distancia = np.sqrt((pos1[2, 0, :] - pos2[2, 0, :])**2 + 
                       (pos1[2, 1, :] - pos2[2, 1, :])**2)
    
    # Remove zeros para evitar problemas no log
    mascara = distancia > 1e-15
    if np.sum(mascara) > 10:
        # Ajuste linear simples
        x = np.arange(len(distancia))[mascara] * dt
        y = np.log(distancia[mascara])
        
        # Coeficiente angular = expoente de Lyapunov aproximado
        if len(x) > 1:
            coef = np.polyfit(x, y, 1)
            return coef[0]
    
    return 0.0

def criar_grafico_simples(pos, massas, titulo="Trajetórias dos 3 Corpos"):
    """Cria um gráfico simples das trajetórias"""
    plt.figure(figsize=(8, 6), dpi=80)  # Tamanho reduzido para celular
    
    # Cores e labels
    cores = ['gold', 'blue', 'red']
    labels = ['Corpo 1 (Sol)', 'Corpo 2 (Terra)', 'Corpo 3 (Perturbação)']
    
    # Plota cada trajetória
    for i in range(3):
        plt.plot(pos[i, 0, :], pos[i, 1, :], 
                color=cores[i], label=labels[i], 
                linewidth=2 if i == 0 else 1, alpha=0.8)
    
    # Marca as posições iniciais
    for i in range(3):
        plt.scatter(pos[i, 0, 0], pos[i, 1, 0], 
                   color=cores[i], s=100, zorder=5)
        plt.text(pos[i, 0, 0], pos[i, 1, 0], f' m={massas[i]}', 
                fontsize=10, verticalalignment='bottom')
    
    plt.xlabel('Posição X', fontsize=12)
    plt.ylabel('Posição Y', fontsize=12)
    plt.title(titulo, fontsize=14)
    plt.legend(loc='upper right', fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    
    # Adiciona informações no gráfico
    plt.text(0.02, 0.02, f'Passos: {pos.shape[2]}\nDt: 0.1', 
            transform=plt.gca().transAxes, fontsize=9,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    return plt.gcf()

# ============================================================================
# CONFIGURAÇÃO DA SIMULAÇÃO
# ============================================================================

print("=" * 50)
print("SIMULADOR DE 3 CORPOS - Versão Mobile")
print("=" * 50)

# Condições iniciais simplificadas (apenas 2D para economizar recursos)
# [x1, y1, z1, vx1, vy1, vz1, x2, y2, z2, ...]
condicoes_iniciais = np.array([
    # Corpo 1: Sol (no centro, praticamente parado)
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    # Corpo 2: Terra (órbita circular)
    1.0, 0.0, 0.0, 0.0, 0.8, 0.0,
    # Corpo 3: Lua/Asteroide (órbita perturbada)
    1.1, 0.2, 0.0, 0.0, 0.9, 0.0
])

massas = [50.0, 1.0, 0.1]  # Massas relativas

# ============================================================================
# EXECUÇÃO PRINCIPAL
# ============================================================================

try:
    print("\n[1/3] Executando simulação principal...")
    pos, vel = integracao_simplificada(condicoes_iniciais, massas, 
                                       passos=800, dt=0.08)
    
    print("[2/3] Calculando efeito borboleta...")
    pos1, pos2 = simular_efeito_borboleta(condicoes_iniciais, massas, 
                                         perturbacao=1e-5, passos=400, dt=0.1)
    
    print("[3/3] Criando visualizações...")
    
    # Gráfico 1: Trajetórias principais
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 1, 1)
    
    # Trajetórias coloridas
    cores = ['gold', 'blue', 'red']
    for i in range(3):
        plt.plot(pos[i, 0, :], pos[i, 1, :], 
                color=cores[i], linewidth=2, alpha=0.8)
    
    plt.title('Trajetórias dos 3 Corpos (Sistema Solar Simplificado)', fontsize=14)
    plt.xlabel('Posição X')
    plt.ylabel('Posição Y')
    plt.grid(True, alpha=0.3)
    plt.legend(['Sol (m=50)', 'Terra (m=1)', 'Asteroide (m=0.1)'])
    
    # Gráfico 2: Efeito Borboleta
    plt.subplot(2, 1, 2)
    
    # Calcula distância entre trajetórias perturbadas
    distancia = np.sqrt((pos1[2, 0, :] - pos2[2, 0, :])**2 + 
                       (pos1[2, 1, :] - pos2[2, 1, :])**2)
    
    # Expoente de Lyapunov aproximado
    lyapunov = calcular_lyapunov_simples(pos1, pos2, dt=0.1)
    
    plt.semilogy(np.arange(len(distancia)) * 0.1, distancia, 'r-', linewidth=2)
    plt.xlabel('Tempo')
    plt.ylabel('Distância (escala log)')
    plt.title(f'Efeito Borboleta | Lyapunov ≈ {lyapunov:.4f}', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.text(0.7, 0.9, f'λ = {lyapunov:.4f}', transform=plt.gca().transAxes,
             bbox=dict(boxstyle="round", facecolor="yellow", alpha=0.8))
    
    plt.tight_layout()
    plt.show()
    
    # ============================================================================
    # ANIMAÇÃO SIMPLES (OPCIONAL - mais leve que matplotlib.animation)
    # ============================================================================
    print("\nDeseja ver uma animação simples? (S/N)")
    resposta = input().strip().upper()
    
    if resposta == 'S':
        print("Criando animação passo a passo...")
        
        # Mostra alguns passos da animação
        passos_animacao = min(20, pos.shape[2] // 40)
        
        plt.figure(figsize=(8, 6))
        for passo in range(0, pos.shape[2], passos_animacao):
            plt.clf()
            
            # Plota trajetória completa até o passo atual
            for i in range(3):
                plt.plot(pos[i, 0, :passo+1], pos[i, 1, :passo+1], 
                        color=cores[i], linewidth=1, alpha=0.5)
            
            # Plota posições atuais
            for i in range(3):
                plt.scatter(pos[i, 0, passo], pos[i, 1, passo], 
                          color=cores[i], s=100, zorder=5)
            
            plt.xlim(np.min(pos[:, 0, :]) - 0.5, np.max(pos[:, 0, :]) + 0.5)
            plt.ylim(np.min(pos[:, 1, :]) - 0.5, np.max(pos[:, 1, :]) + 0.5)
            plt.title(f'Passo {passo}/{pos.shape[2]}')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.grid(True, alpha=0.3)
            
            plt.pause(0.1)  # Pequena pausa entre frames
        
        plt.show()
    
    # ============================================================================
    # INFORMAÇÕES FINAIS
    # ============================================================================
    print("\n" + "=" * 50)
    print("ANÁLISE DA SIMULAÇÃO:")
    print("=" * 50)
    
    # Energia total aproximada
    energia_cinetica = 0
    for i in range(3):
        v2 = np.sum(vel[i, :, -1]**2)
        energia_cinetica += 0.5 * massas[i] * v2
    
    print(f"1. Energia cinética final: {energia_cinetica:.4f}")
    print(f"2. Expoente de Lyapunov: {lyapunov:.6f}")
    
    if lyapunov > 0.01:
        print("   → Sistema CAÓTICO detectado!")
    elif lyapunov > 0:
        print("   → Sistema levemente caótico")
    else:
        print("   → Sistema estável")
    
    print(f"3. Distância final entre órbitas: {distancia[-1]:.2e}")
    
    # Sugestões para experimentar
    print("\n" + "=" * 50)
    print("EXPERIMENTE MODIFICAR:")
    print("=" * 50)
    print("1. Altere as massas: massas = [100, 1, 0.01]")
    print("2. Mude as velocidades iniciais")
    print("3. Aumente a perturbação para 0.01")
    print("4. Adicione um 4º corpo para mais caos!")
    
except Exception as e:
    print(f"\n⚠️  Erro durante a execução: {e}")
    print("\nDicas para solucionar:")
    print("1. Certifique-se de ter numpy e matplotlib instalados")
    print("2. Reduza o número de passos se o celular for lento")
    print("3. Use valores menores para dt (ex: 0.05)")
    print("4. Execute em partes menores do código")

# ============================================================================
# CÓDIGO PARA TESTES RÁPIDOS (descomente para usar)
# ============================================================================
"""
# Teste rápido com menos passos
print("\n[TESTE RÁPIDO] Executando simulação reduzida...")
pos_test, vel_test = integracao_simplificada(condicoes_iniciais, massas, 
                                           passos=200, dt=0.1)

plt.figure(figsize=(6, 6))
for i in range(3):
    plt.plot(pos_test[i, 0, :], pos_test[i, 1, :], linewidth=2)
plt.title('Teste Rápido - 200 Passos')
plt.show()
"""