import csv


def main():
    arqcsv = open(
        'C:/Users/rafak/OneDrive - Universidade Feevale/Feevale/Ciencias da computacao Sem3/Topicos 1/EAD/praniia.csv', 'r')
    csv_handle = csv.reader(arqcsv, delimiter=';')
    for i in csv_handle:
        print(i)
    arqcsv.close()


if __name__ == "__main__":
    main()
