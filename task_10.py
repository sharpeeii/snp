def count_words(string):
    if string == "":
        return "nonono mister fish"
    counter = dict()
    words_raw = string.lower().split()
    for word in words_raw:
        cleaned_word = ''.join(char for char in word if char.isalpha())
        if cleaned_word:
            if cleaned_word and cleaned_word in counter:
                counter[cleaned_word] += 1
            else:
                counter[cleaned_word] = 1
    return counter

