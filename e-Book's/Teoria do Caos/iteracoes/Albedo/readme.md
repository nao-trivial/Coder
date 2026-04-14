# Teoria do Modelo Albedo-Temperatura: Do Balanço Radiativo à Bifurcação

## 1. A equação fundamental

O modelo descreve a evolução da temperatura média da superfície terrestre (ou de um sistema simplificado gelo-oceano) através do balanço entre radiação absorvida e radiação emitida:

\[
C \frac{dT}{dt} = (1 - A(T))\, Q - \sigma T^4
\]

Onde:

- \(T\) = temperatura (K)
- \(C\) = capacidade térmica efetiva (J/m²·K) – controla a inércia térmica
- \(A(T)\) = albedo (refletividade) – função da temperatura
- \(Q\) = forçamento solar médio (W/m²)
- \(\sigma = 5.67 \times 10^{-8}\) W/m²·K⁴ (constante de Stefan-Boltzmann)

### 1.1 Significado físico de cada termo

- **Radiação absorvida**: \((1 - A)Q\) – quanto menor o albedo, mais calor entra.
- **Radiação emitida**: \(\sigma T^4\) – todo corpo aquecido emite radiação térmica (lei de Stefan-Boltzmann).
- **Derivada temporal**: quando a absorção supera a emissão, a temperatura aumenta (\(dT/dt > 0\)).

## 2. O papel do albedo: feedback positivo

O albedo não é constante; ele depende da temperatura porque o gelo derrete quando esquenta:

\[
A(T) =
\begin{cases}
A_{\text{gelo}} \approx 0.7 & \text{se } T \ll T_{\text{fusão}} \\
A_{\text{água}} \approx 0.2 & \text{se } T \gg T_{\text{fusão}}
\end{cases}
\]

Entre esses extremos, \(A(T)\) varia suavemente (transição linear ou sigmoide).

**Realimentação positiva**:

1. Aumento de \(T\) → derretimento do gelo → diminuição de \(A\).
2. Menor \(A\) → maior absorção \((1-A)Q\) → mais aquecimento.
3. O aquecimento acelera o próprio derretimento → ciclo de amplificação.

Essa é a origem do **ponto de não retorno**: uma vez que o gelo derrete além de um limiar, o sistema não consegue mais voltar ao estado gelado, mesmo que o forçamento \(Q\) retorne ao valor original (histerese).

## 3. Solução da equação e estados estacionários

No equilíbrio, \(dT/dt = 0\), logo:

\[
(1 - A(T))\, Q = \sigma T^4
\]

Esta equação pode ter **múltiplas soluções** para um mesmo \(Q\) devido à dependência de \(A\) com \(T\). Graficamente, as soluções são os cruzamentos entre a curva de emissão \(\sigma T^4\) e a reta de absorção \((1 - A(T)) Q\).

### 3.1 Exemplo de bifurcação

- Para \(Q\) baixo: existe apenas um estado estacionário frio (gelado).
- Para \(Q\) intermediário: surgem **três** estados: um frio (estável), um instável (no meio) e um quente (estável).
- Para \(Q\) alto: apenas o estado quente (sem gelo) permanece.

O **ponto crítico** ocorre quando os estados frio e instável colidem e desaparecem – é a bifurcação de dobra (*saddle-node bifurcation*). A partir desse valor de \(Q\), mesmo uma pequena perturbação pode levar o sistema irreversivelmente ao estado quente.

## 4. Discretização temporal: iteração linear por partes

Para simular numericamente, usamos o método de Euler (diferenças finitas):

\[
T_{n+1} = T_n + \frac{\Delta t}{C}\Big[(1 - A(T_n))Q - \sigma T_n^4\Big]
\]

Se aproximarmos \(A(T)\) por uma função degrau e linearizarmos o termo de emissão em torno de um ponto fixo, obtemos duas **equações lineares**:

- **Ramo gelado** (para \(T \le T_{\text{fusão}}\)):  
  \(T_{n+1} = T_n + \alpha_{\text{gelo}}(Q - Q_{\text{eq,gelo}})\)
- **Ramo água** (para \(T > T_{\text{fusão}}\)):  
  \(T_{n+1} = T_n + \alpha_{\text{água}}(Q - Q_{\text{eq,água}})\)

Cada ramo tem um ponto fixo \(T^*\) onde \(T_{n+1} = T_n\). A estabilidade desses pontos fixos é dada pelo fator de amplificação \(a = 1 + \alpha \cdot \text{(derivada)}\). Para o ramo gelado, \(a < 1\) antes do ponto crítico; após o crítico, o ponto fixo deixa de existir ou se torna instável.

## 5. O diagrama de bifurcação e o ponto de não retorno

O diagrama de bifurcação plota os **estados estacionários** (valores de \(T\) após longo tempo) em função do parâmetro \(Q\).

- **Região reversível** (\(Q < Q_c\)): se você perturbar a temperatura, o sistema retorna ao mesmo estado gelado.
- **Região de histerese** (\(Q\) próximo de \(Q_c\)): dois estados estáveis coexistem – o sistema pode estar gelado ou descongelado dependendo da história.
- **Região catastrófica** (\(Q > Q_c\)): apenas o estado descongelado é estável. Qualquer desvio para o gelado é irreversível.

> **Analogia com trauma**:  
> Abaixo de um limiar de estresse (parâmetro de controle), a pessoa retorna ao equilíbrio após uma adversidade.  
> Acima do limiar, ocorre uma mudança estrutural na personalidade – o sistema “salta” para um novo atrator.  
> Isso não é falha de caráter; é um comportamento universal de sistemas não lineares.

## 6. Por que a iteração linear ajuda a entender?

A equação completa é não linear, mas **localmente** (em torno de um estado estacionário) podemos linearizá-la:

\[
\delta T_{n+1} \approx \left[1 + \frac{\Delta t}{C}\left( -\frac{dA}{dT}Q - 4\sigma T^4 \right) \right] \delta T_n
\]

O termo entre colchetes é o **fator de amplificação** \(a\). Se \(|a| < 1\), a perturbação \(\delta T\) desaparece (sistema estável). Se \(|a| > 1\), a perturbação cresce (instabilidade). A bifurcação ocorre quando \(a\) cruza o valor 1.

Assim, o comportamento do sistema albedo-temperatura pode ser decomposto em **sequências de iterações lineares** que trocam de regime quando a temperatura ultrapassa o ponto de fusão. Essa visão por partes é didática e conecta diretamente com o conceito elementar de iteração linear.

## 7. Conclusão

O modelo albedo-temperatura é um exemplo rico para ensinar:

- Balanço energético e feedbacks climáticos.
- Sistemas dinâmicos não lineares e bifurcações.
- Pontos de não retorno e histerese.
- Conexão entre iteração linear (simples) e comportamento complexo.

Compreender essa matemática é essencial não só para as ciências da Terra, mas também para áreas como ecologia, economia e psicologia, onde limiares e mudanças de regime são comuns.