from stats import get_num_words, get_num_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()      
    return file_contents

def main():
    text = get_book_text('./books/frankenstein.txt')
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    char_dic = get_num_char(text)
    print(char_dic)
main()