def format_string(string:str):
    result = ''.join(ch.lower() for ch in string if ch.isalnum())
    return result

def is_palindrome(string: str):
    formatted = format_string(string)
    left = 0
    right = len(formatted)-1
    while left < right:
        if formatted[left]  != formatted[right]:
            return False
        left += 1
        right -= 1
    return True

while True:
    print(is_palindrome(input()))
