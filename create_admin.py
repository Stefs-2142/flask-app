from getpass import getpass
import sys

from webapp import create_app
from webapp.user.models import User
from webapp.db import db


app = create_app()

with app.app_context():
    user_name = input('Введите имя пользователя:')

    if User.query.filter(User.user_name == user_name).count():
        print('Пользователь с таким имемнем уже сущуествует.')
        sys.exit(0)

    password_1 = getpass('Введите пароль:')
    password_2 = getpass('Повторите пароль:')

    if not password_1 == password_2:
        print('Пароли не совпадают.')
        sys.exit(0)

    new_user = User(user_name=user_name, role='admin')
    new_user.set_password(password_1)

    db.session.add(new_user)
    db.session.commit()
    print(f'Пользователь "{user_name}" c правами " admin" создан.')
