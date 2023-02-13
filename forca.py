

def jogar():
    print("Bem Vindo ao jogo da Forca")
    secrect_word = "banana"
    hit= False
    hanged= False
    while(not hanged and not hit):
        index = 0
        chute = input("Digite uma letra")
        chute = chute.strip( )
        for letra in secrect_word:
            index = index + 1 #ele tem que estar aqui, pois a cada for eu vejo a posição verificada
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(chute, index))


    print("Jogando....")


if(__name__=="__main__"):
    jogar()