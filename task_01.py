def format_string(string:str):
    result = ''.join(ch.lower() for ch in string if ch.isalnum())
    return result

def is_palindrome(string: str):
    formatted = format_string(string)
    return formatted == formatted[::-1]

