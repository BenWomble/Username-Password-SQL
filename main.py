from SQL import sql_database_connect
from Menu import menu_list
from Menu import menu_exist


#  SQL Database Connection Properties

SQL_CONNECT = sql_database_connect.sql_connect_local()
mycursor = SQL_CONNECT.cursor()

#  SQL Database INSERT

#  SQL_FORMULA_INSERT = f"INSERT INTO users (name) VALUES ('')"
#  mycursor.execute(SQL_FORMULA_INSERT, )
#  SQL_CONNECT.commit()

#  SQL Database SELECT

#  SQL_FORMULA_FIND = f"SELECT name FROM users WHERE name=''"
#  mycursor.execute(SQL_FORMULA_FIND)
#  myresult = mycursor.fetchall()

#  menu_list.menu_top()


def create_user():
    print()
    print('-' * 30)
    print(('-' * 8) + 'Create New User' + ('-' * 7))
    print('-' * 30)
    print()
    print('-' * 30)
    print('Please input your new username.')
    print('-' * 30)
    created_user = input(':  ')
    return created_user


def find_user():
    fetch = menu_exist.menu_find_user()
    return fetch


execute_main_menu = menu_list.menu_top()
while True:
    if execute_main_menu == '1':
        print(create_user())
        break
    if execute_main_menu == '2':
        print(find_user())
        break
    if execute_main_menu in ['q', 'Q']:
        execute_main_menu = 'Q'
        print()
        print('-' * 30)
        print("Do you want to quit? (y/n)")
        print('-' * 30)
        quit_choice = input(":  ")
        if quit_choice in ["y", "Y"]:
            print()
            print('-' * 30)
            print('Goodbye. Have A Nice Day!')
            print('-' * 30)
            break
        elif quit_choice in ["n", "N"]:
            print()
            print('-' * 30)
            print('Returning to Main Menu')
            print('-' * 30)
            print()
            menu_list.menu_top()
            break
        break
