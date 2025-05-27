def str_multiply(string: str):
    ans = 1
    flag = False
    for ch in string:
        if ch == "0":
            return 0
        if ch.isdigit():
            ans = ans * int(ch)
            flag = True
    return ans if flag else None

def multiply_numbers(inputs = None):
    if inputs is None:
        return None
    if isinstance(inputs, (int, float, complex)):
        return str_multiply(str(inputs))
    if isinstance(inputs, str):
        return str_multiply(inputs)
    if isinstance(inputs, (list,tuple,set)):
        ans = 1
        flag = False
        for i in inputs:
            digit = multiply_numbers(i)
            if digit == 0:
                return 0
            elif digit is not None:
                ans = ans * digit
                flag = True
        return ans if flag else None
    if isinstance(inputs, dict):
        ans = 1
        flag = False
        for key, value in inputs.items():
            for i in (value,key):
                digit = multiply_numbers(i)
                if digit == 0:
                    return 0
                elif digit is not None:
                    ans = ans * digit
                    flag = True
        return ans if flag else None

