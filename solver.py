guess = ""
result = ""
words = []


with open('datasets/answers.txt') as f:
    for line in f:
        words.append(line.strip())

        
print("Enter a starter word")

for guesses in range(6):
    guess = input("Word: ").lower()
    
    if guess in words:
        print("\n\nWhat Result Did Wordle Give You?")
        print("$ = Green, * = Yellow, # = Grey")
        result = input("Results: ")
        
        # if solved
        if result == "$$$$$":
            print("\n\nMission Acomplished: Wordle in", guesses+1)
            break
        
        words_tuple = tuple(words)
        for word in words_tuple:
            for i in range(5):
                
                #remove from list if word has grey letter
                if result[i] == "#" and guess[i] in word:
                    words.remove(word)
                    break
                
                # remove from list if word goes not have green letter in correct place
                elif result[i] == "$" and guess[i] != word[i]:
                    words.remove(word)
                    break
                    
                # remove from list if word does not have yellow letter
                elif result[i] == "*" and guess[i] not in word:
                    words.remove(word)
                    break
                    
                # remove from list if word has yellow letter in same place
                elif result[i] == "*" and guess[i] == word[i]:
                    words.remove(word)
                    break
                    
        print("\nThese are a list of possible answers, use your judgement to select one.\n")
        print(words)
                
    else:
        print("Error: Word not in dataset")
        break