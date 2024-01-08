import pulp
import sys

# Define Variáveis
input_lines = sys.stdin.readlines()
toys, packs, max_production = list(map(int, input_lines[0].split()))

totalToys = toys + packs
objective = 0
all_toys = 0

profit = [0] * totalToys
variables = [0] * totalToys
max_capacity = [0] * toys
capacity = [0] * toys

# Função Objetivo
max_profit = pulp.LpProblem('max_profit', pulp.LpMaximize)

# Define Variáveis
toy_lines = input_lines[1:]

# Cria e define todos os brinquedos e pacotes
for toy in range(totalToys):
    line = toy_lines[toy]

    if toy < toys:
        profit[toy], capacity[toy] = list(map(int, line.split()))
        variables[toy] = pulp.LpVariable(f"t{toy}", lowBound=0, upBound=capacity[toy], cat="Integer")
        
        all_toys += variables[toy]
        
        max_capacity[toy] += variables[toy]

    else:
        toy1, toy2, toy3, profit[toy] = list(map(int, line.split()))

        variables[toy] = pulp.LpVariable(f"p{toy}", lowBound=0, cat="Integer")
        
        max_capacity[toy1-1] += variables[toy]
        max_capacity[toy2-1] += variables[toy]
        max_capacity[toy3-1] += variables[toy]
        
        all_toys += 3*variables[toy]
        
    # Função Objetivo
    objective += variables[toy] * profit[toy] 

# Função Objetivo
max_profit += objective

for toy in range(toys):
    max_profit += max_capacity[toy] <= capacity[toy]

# Restrição para a capacidade total disponível
max_profit += all_toys <= max_production

# Resolve o problema de otimização
max_profit.solve(pulp.GLPK(msg=0))

# # Imprime os valores das variáveis
print(len(max_profit.constraints))

# Imprime o valor da função objetivo
print(int(pulp.value(max_profit.objective)))