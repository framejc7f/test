from password_generator import PasswordGenerator
import randomtimestamp
import datetime



def getPassword():
    """Generate random password"""
    password = PasswordGenerator()
    password.minlen = 8
    password.maxlen = 10
    return password.generate()


def getDate():
    """Random date 1950.1.1 — 2008-1-1""" 
    max =  datetime.date(2008, 1, 1)
    date = randomtimestamp.random_date(end=max)
    
    year = date.year
    month = date.month
    day = date.day
    monthList = {1: "Январь", 2 : "Февраль", 3: "Март", 4 : "Апрель", 5: "Май", 6 : "Июнь", 7: "Июль", 8 : "Август", 9: "Сентябрь", 10 : "Октябрь", 11: "Ноябрь", 12 : "Декабрь",}

    # print(f'{year=}\n{month=}({monthList[month]})\n{day=}')
    return (monthList[month], day, year)
