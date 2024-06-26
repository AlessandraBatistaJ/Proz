print("Digite um número:")
n1 = int(input())
print("Digite outro número:")
n2 = int(input())
print("Escolha uma operação: Digite 1 para soma, 2 para subtração, 3 para multiplicação, 4 para divisão ou 0 para sair")
operacao = int(input())

if (operacao == 1):
    resultado = n1 + n2
    print("O resultado da soma entre " + str(n1) + " + " + str(n2) + " é = " + str(resultado))
elif (operacao == 2):
    resultado = n1 - n2
    print("O resultado da subtração entre " + str(n1) + " - " + str(n2) + " é = " + str(resultado))
elif (operacao == 3):
    resultado = n1 * n2
    print("O resultado da multiplicação entre " + str(n1) + " * " + str(n2) + " é = " + str(resultado))
elif (operacao == 4):
    resultado = n1 / n2
    print("O resultado da divisão entre " + str(n1) + " / " + str(n2) + " é = " + str(resultado))
elif (operacao == 0):
    print("Você está saindo da calculadora. Até mais!")
else:
    print("Essa opção não existe")

