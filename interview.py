

# Functinon to generate a dict from a file
def generate_dictionary(filepath: str) -> dict():
    dict_name = dict()
    with open(filepath, "r") as file:
        dict_file = file.readlines()
    # for each line, strip whitespace, find its size, and
    # where key = length, append word into value list
    for line in dict_file:
        word = line.strip().lower()
        size = len(word)
        if size in dict_name.keys():
            dict_name[size].append(word)
        else:
            dict_name[size] = [word]
    return dict_name

# function to organize letters in a word alphabetically
def sort_letters_in_word(word: str) -> str:
    word = ''.join(sorted(word))
    return word

filepath = input("Please submit dictionary filepath: ")
print("creating working dictionary. . .")

user_dict = generate_dictionary(filepath)

user_word = input("To exit the program, enter \".quit\" \nWord to anagram: ").strip()
while user_word != ".quit":
    ordered_user_word = sort_letters_in_word(user_word).lower()
    print("finding anagrams. . .")

    same_length = user_dict[len(user_word)]
    anagrams = []

    # for each word of the same length in the dict, 
    # if the organized words are equal, and the 
    # dict word != the entered word, add word to the 
    # list of anagrams
    for word in same_length:
        ordered_word = sort_letters_in_word(word)
        if ordered_user_word == ordered_word and user_word != word:
            anagrams.append(word)
            
    print(user_word + " has " + str(len(anagrams)) + " anagrams: ")
    print(anagrams)
    user_word = input("To exit the program, enter \".quit\" \n Next word to anagram: ")