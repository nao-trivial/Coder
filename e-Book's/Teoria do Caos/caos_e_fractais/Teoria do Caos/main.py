from logistic_map import MapaLogistico
from cobweb_plotter import TeiaAranha

# Ciclo estável para r = 3.2
r = 3.2
mapa = MapaLogistico(r)

# Encontre o ciclo numericamente (pode ser feito com iteração)
x0 = 0.5
orb = mapa.orbita(x0, 100)
ciclo = list(set(orb[-20:]))  # simplificado: últimos valores distintos
ciclo.sort()
print(f"Ciclo aproximado: {ciclo}")

# Análise de estabilidade
d, estavel = mapa.estabilidade_ciclo(ciclo)
print(f"Derivada do ciclo: {d:.3f} → Estável? {estavel}")

# Teia de aranha
teia = TeiaAranha(mapa, x0=0.52, iteracoes=50)
teia.plotar(ciclo=ciclo, titulo=f'Mapa Logístico r={r} (Ciclo estável)')