"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def user_data(name, surname, year_of_birth, city, email, phone):
    return print(f'{name} {surname} '
                 f'{year_of_birth} года рождения, '
                 f'проживает в городе {city}, '
                 f'email: {email}, телефон: {phone}')
user_data(
    name=input('Имя: '),
    surname=input('Фамилия: '),
    year_of_birth=input('Год рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: '),
)