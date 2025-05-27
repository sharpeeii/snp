def format_string(string):
    result = ''.join(ch.lower() for ch in string if ch.isalnum())
    return result

def is_palindrome(string):
    if string is None:
        return False
    formatted = format_string(str(string))
    return formatted == formatted[::-1]

print(is_palindrome(None))
