def combine_anagrams(words_array):
    anagram_dict = {}
    for word in words_array:
        key = ''.join(sorted(word.lower()))
        if not key in anagram_dict:
            anagram_dict[key] = []
        anagram_dict[key].append(word)
    return list(anagram_dict.values())

