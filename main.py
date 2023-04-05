#!/usr/bin/env python3
import secrets
import sys

def main():
    # Asks whether to use the default wordlist or not
    ask = input("Would you like to use the default wordlist (y/n): ")

    # Confirms answer
    if ask == "y":
        wordlist = "eff_large_wordlist.txt"
    elif ask == "n":
        wordlist = input("Please enter the name of the wordlist file that was dropped in the folder (case-sensitive): ")
    # Asks how many words to include within the passwor
    num = int(input("Enter number of words: "))

    # Appends path to current working directory to not use absolute paths when opening wordlist
    sys.path.append(".")    

    # Views specified wordlist
    with open(f"wordlists/{wordlist}") as f:

        # Attempts to generate password and print out result
        try:
            words = [word.strip() for word in f]
            password = '-'.join(secrets.choice(words) for i in range(num))
            print(password)
        
        # If error occurs, outputs string and exits script
        except Exception:
            print("Sorry, there was an issue generating your password.")
            exit()
main()

