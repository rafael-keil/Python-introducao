import csv


def encripta(palavra, chave):

    while len(chave) < len(palavra):
        chave = chave + chave

    codificado = ''
    i = 0
    while i < len(palavra):
        valor = ord(palavra[i])+ord(chave[i])
        resto = valor % 25
        novaletra = chr(97+resto)
        codificado += novaletra
        i += 1

    return codificado


def main():
    planilhaArquivo = open('planilha.csv', 'r')
    planilha = csv.DictReader(planilhaArquivo, delimiter=';')

    lgpdArquivo = open('lgpd.csv', 'w', newline='', encoding='utf-8')
    campos = ['Nome do vivente', 'Profissao', 'Idade']
    lgpd = csv.DictWriter(lgpdArquivo, fieldnames=campos,
                          delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    
    lgpd.writeheader()

    for linha in planilha:
        nomeEncriptado = encripta(linha['Nome do vivente'], linha['Profissao'])
        profissaoEncripado = encripta(linha['Profissao'], linha['Nome do vivente'])
        idadeEncriptada = encripta(str(linha['Idade']), 'idade')
        
        lgpd.writerow(
            {'Nome do vivente': nomeEncriptado, 'Profissao': profissaoEncripado, 'Idade': idadeEncriptada})

    planilhaArquivo.close()
    lgpdArquivo.close()


if __name__ == '__main__':
    main()
