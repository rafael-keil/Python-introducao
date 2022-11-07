def chapeuSeletor(nome):
    for i in nome:
        if(i == "g"):
            return("Grifinória")
        elif(i == "s"):
            return("Soncerina")
        elif(i == "c"):
            return("Corvinal")
        elif(i == "l"):
            return("Lufa-Lufa")

    return("Grifinória")


def main():
    n = input("Digite seu nome: ")
    print("A casa escolhida foi: " + chapeuSeletor(n))


if __name__ == "__main__":
    main()
