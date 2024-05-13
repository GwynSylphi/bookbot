def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = book_word_count(text)
    letter_count = book_letter_count(text)
    alpha_sorted_list = alphabet_count_list_sort(letter_count)

    print(f"--- Report of {book_path} ---")
    print(f"There are {word_count} words found in the document")
    
    for element in alpha_sorted_list:
        print(f"The {element["char"]} character was found {element["num"]} times!")
    
    print("--- End of Report ---")


def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def book_word_count(text):
    words = []
    words = text.split()
    #could just use return len(words) here instead of the for loop
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def book_letter_count(text):
    alphabet_count = {}
    words = []
    words = text.split()
    for word in words:
        word = word.lower()
        for letter in word:
            if letter in alphabet_count:
                alphabet_count[letter] += 1
            elif letter.isalpha():
                alphabet_count[letter] = 1
            else:
                pass
    return alphabet_count

def sort_on(alpha):
    return alpha["num"]

def alphabet_count_list_sort(num_alphas_dict):
    sorted_list = []
    for letter in num_alphas_dict:
        sorted_list.append({"char": letter, "num": num_alphas_dict[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()