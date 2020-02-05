def person_info(name, surname, year, city, email, phone):
    print(f'{name} {surname}, {year} год(а) рождения, г. {city}, {email}, тел. {phone}')

person_info(name=input('Name: '), surname=input('Surname: '), year=input('Year: '), city=input('City: '), email=input('Email: '), phone=input('Phone: '))