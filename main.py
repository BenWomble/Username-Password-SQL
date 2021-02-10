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

SQL_FORMULA_FIND = f"SELECT name FROM users WHERE name=''"
#  mycursor.execute(SQL_FORMULA_FIND)
#  myresult = mycursor.fetchall()

#  menu_list.menu_top()


EXECUTE_MAIN_MENU = menu_list.menu_top()
EXECUTE_USER_SEARCH = menu_exist.menu_exist_user()


def main_menu():
    while EXECUTE_MAIN_MENU != 'Q':
        if EXECUTE_MAIN_MENU == int(1):
            create_user()
        if EXECUTE_MAIN_MENU == int(2):
            find_user()


def create_user():
    print('-' * 30)
    print(('-' * 6) + 'Create New User' + ('-' * 5))
    print()
    print('Please input your new username.')
    print('-' * 30)
    print('-' * 30)
    created_user = input(': ')
    return created_user


def find_user():
    menu_exist.menu_exist_user()
    while EXECUTE_USER_SEARCH != 'Q':
        if EXECUTE_USER_SEARCH == '1':
            default_user()
        elif EXECUTE_USER_SEARCH == '2':
            global SQL_FORMULA_FIND
            mycursor.execute(SQL_FORMULA_FIND)
            myresult = mycursor.fetchall()
            for result in myresult:
                print(result)


find_user()
