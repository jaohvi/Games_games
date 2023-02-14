
def jogar():
    print("Bem Vindo ao jogo da Forca")
    secrect_word = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    print(letras_acertadas)
    hit= False
    hanged= False
    while(not hanged and not hit):
        chute = input("Digite uma letra")
        chute = chute.strip( )
        index=0
        for letra in secrect_word:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index]=letra
            index = index + 1  # ele tem que estar aqui, pois a cada for eu vejo a posição verificada
        print(letras_acertadas)
        letras_faltando=str(letras_acertadas.count("_"))
        print('Ainda faltam acertar {} letras'.format(letras_faltando))
    print("Jogando....")
if(__name__ == "__main__"):
    jogar()