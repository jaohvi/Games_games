import adivinhacao
import forca

def escolha_jogo():
    print("Escolha o jogo")
    print ("(1) Adivinhação 1 (2) Adicinhação 2")
    jogo=int(input("Qual jogo? Digite: "))
    if(jogo==1):
        print("Jogo 1")
        adivinhacao.jogar_adivinhacao1()
    elif(jogo==2):
        print("Jogo 2")
        forca.jogar()
if(name=="main"):
    escolha_jogo()