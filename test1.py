# Load Pupl
import pulp
dir(pulp)

# Define Variable
x = pulp.LpVariable('x', lowBound=0)
y = pulp.LpVariable('y', lowBound=0)

#Objective Function
max_z = pulp.LpProblem('Maximize_Z', pulp.LpMaximize)
max_z += 5*x + 10*y

# Constraints
max_z += x + 2*y <= 120
max_z += x + y >= 60
max_z += x - 2*y >= 0

#Preview
print(max_z)

#Check for the status
pulp.LpStatus[max_z.status]

#Solve/optimization
max_z.solve()

#Check for the status
pulp.LpStatus[max_z.status]

#Method 1
#Get the Values
print(x.varValue) 
print(y.varValue)

#Method 2
for var in max_z.variables(): #stores the values of the variables
    print(var.name, "==>", var.varValue)
    
#Method 3
#Get the optimal value
pulp.value(max_z.objective)
    