
from stats import get_num_words, get_char_count, book_report
import sys

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_content = f.read()
    
    return file_content
    
    
def main():
    FILEPATH:str = 'books/frankenstein.txt'
    word_num = get_num_words(get_book_text(FILEPATH))
    char_counter:dict = get_char_count(get_book_text(FILEPATH))
    book_report(char_counter,word_num,FILEPATH)
    

main()
