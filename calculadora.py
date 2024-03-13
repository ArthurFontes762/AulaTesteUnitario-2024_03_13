def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        raise ValueError("Não é possível dividir por zero!")
    return x / y

def potenciacao(x, y):
    return x ** y

def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")

    escolha = input("Digite a opção (1/2/3/4/5): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = None

    if escolha == '1':
        resultado = adicao(num1, num2)
    elif escolha == '2':
        resultado = subtracao(num1, num2)
    elif escolha == '3':
        resultado = multiplicacao(num1, num2)
    elif escolha == '4':
        resultado = divisao(num1, num2)
    elif escolha == '5':
        resultado = potenciacao(num1, num2)
    else:
        print("Opção inválida!")

    if resultado is not None:
        print("Resultado:", resultado)

if __name__ == "__main__":
    calculadora()
