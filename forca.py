import random
def jogar():
    imprime_apresentacao()
    secrect_word = inicializa_arquivo()
    letras_acertadas = inicializa_secrect_word(secrect_word)
    print(letras_acertadas)
    hit= False
    hanged= False
    erro=0
    while(not hanged and not hit):
        chute= pede_chute()
        if(chute in secrect_word):
            marca_letras_acertadas(letras_acertadas, chute, secrect_word)
        else:
            erro+=1
            desenha_forca(erro)
            tentativas=6 - erro
            print("Restam {} tentativas".format(tentativas))
        print(letras_acertadas)
        hanged= erro==7
        if ("_" not in letras_acertadas):
            hit=True
            break
        #hit= "_" not in letras_acertadas
        letras_faltando=str(letras_acertadas.count("_"))
        print('Ainda faltam acertar {} letras'.format(letras_faltando))
        print("Jogando....")
    if(hit):
        imprime_parabens()
    else:
        imprime_derrota(secrect_word)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
def imprime_parabens():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def imprime_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def marca_letras_acertadas(letras_acertadas, chute, secrect_word):
    index=0
    for letra in secrect_word:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1  # ele tem que estar aqui, pois a cada for eu vejo a posição verificada

def pede_chute():
    chute = input("Digite uma letra")
    chute = chute.strip().upper()
    return chute

def imprime_apresentacao():
    print("**************************")
    print("Bem Vindo ao jogo da Forca")
    print("**************************")
def inicializa_arquivo():
    arquivo=open("palavras.txt","r") #a variavel arquivo fica definida só aqui dentro, não é global
    palavras=[]
    for linha in arquivo:
        linha= linha.strip()
        palavras.append(linha)
    arquivo.close()
    num=random.randrange(0,len(palavras))
    secrect_word=palavras[num].upper()
    return secrect_word
def inicializa_secrect_word(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()