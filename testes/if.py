x = input("digite um número inteiro: ")

if(int(x) < 10):
    print("1 digito")
elif(int(x) < 99):
    print("2 digitos")
elif(int(x) < 999):
    print("3 digitos")
else:
    print("4 ou mais digitos")    