# A company makes two products (X and Y) using two machines (A and B). Each unit of X that is produced requires
# 50 minutes processing time on machine A and 30 minutes processing time on machine B. Each unit of Y that is produced 
# requires 24 minutes processing time on machine A and 33 minutes processing time on machine B.

# At the start of the current week there are 30 units of X and 90 units of Y in stock. Available processing time on machine A is
# forecast to be 40 hours and on machine B is forecast to be 35 hours.

# The demand for X in the current week is forecast to be 75 units and for Y is forecast to be 95 units. Company policy is to
# maximise the combined sum of the units of X and the units of Y in the stock at the end of the week.

# Formulate the problem of deciding how much of each product to make in the current week as a linear program


# let x be for unit X
# let y be for unit Y

# Constraints
# A 50 min x 24 min y <= 40 hours x (60 min)
# B 30 min x 33 min y <= 35 hours x (60 min)

# Start and End
# x 30 75
# y 90 95

# x + y = 50 (75-30) + (95-90)

#Define variables
import pulp
dir(pulp)

# Define Variable
X = pulp.LpVariable('X', lowBound=0)
Y = pulp.LpVariable('Y', lowBound=0)

#Objective Function
max_profit = pulp.LpProblem('Maximize_Profit', pulp.LpMaximize)

max_profit += X + Y - 50

#Constraints
max_profit += 50*X + 24*Y <= 40*60 
max_profit += 30*X + 33*Y <= 35*60 
max_profit += X >= 75 - 30
max_profit += Y >= 95 - 90

#Solve
max_profit.solve()