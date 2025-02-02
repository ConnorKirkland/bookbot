def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    char_list = convert_to_list(char_count)
    char_list.sort(reverse=True, key=sort_on)
    for dict in char_list:
        print(f"The '{dict["char"]}' character was found {dict["count"]} times")
    # print(f"{num_words} words found in the document")
    # print(char_count)

def convert_to_list(dict):
    new_list = []
    for c in dict:
        if c.isalpha():
            new_list.append({"char":c,"count":dict[c]})
    return new_list
    

def sort_on(dict):
    return dict["count"]

def get_char_count(text):
    countDict = {}
    for c in text:
        lower_c = c.lower()
        if lower_c in countDict:

            countDict[lower_c] += 1
        else:
            countDict[lower_c] = 1
    return countDict

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
