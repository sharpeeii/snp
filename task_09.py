def get_value(pair: tuple):
    return pair[1]

def connect_dicts(dict1: dict, dict2: dict): 
    if sum(dict1.values()) > sum(dict2.values()):
        priority, secondary = dict1, dict2
    else:
        priority, secondary = dict2, dict1 
    
    priority = {key: value for key, value in priority.items() if value >= 10} 

    for key, value in secondary.items():
        if key not in priority and value >= 10:
            priority[key] = value 

    sorted_items = sorted(priority.items(), key=get_value) #я хейтер лямбд
    return dict(sorted_items)

