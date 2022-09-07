# Создайте программу для игры в "Крестики-нолики".

from random import randint

turn_counter = 0
playing_field = [str(i) for i in range(9)]
separator = ['---', '-', '---', '-', '---']

def print_playing_field():
    global playing_field
    global separator
    for i in range(3):
        line = [i for i in playing_field[i * 3 : i * 3 + 3]]
        for j in range(len(line)):
            if j == 2 or j == 5 or j == 8:
                print(f" {line[j]} ")
            else:
                print(f" {line[j]} |", end='')
        if i != 2:
            for sep in separator:
                print(sep, end='')
            print()
def check_for_win(symbol):
    global playing_field
    # горизонтали
    if (   playing_field[0] == playing_field[1] == playing_field[2] == symbol
        or playing_field[3] == playing_field[4] == playing_field[5] == symbol
        or playing_field[6] == playing_field[7] == playing_field[8] == symbol):
        return True
    # вертикали
    if (   playing_field[0] == playing_field[3] == playing_field[6] == symbol
        or playing_field[1] == playing_field[4] == playing_field[7] == symbol
        or playing_field[2] == playing_field[5] == playing_field[8] == symbol):
        return True
    # диагонали
    if (   playing_field[0] == playing_field[4] == playing_field[8] == symbol
        or playing_field[2] == playing_field[4] == playing_field[6] == symbol):
        return True
    return False
def player_turn(player_name, symbol):
    global playing_field
    global turn_counter
    print(f"Ход игрока {player_name}")
    while True:
        turn = int(input("Выберите одну из свободных ячеек, отмеченных цифрой: "))
        if 0 <= turn <= 8 and playing_field[turn].isdigit():
            playing_field[turn] = symbol
            turn_counter += 1
            break
def run_with_human():
    global turn_counter
    turn_counter = randint(1, 2)
    while len(list(filter(lambda x: x.isdigit(), playing_field))) > 0:
        player_name = ""
        symbol = ""
        print_playing_field()
        if not turn_counter % 2:
            player_name = "First"
            symbol = "X"
            player_turn(player_name, symbol)
            if check_for_win(symbol):
                print(f"'{player_name}' побеждает!")
                return
        else:
            player_name = "Second"
            symbol = "O"
            player_turn(player_name, symbol)
            if check_for_win(symbol):
                print(f"'{player_name}' побеждает!")
                return
    print("Ничья")

run_with_human()