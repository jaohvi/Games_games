import random
def jogar_adivinhacao1():
    print("***************")
    print("BEM VINDO PARA ADIVINHAR")
    print("***************")
    print ("Qual nível de dificuldade?")
    print("Sendo: (1) Fácil (2) Médio (3) Díficil")
    nivel=int(input("Digite o nível: "))
    #numero=round(random.random()*100) #random gera entre 0.0 e 1.0
    numero= random.randrange(1,101)
    pontos=1000
    print(numero)
    if(nivel==1):
        tentativas= 20
    elif(nivel==2):
        tentativas=10
    else:
        tentativas=3

    #rodada=1
    #while(rodada <= tentativas):
    for (rodada) in range(1,tentativas+1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite um número entre 0 e 100:")
        chute = int(chute_str)
        print("Você digitou:", chute_str)

        if(chute<1 or chute >100):
            print("Digite um valor entre 0 e 100!")
            continue
        x = numero - chute
        if (x==0):
            print("Parabéns, você acertou!!")
            print("Fim de jogo.")
            break #serve para acabar com o loop do for
            #rodada=5
        elif(x!=0):
            if(x<0):
                    print("O seu chute foi maior que o numero secreto")
            else:
                    print("O seu chute foi menor que o numero secreto")
            pontosperdidos = abs(numero - chute)
            pontos = pontos - pontosperdidos
        if(rodada==tentativas):
            print("O numero secreto era {}".format(numero))
    print("Você fez {:04d} pontos".format(pontos))
            #chute_str = input("Digite o seu número:")
          #  print("Você digitou:", chute_str)
          #  chute = int(chute_str)
           # x = numero - chute
           # rodada= rodada + 1
if(name=="main"):
    jogar_adivinhacao1()