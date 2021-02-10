def menu_top():
    print('-' * 30)
    print(('-' * 13) + 'Menu' + ('-' * 13))
    print('1. Create new user')
    print('2. Use an existing user')
    print('Q. Exit this program')
    print('-' * 30)
    menu_top_answer = int(input(': '))
    return menu_top_answer
