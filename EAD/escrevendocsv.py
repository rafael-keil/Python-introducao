import csv

def main():
    arqcsv = open( 'C:/Users/rafak/OneDrive - Universidade Feevale/Feevale/Ciencias da computacao Sem3/Topicos 1/EAD/times.csv', 'w')
    arquivo = csv.writer(arqcsv, delimiter=';',quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    arquivo.writerow(['Internacional', 'Vermelho', 'Branco'])
    arquivo.writerow(['Gremio','Azul','Branco','Preto'])
    arquivo.writerow(['Fluminense','Verde','Branco','Grená'])
    arquivo.writerow(['Framengu','Preto apagado','Vermelho carniça'])
    arqcsv.close()

if __name__ == "__main__":
    main()
