
from stats import get_num_words, get_char_count
def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_content = f.read()
    
    return file_content
    
    
def main():
    FILEPATH:str = "./books/frankenstein.txt"
    print(get_num_words(get_book_text(FILEPATH)))
    print(get_char_count(get_book_text(FILEPATH)))
    

main()
