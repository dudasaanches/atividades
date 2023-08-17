import calculadora
es = int(input("Escolha a função:\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\nR:"))
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if es == 1:
    a = calculadora.soma(num1, num2)
    print(f"A soma é: {a}")
elif es == 2:
    s = calculadora.subtracao(num1, num2)
    print(f"A subtração é: {s}")
elif es == 3:
    m = calculadora.multiplicacao(num1, num2)
    print(f"A multiplicação é: {m}")
elif es == 4:
    d = calculadora.divisao(num1, num2)
    print(f"A divisão é: {d}")
else:
    print("ERRO")