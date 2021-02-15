def menu_exist_user():
    print('-' * 30)
    print(('-' * 13) + 'Menu' + ('-' * 13))
    print('1. Use default account: "Player"')
    print('2. Input existing username')
    print('Q. Exit this program')
    print('-' * 30)
    exist_user = int(input(': '))
    return exist_user


def menu_find_user():
    print()
    return "Finding User"


def default_user():
    player_name = "Player"
    return player_name
