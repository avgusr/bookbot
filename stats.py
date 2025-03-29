def get_num_words(file_content:str) -> int:
    num_words = len(file_content.split())
    return num_words



def get_char_count(file_content:str) -> dict:

    char_counter:dict[str:int] = {}

    for char in file_content.lower():
        if char not in char_counter:
            char_counter[char] = 1
        else:
            char_counter[char] += 1
    
    return char_counter


def book_report(char_counter:dict, word_count:int, file:str) -> str:
    char_count:list[dict] = []
    for key, value in char_counter.items():
        if key.isalpha():
            char_count.append({"char":key,"count":value})
    
    def sort_on(dic:dict) -> int:
        return dic["count"]
    

    char_count.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for e in char_count:
        print(f"{e['char']}: {e['count']}")
    print("============= END ===============")
