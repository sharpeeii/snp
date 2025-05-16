class NoSuchStrategyError(Exception):
    def __init__(self, name, strat):
        super().__init__(f"Invalid strat ('{strat}') by {name} \n Strats in RPS game: 'R', 'P', 'S' -_- ")

class WrongNumberOfPlayersError(Exception):
    def __init__(self, given_amnt):
        super().__init__(f"Invalid amount of players: {given_amnt} given, but only 2 allowed")

class InvalidFormat(Exception):
    def __init__(self):
        super().__init__("Please, pass the correct matrix")

def amount_is_valid(amount):
    return amount == 1 or amount == 2

def strat_is_valid(strat):
    return strat.upper() in "RPS" 

def get_winner_index(comb):
    return 1 if comb in ["RP", "SR", "PS"] else 0 

def rps_game_winner(table: list):
    if not isinstance(table, list):
        raise InvalidFormat()
    
    amount = len(table)
    if not amount_is_valid(amount):
        raise WrongNumberOfPlayersError(amount)

    for player in table:
        if not isinstance(player, list) or len(player) != 2:
            raise InvalidFormat()
        if not isinstance(player[1], str) or not strat_is_valid(player[1]):
            raise NoSuchStrategyError(player[0], player[1])

    if amount == 1:
        return f"{table[0][0]} {table[0][1]}"
    #если вдруг решили сойти с ума

    comb = (table[0][1] + table[1][1]).upper() #извлекаем полученную комбинацию

    winner_index = get_winner_index(comb)
    winner = table[winner_index]
    return f"{winner[0]} {winner[1]}"

