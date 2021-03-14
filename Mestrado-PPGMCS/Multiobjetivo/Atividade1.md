1) Uma fábrica de computadores produz dois modelos de microcomputadores A e B. Os lucros de A e B são, respectivamente, R$ 180 e R$ 300. O modelo A requer, na sua produção, um gabinete pequeno e uma unidade de disco. O modelo B requer 1 gabinete grande e 2 unidades de disco. Existem no estoque 60 do gabinete pequeno, 50 do gabinete grande e 120 unidades de disco. Crie um modelo matemático para o esquema de produção que maximize o lucro.

**Variáveis de decisão:**

A: Quantidade de microcomputadores do tipo A, a serem produzidos<br/>
B: Quantidade de microcomputadores do tipo B, a serem produzidos<br/>

**Função objetivo:**

Max F(A, B) = 180 * A + 300 * B

**Restrições:**

r1: 1 * A <= 60 // gabinetes pequenos<br/>
r2: 1 * B <= 50 // gabinetes grandes<br/>
r3: 1 * A + 2 * B <= 120 // unidades de disco<br/>
r4: A, B são números inteiros positivos.<br/>

2) Um fundo de investimentos tem até R$ 300.000 para aplicar em duas ações. A empresa D é diversificada (tem 40% do seu capital aplicado em cerveja e o restante aplicado em refrigerantes) e espera-se que forneça bonificações de 12%. A empresa N não é diversificada (produz apenas cerveja) e espera-se que distribua bonificações de 20%. Crie um modelo matemático para o esquema de investimento que maximize o lucro, considerando as restrições a seguir.

O investimento na empresa diversificada pode atingir R$ 270.000.<br/>
O investimento na empresa não-diversificada pode atingir R$ 150.000.<br/>
O investimento em cada produto (cerveja ou refrigerante) pode atingir R$ 180.000.<br/>

**Variáveis de decisão:**

D: investimento na empresa D<br/>
N: investimento na empresa N<br/>

**Função objetivo:**

Max F(D, N) = 0,12 * D * (0,4 + 0,6) + 0,20 * N * (1)

**Restrições:**

r1: D + N <= 300.000 // investimento nas empresas D e N.<br/>
r2: D <= 270.000 // investimento na empresa D (diversificada)<br/>
r3: N <= 150.000 // investimento na empresa N (não diversificada)<br/>
r4: 0,4 * D + 1 * N <= 180.000 // investimento em cerveja<br/>
r5: 0,6 * D <= 180.000 // investimento em refrigerante<br/>
r6: D, N >= 0<br/>

3) Uma pequena fábrica de móveis produz dois modelos de molduras ornamentais, cujos preços de venda são, respectivamente, R$110,00 e R$65,00. Ela possui 7 peças de madeira e dispõe de 30 horas de trabalho para confeccionar os dois modelos, sendo que o modelo A requer 2 peças de madeira e 5 horas de trabalho, enquanto o modelo B necessita de 1 peça de madeira e 7 horas de trabalho. Crie o modelo matemático para determinar quantas molduras de cada modelo a fábrica deve montar se desejar maximizar o rendimento obtido com as vendas.

**Variáveis**

A: quantidade de moldura do tipo A<br/>
B: quantidade de moldura do tipo B<br/>

**Função Objetivo**

Max F(A,B) = 110A + 65B

**Restrições**

r1: 2A + 1B <= 7 //Madeira<br/>
r2: 5A + 7B <= 30 //Horas de trabalho<br/>
r3: A e B pertencem ao conjunto dos números naturais<br/>

4) Um agricultor está interessado na produção do milho e algodão. Ele possui área disponível de 100 ha e sabe que pode dispor, durante o período de produção de milho e algodão, de 3.600 homens/dia e 240 dias de trabalho de um trator médio. Com base em sua experiência, ele sabe que naquela terra e com sua técnica de produção, o milho produz 2.000 Kg/ha e o algodão 1.800 kg/ha. A cultura do milho exige 30 homens/dia por ha e 4 dias de serviço de trator por hectare, enquanto o algodão exige 60 homens/dia por ha e 2 dias de trator por ha. As perspectivas de preço são de R$ 1.700,00 por tonelada de milho e de R$ 2.040,00 por tonelada de algodão. Crie um modelo matemático para identificar qual a combinação dessas 2 linhas de produção que lhe pode proporcionar a maior renda possível.

**Variáveis de decisão:**

M: área em hectares disponíveis para a produção do milho<br/>
A: área em hectares disponíveis para a produção do algodão<br/>

**Função objetivo:**

Max F(M, A) = 1700 * 2 * M + 2040 * 1,8 * A

**Restrições:**

r1: M + A <= 100  // hectares disponíveis para os dois cultivos.<br/>
r2: 30 * M + 60 * A <= 3.600 // homens por dia<br/>
r3: 4 * M + 2 * A <= 240 // dias de trator médio<br/>
r4: M, A >= 0<br/>

5) Uma fábrica produz dois artigos A e B, que devem passar por duas máquinas diferentes M1 e M2. M1 tem 12 horas de capacidade diária disponível e M2 tem 5 horas. Cada unidade de produto A requer 2 horas em ambas as máquinas. Cada unidade de produto B requer 3 horas em M1 e 1 hora em M2. O lucro líquido de A é de R$60,00 por unidade e o de B, R$ 70,00 por unidade. Crie o modelo matemático para determinar a quantidade a ser produzida de A e B a fim de se ter um lucro máximo.

**Variáveis de decisão:** O que podemos conseguir alterar no problema são as quantidades de artigos A e B, logo as variáveis de decisão são:

qA: quantidade produzida do artigo A<br/>
qB: quantidade produzida do artigo B<br/>

**Função objetivo:**

Max F(qA, qB) = 60 * qA + 70 * qB

**Restrições:**

r1: 2 * qA + 3 * qB <= 12 // horas de capacidade diária disponível da máquina M1<br/>
r2: 2 * qA + 1 * qB <= 5 // horas de capacidade diária disponível da máquina M2<br/>
r3: qA, qB são pertencentes ao conjunto dos números naturais<br/>

6) Certa firma processa dois tipos de fibra sintética (A e B). No departamento responsável pela mistura de ingredientes, que dispõe de 200 horas por mês, a produção é limitada por 2 horas por tonelada da fibra A e 4 horas por tonelada da fibra B. No departamento responsável pela embalagem, as necessidades são 6 horas por tonelada da fibra A e 8 horas para a fibra B, com um total máximo de 480 horas disponível por mês. Para o departamento responsável pelo corte das fibras, as necessidades são 10 e 6 horas por toneladas das fibras A e B, respectivamente. Esse departamento dispõe de apenas 600 horas por mês. Outros departamentos limitam a produção de fibra B a um máximo de 35 toneladas por mês. O lucro é de R$ 8 por tonelada para a fibra A e R$ 10 para a fibra B. Crie o modelo matemático para determinar as quantidades mensais de fibras A e B que devem ser produzidas de forma a maximizar os lucros.

7) .

8) Uma empresa tem disponíveis os seguintes tecidos: 16 m² de algodão, 11 m² de seda e 15 m² de lã. Para confeccionar um terno padrão, são necessários 2 m² de algodão, 1m² de seda e 1 m² de lã. Para um vestido padrão, são necessários 1 m² de algodão, 2 m² de seda e 3 m² de lã. Crie o modelo matemático para definir quantas peças de cada tipo a microempresa deve fabricar para ter o maior lucro possível, considerando que o lucro líquido de um terno é de R$ 300 e de um vestido é de R$ 500.

**Variáveis de decisão:**

qT: quantidade de ternos a serem produzidos<br/>
qV: quantidade de vestidos a serem produzidos<br/>

**Função objetivo:**

Max F(qT, qV) = 300 * qT + 500 * qV

**Restrições:**

r1: 2 * qT + 1 * qV <= 16   // Algodão<br/>
r2: 1 * qT + 2 * qV <= 11 // Seda<br/>
r3: 1 * qT + 3 * qV <= 15  //Lã<br/>
r4: qT, qV pertencem ao conjunto dos naturais.<br/>

