from datetime import datetime, timedelta

def date_in_future(integer):

    if isinstance(integer, int):
        required_date = datetime.now() + timedelta(days=integer)
        formatted_date = required_date.strftime("%d-%m-%Y %H:%M:%S")
        print(formatted_date)
    else:
        current_date = datetime.now()
        print(current_date)

date_in_future(365)

#в условии написано то вернуть дату, то вывести дату
#в примере метод вызван без print, так что решил именно выводить дату, вотт
