from pulp import *

# Criação do problema de maximização
prob = LpProblem("Maximize_Profit", LpMaximize)

# Variáveis de decisão
# Exemplo: x1, x2, ..., xn representam a quantidade de cada brinquedo
x = [LpVariable(f"x{i}", lowBound=0, cat=LpInteger) for i in range(1, n+1)]

# Função objetivo
prob += lpSum([profit[i-1] * x[i-1] for i in range(1, n+1)])

# Restrições de capacidade de produção para cada brinquedo
for i in range(1, n+1):
    prob += x[i-1] <= capacity[i-1]

# Restrições de capacidade de produção total
prob += lpSum(x) <= max_total_capacity

# Restrições para pacotes especiais
# Exemplo: 3x1 + 5x2 + 2x3 <= 130 (para o pacote especial {1, 2, 3})
for i in range(p):
    indices = [products_in_bundle[i][j] for j in range(3)]
    prob += lpSum([x[index-1] for index in indices]) <= bundle_profit[i]

# Resolução do problema
prob.solve()

# Exibição da solução
print("Lucro máximo diário:", value(prob.objective))