import math 
import numpy as np 

SP = float(67.836)
RJ = float(36.678)
MG = float(29.229)
ES = float(27.165)
outros = float(19.849)

total = SP + RJ + MG + ES + outros





print(f'São Paulo representa {(SP/total * 100):2f}% do valor total mensal') 
print(f'Rio de Janeiro representa {(RJ/total * 100):2f}% do valor total mensal') 
print(f'Minas Gerais representa {(MG/total * 100) :2f}% do valor total mensal') 
print(f'Espirito Santo representa {(ES/total * 100) :2f}% do valor total mensal') 
print(f'"outros" representa {(outros/total * 100)}% do valor total mensal') 

