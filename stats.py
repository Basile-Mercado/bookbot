def sort_on(items):
    for i in items:
        return items[i]

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

def sort_char_dict(char_dict):
    list_of_dict = []
    for c in char_dict:
        if c.isalpha():
            list_of_dict.append({c: char_dict[c]})   
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict     