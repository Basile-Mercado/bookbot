def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()      
    return file_contents

def get_number_of_words(text):
    list_of_words = text.split()
    count = 0
    for i in range(0, len(list_of_words)):
        count += 1
    return count

def main():
    text = get_book_text('./books/frankenstein.txt')
    num_words = get_number_of_words(text)
    print(f"{num_words} words found in the document")
main()