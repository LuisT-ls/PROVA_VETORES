G = []
R = []

acertos = 0
count = 0

print("\nDigite o gabarito da questão  ")

for count in range(20):
    count = + 1
    gabarito = str(input())
    G.append(gabarito)

for count in range(50):
    count = + 1
    
    print("\nDigite a resposta do aluno ")
    
    for i in range(20):
        respostas = str(input())
        R.append(respostas)
        
    if(set(R) == set(G)):
        print("\nAPROVADO")
    else:
        print("\nREPROVADO")