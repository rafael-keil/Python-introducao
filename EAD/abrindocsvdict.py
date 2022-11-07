import csv


def main():
    arqcsv = open(
        'praniia.csv', 'r')
    csv_handle = csv.DictReader(arqcsv, delimiter=';')

    for i in csv_handle:
        print(i)
    arqcsv.close()


if __name__ == "__main__":
    main()
