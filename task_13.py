from datetime import datetime
import time

def cached(max_size = None, seconds = None):
    if not isinstance(max_size, int):
        max_size = None                         #по тз обработка типов
    if not isinstance(seconds, int):
        seconds = None
    def decorator(func):
        cache = {}
        def wrapper(*args, **kwargs):              #структура кэша - {tuple:{value:date}}
            try:
                current_key = (args, tuple(sorted(kwargs.items()))) 
            except Exception:                    #делаем ключ только при условии, что тип хэшируется
                try:                             #иначе просто не кэшируем результат
                    return func(*args, **kwargs)
                except Exception:      
                    return None     #если сама функция ляжет

            expired_keys = []
            if seconds is not None:
                for key in cache:
                    time_spent = datetime.now() - cache[key]['date'] 
                    if time_spent.total_seconds() > seconds:  #удаляем просрочку
                        expired_keys.append(key)
            for key in expired_keys:
                del cache[key]

            if current_key in cache:
                result = cache[current_key]['value']
            else:
                if max_size is not None and len(cache) == max_size:
                    first = next(iter(cache))
                    del cache[first]
                try:
                    value = func(*args, **kwargs)
                except Exception:
                    return None
                cache[current_key] = {'value': value, 'date': datetime.now()}
                result = cache[current_key]['value']
            return result 
        return wrapper
    return decorator

