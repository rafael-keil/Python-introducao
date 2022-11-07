import csv

def main():
    arqcsv = open( 'C:/Users/rafak/OneDrive - Universidade Feevale/Feevale/Ciencias da computacao Sem3/Topicos 1/EAD/times.csv', 'w')
    campos = ['Time','cor 1','cor 2', 'cor 3']
    arquivo = csv.DictWriter(arqcsv, fieldnames=campos, delimiter=';',quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    arquivo.writeheader()
    arquivo.writerow({'Time':'Internacional', 'cor 1':'Vermelho', 'cor 2':'Branco'})
    arquivo.writerow({'Time':'Gremio','cor 1':'Azul','cor 2':'Branco','cor 3':'Preto'})
    arqcsv.close()

if __name__ == "__main__":
    main()
