def get_num_words(text):
    list_of_words = text.split()
    return len(list_of_words)

def get_num_char(text):
    char_dict = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict