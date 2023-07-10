import random
import requests
from tkinter import *

#variavel para armazenar a quantidade de linhas existentes no jogo
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#simbolos disponiveis em cada linha
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
#valor de cada simbolo
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#função que verifica quanto o usuario fez por rodada
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winnings_line.append(line + 1)

    return winnings, winnings_line

#função para gerar as letras randomicamente
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

#função para imoprimir as letras aleatorios de forma bonitinha
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# uma função que pode ser convocada dentro do codigo, nesse caso, é uma funçao referente ao deposito que o usuario está realizando na plataforma
def deposit():
    while True:
        # declara a variavel "amount" e pede para o usuario inputar uma informação
        amount = input("What would you like to deposit? $")
        # checa se a info inputada é um digito
        if amount.isdigit():
            #transforma o input em uma variavel inteira e armazena na variavel "amount"
            amount = int(amount)
            #if para checar se o valor é maior que zero
            if amount > 0:
                # se for maior, ele breka e vai para o return
                break
            else:
                #se nao for maior, ele imprime na tela a mensagem solicitando um numero maior que 0
                print ("Amount must be greater than 0.")
        #se o valor inputado nao for um numero, imprime a mensagem solicitando que o usuario insira um numero
        else:
            print("Please enter a number.")
    # retorna o valor inputado se for um numero
    return amount

#funçao para validar o numero de linhas que o usuario quer apostar
def get_number_of_lines ():
    while True:
        #pede para o usuario inputar quantos linhas ele quer apostar, podendo ser entre 1 e 3
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        #verifica se o valor inputado é um digito
        if lines.isdigit():
            #se for, ele converte para uma variavel de numero
            lines = int(lines)
            # if que verifica se o valor inputado está entre os valores possiveis
            if 1 <= lines <= MAX_LINES:
                break
            #se nao estiver, ele pede para o usuario inputar um numero valido de linhas
            else:
                print ("Enter a valid number of lines.")
        #se o valor inputado inicialmente nao é um digito, ele pede para o usuario inputar um numero
        else:
            print("Please enter a number.")
    #retorna o valor de linhas inputado pelo usuario
    return lines


#função que pega o valor que o usuario quer apostar
def get_bet():
    while True:
        #pede para ele informar quanto ele quer apostar em cada linha
        amount = input("What would you like to bet on each line? $")
        #verifica se o valor inputado é um digito
        if amount.isdigit():
            #transforma o valor em um numero
            amount = int(amount)
            #verifica se o valor inputado está entre o valor minimo e maximo aceito
            if MIN_BET <= amount <= MAX_BET:
                #se sim, ele breka e vai para o final
                break
            else:
                #se nao, ele pede para o usuario inserir um numero entre o minimo e maximo
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            #caso o valor inputado no inicio nao seja um digito, ele pede para o usuario inserir um numero
            print("Please enter a number.")
    #retorna o valor apostado
    return amount


def spin(balance):
    # varicial lines que armazena o valor da função get_number_of_lines
    lines = get_number_of_lines()
    # validar
    while True:
        # variavel bet armazena o valor da função get_bet
        bet = get_bet()
        # variavel total_bet realiza a multiplicação entre o valor que o usuario quer apostar e quantidade de linahs que ele quer apostar
        total_bet = bet * lines

        # faz uma validação se os valores inputados respeita os valores que ja estao no sistema
        if total_bet > balance:
            # pede para ele inserir um valor tangivel e ainda mostra qual é o balance dele
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            # se o valor estiver ok, ele breka
            break

    # imprime o quanto eles está apostando e em quantas linhas, mostrando qual o valor total da posta
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet} ")

    # imprime todas as funções
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_line = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winnings_line)
    return winnings - total_bet

#função para armazenar a parte principal do programa
def main():
    #variavel balance armazena o valor da função deposit
    balance = deposit()
    #while para continuar rodando o jogo enquanto o usuario quiser
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    #caso ele saia, mostra com quanto ele ficou no final
    print(f"You left with ${balance}")

main()

