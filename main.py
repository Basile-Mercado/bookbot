from stats import get_num_words, get_num_char, sort_char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()      
    return file_contents

def get_report():
    print("""============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...""")
    text = get_book_text('./books/frankenstein.txt')
    num_words = get_num_words(text)
    print(f"""----------- Word Count ----------\nFound {num_words} total words""")
    char_dict = get_num_char(text)
    sorted_list = sort_char_dict(char_dict)
    for sorted in sorted_list:
        for s in sorted:
            print(f"{s}: {sorted[s]}")
    
def main():
    get_report()
    
main()