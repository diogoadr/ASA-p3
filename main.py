import pulp

# Define Variable
# t - number of toys
# p - number of packs
# max - max capacity of production
t, p, max = map(int, input("").split())

totalToys = t+p

#all variables corresponding to the toys
x = [0]*(totalToys)
#capacity
c = [0]*(totalToys)
#profit
l = [0]*(totalToys)

# Define Variables
variables = pulp.LpVariable.dicts("x", range(totalToys), lowBound=0, cat="Integer")

#create and define all the toys and packs
for i in range(totalToys):
    
    if i <= t-1:
        l[i], c[i] = map(int, input("").split())
        
    else:
        t1, t2, t3, l[i] = map(int, input("").split())
        c[i] = min(c[t1-1], c[t2-1], c[t3-1]) # corrected index is x-1
        
    #objective += l[i]*x[i] maximize the profit with the quantities of each toy (pack counts as a toy)

#Objetive Function
max_profit = pulp.LpProblem('max_profit', pulp.LpMaximize)
    
# max_profit += profit*xi + ... + profit*xt 
max_profit += pulp.lpSum([l[i] * variables[i] for i in range(totalToys)])

#Constraints
# xi <= ci  
for i in range(totalToys):
    max_profit += variables[i] <= c[i]

# sumxi <= max
max_profit += pulp.lpSum([variables[i] for i in range(totalToys)]) <= max


#explore the ideia of the bundle being another toy with the profit 
#given and the capacity of the min of the products in the bundle

#preview
# print(max_profit)
solver = pulp.LpSolver_CMD(msg=False)
max_profit.solve()

#Solve
print(int(pulp.value(max_profit.objective)))













# Create decision variables dynamically
# variables = LpVariable.dicts("x", range(len(coefficients)), lowBound=0, cat="Integer")

# # Add objective function
# prob += lpSum([coefficients[i] * variables[i] for i in range(len(coefficients))])

# # Add constraints
# for constraint in constraints:
#     prob += lpSum([constraint[i] * variables[i] for i in range(len(coefficients))]) <= constraint[-1]
