numeros_escondido = 10
i=0
while True:   
    num = int(input("Tente descobrir o número escondido: "))
    if num < numeros_escondido: 
        print("O número digitado é menor, tente outra vez")
        i+=1
    elif num > numeros_escondido:
        print("O número digitado é maior, tente outra vez")
        i=+1
    else:
        print("Você acertou o número escolhido!")
        break

print(f"Sua tentativas para acertar foram {i}")

