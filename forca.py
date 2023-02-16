import random
def jogar():
    print("Bem Vindo ao jogo da Forca")

    arquivo=open("palavras.txt","r")
    palavras=[]
    for linha in arquivo:
        linha= linha.strip()
        palavras.append(linha)
    arquivo.close()
    num=random.randrange(0,len(palavras))
    secrect_word=palavras[num].upper()

    letras_acertadas = ["_" for letra in secrect_word]
    print(letras_acertadas)
    hit= False
    hanged= False
    erro=0
    while(not hanged and not hit):
        chute = input("Digite uma letra")
        chute = chute.strip( ).upper()
        index=0
        if(chute in secrect_word):
            for letra in secrect_word:
                if(chute == letra):
                    letras_acertadas[index]=letra
                index += 1  # ele tem que estar aqui, pois a cada for eu vejo a posição verificada
        else:
            erro+=1
            tentativas=6 - erro
            print("Restam {} tentativas".format(tentativas))
        print(letras_acertadas)
        hanged= erro==6
        if ("_" not in letras_acertadas):
            hit=True
            break
        #hit= "_" not in letras_acertadas
        letras_faltando=str(letras_acertadas.count("_"))
        print('Ainda faltam acertar {} letras'.format(letras_faltando))
        print("Jogando....")
    if(hit):
        print("Parabens!Acertou")
    else:
        print("Você perdeu!")
if(__name__ == "__main__"):
    jogar()