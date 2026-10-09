
def count_words(str):
    words = str.split() 
    return len(words)
def find_how_many_times(str,word):
    words = str.split()
    return words.count(word)
    # if num < 2 :
    #   print(f"{word} appears {num} time")
    # else:
    #   print(f"{word} appears {num} times")

def most_common_word(str):
    words = str.split()
    dictionary = {}
    for i in words:
        if not i in dictionary:
          dictionary[i] = 1
        else :
          dictionary[i] += 1
    # or return max(dictionary,key = dictionary.get)
    temp_max_value = 0
    max_word = None
    for key in dictionary:
        value = dictionary[key]
        if value > temp_max_value :
            temp_max_value = value 
            max_word = key 
    return max_word,temp_max_value

def longest_word(str):
    words = str.split()
    return max(words, key=len)
     
    



