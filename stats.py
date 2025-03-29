def get_num_words(file_content) -> int:
    num_words = len(file_content.split())
    print(f"{num_words} words found in the document")