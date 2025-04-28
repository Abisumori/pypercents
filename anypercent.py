def percent(number,perc):
    try:
        if perc > 100 or perc <= 0:
            return 'Процент указан неверно!'
        result = number / 100 * perc
        return result
    except:
        return 'Произошла ошибка, проверьте правильность введённых данных'

def nopercent(number,perc):
    if perc > 100 or perc <= 0:
        return 'Процент указан неверно!'
    result = number * (1 - perc/100)
    return result
