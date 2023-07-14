def calculadora(num1, num2, operacao):
    # Função que realiza as operações da calculadora
    # Recebe como parâmetros num1 e num2 (os números da operação) e operacao (o código da operação desejada)

    if operacao == 1:
        resultado = num1 + num2  # Realiza a soma dos números
    elif operacao == 2:
        resultado = num1 - num2  # Realiza a subtração dos números
    elif operacao == 3:
        resultado = num1 * num2  # Realiza a multiplicação dos números
    elif operacao == 4:
        if num2 != 0:
            resultado = num1 / num2  # Realiza a divisão dos números (verifica se o divisor é diferente de zero)
        else:
            return "Erro: Divisão por zero não é possível"  # Retorna uma mensagem de erro caso haja divisão por zero
    else:
        return "Erro: Operação inválida"  # Retorna uma mensagem de erro caso a operação seja inválida

    return resultado  # Retorna o resultado da operação

num1 = float(input("Digite o primeiro número: "))  # Obtém o primeiro número do usuário
num2 = float(input("Digite o segundo número: "))  # Obtém o segundo número do usuário
operacao = int(input("Digite a operação desejada:\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n"))  # Obtém o código da operação desejada

resultado = calculadora(num1, num2, operacao)  # Chama a função calculadora passando os valores obtidos como parâmetros
print("Resultado:", resultado)  # Imprime o resultado na tela