class Calculadora:
    """
    Esta classe oferece dois métodos estáticos para cálculos matemáticos simples:
        - Fatorial de um número.
        - Sequência de Fibonacci.
    """

    @staticmethod
    def Fibonacci(numero: float) -> float:
        pass

    @staticmethod
    def Fatorial(numero: float) -> float:
        pass



def main():
    while True:
        print("#############################################")
        print("Operações Disponíveis: (Fatorial) (Fibonacci)")
        opcao = input("Digite 1 para Fatorial:\tDigite 2 para Fibonacci\tDigite 3 para sair\nOpção: ")

        if opcao == '3':
            print("Finalizando...\n")
            break

        if opcao not in '12':
            print("Opção inválida. Digite apenas 1, 2 ou 3.")
            continue

        try:
            numero_str = input("Digite o número: ")
            numero = float(numero_str)
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")
            continue



        if opcao == '1':
            result = Calculadora.Fatorial(numero = numero)
            print(f'Resultado do Fatorial de {numero}: {result}')

        elif opcao == '2':
            result = Calculadora.Fibonacci(numero = numero)
            print(f'Resultado do Fibonacci de {numero}: {result}')

        print("#############################################")


main()