import string



def count_letters(file_contents):
    alphabet = string.ascii_lowercase
    alphabet_dict = {}
    # alphabet_dict[" "] = 0
    for letter in alphabet:
        alphabet_dict[letter] = 0

    words = file_contents.lower()

    for char in words:
        if alphabet_dict.get(char) != None:
            alphabet_dict[char] += 1

    return alphabet_dict

def value_getter(item):
    return item[1]

def report(len_words,alphabet_dict):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{len_words} words found in the document')
    print('')
    sorted_dict = dict(sorted(alphabet_dict.items(),key=value_getter,reverse=True))
    for item in sorted_dict:
        # print(item)
        value = sorted_dict[item]
        print(f"The '{item}' character was found {value} times")
    print('--- End report ---')

def count_words(file_contents):

    words = file_contents.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    len_words = count_words(file_contents)
    alphabet_dict = count_letters(file_contents)
    report(len_words,alphabet_dict)
    # print(len_words)
    # print(alphabet_dict)

if __name__ == "__main__":
    main()