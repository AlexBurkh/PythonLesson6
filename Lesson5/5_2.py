# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
#   Играют два игрока делая ход друг после друга. 
#   Первый ход определяется жеребьёвкой. 
#   За один ход можно забрать не более чем 28 конфет. 
#   Все конфеты оппонента достаются сделавшему последний ход. 
#   Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


candies = 2021
first_player_candies = 0
second_player_candies = 0
turn_counter = 0

def take_candies(player_name):
    global turn_counter
    global candies
    while True:
        print(f"Ход игрока '{player_name}'. Осталось {candies} конфет")
        if candies > 28:
            num = input("Возьмите количество конфет от 0 до 28: ")
        else:
            num = input(f"Возьмите количество конфет от 0 до {candies}: ")
        num = int(num)
        if 0 <= num <= 28 and num <= candies:
            turn_counter += 1
            candies -= num
            return num
        else:
            continue

def bot_turn():
    global turn_counter
    global candies

    num = 0
    if candies > 56:
        num = randint(0, 28)
    else:
        if candies > 28:
            num = randint(0, candies - 29)
        else:
            num = candies
    candies -= num
    print(f"Ход игрока 'Bot'. Взял {num} конфет")
    turn_counter += 1
    
    return num

def run_with_human():
    global turn_counter
    global first_player_candies
    global second_player_candies

    turn_counter = randint(1, 2)
    while candies > 0:
        player_name = ""
        if not turn_counter % 2:
            player_name = "First"
            first_player_candies += take_candies(player_name)
        else:
            player_name = "Second"
            second_player_candies += take_candies(player_name)

    print(f"'{player_name}' wins! He won {first_player_candies + second_player_candies}")
    

def run_with_bot():
    global turn_counter
    global first_player_candies
    global second_player_candies

    turn_counter = randint(1, 2)
    while candies > 0:
        winner_name = ""
        if not turn_counter % 2:
            winner_name = "Player"
            first_player_candies += take_candies("Player")
        else:
            winner_name = "Bot"
            second_player_candies += bot_turn()
    print(f"'{winner_name}' wins! He won {first_player_candies + second_player_candies}")


#run_with_human()
run_with_bot()
    

