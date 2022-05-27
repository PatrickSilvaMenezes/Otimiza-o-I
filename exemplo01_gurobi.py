import gurobipy as gp
from gurobipy import GRB

#cria novo modelo

model = gp.Model()
model.setParam(GRB.Param.LogToConsole, 0)

#Cria as variaveis do problema

x1 = model.addVar(lb = 0, ub = GRB.INFINITY, vtype = GRB.CONTINUOUS)
x2 = model.addVar(lb = 0, ub = GRB.INFINITY, vtype = GRB.CONTINUOUS)
x3 = model.addVar(lb = 0, ub = GRB.INFINITY, vtype = GRB.CONTINUOUS)

#Define função objetivo
model.setObjective(2*x1 + 5*x2 + x3, sense = GRB.MAXIMIZE)


#define restrições

model.addConstr(x1 + x2 <=6)
model.addConstr(x2 -x3 >= 4)
model.addConstr(4*x1 + 2*x2 +x3 <=15)

#resolve o problema

model.optimize()

#dados da solução encontrada
print(f'Valor da função objetivo:  {model.objVal}')
print(f'Valor das variáveis: x1 = {x1.X}, x2 = {x2.X}, x3 = {x3.X}')