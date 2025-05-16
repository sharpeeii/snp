class NoSuchStrategyError(Exception):
    def __init__(self):
        super().__init__("Allowed strats in RPS game: 'R', 'P', 'S'  -_- ")

class WrongNumberOfPlayersError(Exception):
    def __init__(self, given_amnt):
        super().__init__(f"Invalid amount of players: {given_amnt} given, but only 2 allowed")

class InvalidFormat(Exception):
    def __init__(self):
        super().__init__("Please, pass the correct matrix")

def amount_is_valid(amount):
    return amount == 1 or amount == 2

def comb_is_valid(comb):
    return comb in ["PR", "RS", "SP", "RP", "SR", "PS", "PP", "SS", "RR"]

def get_winner(comb):
    return comb in ["RP", "SR", "PS"]

def rps_game_winner(table: list):
    if not isinstance(table, list):
        raise InvalidFormat()
    
    amount = len(table)
    if not amount_is_valid(amount):
        raise WrongNumberOfPlayersError(amount)

    for player in table:
        if not isinstance(player, list) or len(player) != 2:
            raise InvalidFormat()

    if amount == 1:
        return f"{table[0][0]} {table[0][1]}"

    comb = table[0][1] + table[1][1] #извлекаем полученную комбинацию
    if not comb_is_valid(comb):
        raise NoSuchStrategyError()

    winner_index = get_winner(comb)
    winner = table[winner_index]
    return f"{winner[0]} {winner[1]}"

