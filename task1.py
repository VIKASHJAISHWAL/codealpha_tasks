import random 
words=["python","computer","hangman","program","devloper"]
word=random.choice(words)
word_latters=list(words)
guessed=["-"]*len(word)
attempts=6
print("welcome to hangman!")
print("guess the word")
print("".join(guessed))
while attempts>0 and "-"in guessed:
    guess=input("Enter a letter:").lower()
    if len(guess)!=1 or not guess.isalpha():
        print("Invalid input.Enter a single letter.")
        continue
    if guess in word_latters:
        for i in range(len(word_latters)):
            if word_latters[i]==guess:
                guessed[i]=guess
        print("Good guess")
    else:
        attempts-=1
        print(f"wrong guess! Attempts left:{attempts}")
    print(" ".join(guessed))
    if "-" not in guessed:
        print("Congratulations! You guessed the word:",word)
    else:
        print("Game over! The word was:",word)                
