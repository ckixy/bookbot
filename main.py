def main():    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_book_words(text)
    char_count = characters(text)
    dic_list = sort_dic(char_count)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for k in dic_list:
        print(f"The '{k["char"]}' character was found {k["count"]} times")

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_book_words(text):
        words = len(text.split())
        return words

def characters(text):
    char = {}
    text_lower = text.lower()
    for c in text_lower:
        if c.isalpha():
            if c in char:
                char[c] += 1
            else:
                char[c] = 1    
    return char
def sort_on(dic):
    return dic["count"]

def sort_dic(char_count):
    dic_list = []
    for k in char_count:
        dic_list.append({"char":k,"count":char_count[k]})
    dic_list.sort(key=sort_on, reverse=True)
    return dic_list

main()