from datetime import datetime, timedelta

def date_in_future(integer):

    if isinstance(integer, int):
        required_date = datetime.now() + timedelta(days=integer)
    else:
        required_date = datetime.now()
     
    formatted_date = required_date.strftime("%d-%m-%Y %H:%M:%S")
    return formatted_date
