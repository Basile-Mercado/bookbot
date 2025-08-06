def get_num_words(text):
    list_of_words = text.split()
    count = 0
    for i in range(0, len(list_of_words)):
        count += 1
    return count