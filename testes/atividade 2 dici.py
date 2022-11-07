def main():

    texto1 = "Caros amigos, a execução dos pontos do programa aponta para a melhoria dos modos de operação convencionais. A certificação de metodologias que nos auxiliam a lidar com o fenômeno da Internet acarreta um processo de reformulação e modernização de alternativas às soluções ortodoxas. Do mesmo modo, a hegemonia do ambiente político auxilia a preparação e a composição dos níveis de motivação departamental. A prática cotidiana prova que a revolução dos costumes não pode mais se dissociar das regras de conduta normativas."
    texto2 = "amigos steam aponta hots"

    pTxt1 = texto1.replace(",", "").replace(".","").split(" ")
    pTxt2 = texto2.replace(",", "").replace(".","").split(" ")
    
    dic = {}

    for i in pTxt1: 
        if i not in dic:
            dic[i] = 1
            

    for i in pTxt2:
        if i in dic:    
            dic[i] = dic[i] + 1
            
    for i in dic:
        if dic[i] == 2:
            print(i + " -- repetida")
            

if __name__ == "__main__":

    main()