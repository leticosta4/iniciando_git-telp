class Calculadora:
    """
    Esta classe oferece dois métodos estáticos para cálculos matemáticos simples:
        - Fatorial de um número.
        - Sequência de Fibonacci.
    """

    @staticmethod
    def Fibonacci(numero: int) -> list[int] | str:
        if numero < 0:
            raise ValueError("Número deve ser não-negativo.")
        if numero == 0:
            return [0]
        
        if numero == 1:
            return [0, 1]
        
        a, b = 0, 1
        fib_sequence = []

        for _ in range(numero + 1):
            fib_sequence.append(a)
            a, b = b, a + b
        return fib_sequence


    @staticmethod
    def Fatorial(numero: int) -> int | str:
        if numero < 0:
            return "Fatorial não é definido para números negativos."
        elif numero == 0 or numero == 1:
            return 1
        else:
            return numero * Calculadora.Fatorial(numero - 1)



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
            numero = int(numero_str)
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