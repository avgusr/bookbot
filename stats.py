def get_num_words(file_content:str) -> int:
    num_words = len(file_content.split())
    return f"{num_words} words found in the document"



def get_char_count(file_content:str) -> dict:

    char_counter:dict[str:int] = {}

    for char in file_content.lower():
        if char not in char_counter:
            char_counter[char] = 1
        else:
            char_counter[char] += 1
    
    return char_counter
