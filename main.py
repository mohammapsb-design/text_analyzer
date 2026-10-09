from analyzer import count_words,find_how_many_times,most_common_word,longest_word
from file_manager import read_file
def check_empty_file(current_file):
    if current_file == None :
     current_file = input("You haven't set current file yet! , please enter it's name : ")
    return current_file
current_file = None
while True:
    menu = f'''
===================================================================================
                  Current file : {current_file}
1.Change current file 
2.Count total words
3.Find how many times a word has been repeated
4.Find the most repeated word
5.Find the longest word
6.Exit
'''
    print(menu)
    try :
       choice = int(input("your choice : "))
    except :
       print("Please enter a valid choice....")
       pass
    if choice == 1 :
          current_file = input("Enter file name : ")
    if choice == 2 :
          current_file = check_empty_file(current_file)
          text = read_file(current_file)
          print(f"Number of total words is {count_words(text)}")
    if choice == 3 :
          current_file = check_empty_file(current_file)
          word = input("Enter the word : ")
          text = read_file(current_file)
          num = find_how_many_times(text,word)
          print(f"{word} is repeated {num} times.")
    if choice == 4 :
          current_file = check_empty_file(current_file)    
          text = read_file(current_file)
          word , num = most_common_word(text)
          print(f"{word} is the most used word, which is repeated {num} times")
    if choice == 5 :
          current_file = check_empty_file(current_file)    
          text = read_file(current_file)
          word = longest_word(text)
          length = len(word)
          print(f"the longest word is [{word}] which has {length} characters.")
    if choice == 6 :
        print("Thanks for trying me , Bye :) ")       
        break