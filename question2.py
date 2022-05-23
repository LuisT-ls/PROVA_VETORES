from math import prod


vetor1 = []
vetor2 = []
vetor3 = []

i = 0

for i in range(10):
    num1 = int(input())
    vetor1.append(num1)
    
for i in range(10):
    num2 = int(input())
    vetor2.append(num2)
    
product = [x * y for x, y in zip(vetor1,vetor2)]
print(product)