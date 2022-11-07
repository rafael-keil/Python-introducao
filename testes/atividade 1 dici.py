def main():

    texto = "Caros amigos, a execução dos pontos do programa aponta para a melhoria dos modos de operação convencionais. A certificação de metodologias que nos auxiliam a lidar com o fenômeno da Internet acarreta um processo de reformulação e modernização de alternativas às soluções ortodoxas. Do mesmo modo, a hegemonia do ambiente político auxilia a preparação e a composição dos níveis de motivação departamental. A prática cotidiana prova que a revolução dos costumes não pode mais se dissociar das regras de conduta normativas."

    dic = {}

    for i in texto:

        if i in dic:

            dic[i] = dic[i] + 1

        else:

            dic[i] = 1

    for i in dic:

        print(i + "--> " + str(dic[i]))


if __name__ == "__main__":

    main()
