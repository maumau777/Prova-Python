'''
Questão 2: Implementar uma Calculadora com Loop
Escreva uma função chamada calculadora que recebe três argumentos: dois números (a e b) e uma string representando a operação (operacao). 
A função deve retornar o resultado da operação aplicada aos dois números. As operações suportadas são:

    + para adição
    - para subtração
    * para multiplicação
    / para divisão

A função deve lidar com a divisão por zero e retornar uma mensagem apropriada nesse caso.

Segue um trecho mostrando como deve ser implementada a função:
    def calculadora(a, b, operacao):
        if operacao == '+':
            return a + b


Na entrada dos números deve ser feito o tratamento de exceções, para que seja tratado os casos que não sejam digitados números.

O programa deve ficar em loop, solicitando ao usuário os valores e a operação até que o usuário digite s para sair.

Os números digitados devem ser armazenados em uma lista e depois de encerrar, mostrar a lista, o maior número, o menor número e a média dos números.

'''

def calculadora(a, b, operacao):
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        return a / b
    else:
        return 'Operação inválida'

lista = []

while True:
    try:
        a = float(input('Digite o primeiro número: '))
        b = float(input('Digite o segundo número: '))
        print('''Digite a operação, sendo:
            + para adição
            - para subtração
            * para multiplicação
            / para divisão''')
        operacao = input('Digite a operação: ')
        resultado = calculadora(a, b, operacao)
        lista.append(resultado)
        print(f'Resultado: {resultado}')
    except ValueError:
        print('Digite um número válido')
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
    except:
        print('Operação inválida')
    finally:
        opcao = input('Quer continuar? Digite y para continuar e s para sair: ')
        if opcao == 's':
            break

print(f'Lista: {lista}')

print(f'Maior número: {max(lista)}')

print(f'Menor número: {min(lista)}')

print(f'Média dos números: {sum(lista) / len(lista)}')
