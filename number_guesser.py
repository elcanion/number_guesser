import random
from datetime import datetime
import pickle

#Use this to rewrite the high score entries to its default values
def rewind_high_scores():
    high_scores = [("Bob", 4, "23-05-2021"), 
                    ("Jane", 6, "15-07-2021"), 
                    ("Ray", 9, "11-03-2021"), 
                    ("Goofy", 13, "29-02-2021"), 
                    ("Ash", 18, "09-05-2021")]
    with open('highscore.dat', 'wb') as f:
        pickle.dump(high_scores, f)
    f.close()

def make_random_number():
    return random.randint(1, 10)

#It's literally that
def get_second_item_from_tuple(item):
    return item[1]

def submit_score(name, tries):
    file_name = "highscore.dat"

    with open(file_name, 'rb') as f:
        loaded_list = pickle.load(f)
    loaded_list.append((name, tries, datetime.today().strftime('%d-%m-%Y')))
    loaded_list.sort(key = get_second_item_from_tuple)
    loaded_list.pop(-1)
    f.close()

    with open(file_name, 'wb') as f:
        pickle.dump(loaded_list, f)
    f.close()

def compare(computer_number, guess):

    if guess < computer_number:
        print(f"The chosen number is greater than {guess}")
        return False
    elif guess > computer_number:
        print(f"The chosen number is lesser than {guess}")
        return False
    else:
        return True

def endgame():
    print("THE GAME IS OVER")
    file_name = "highscore.dat"

    with open(file_name, 'rb') as f:
        loaded_list = pickle.load(f)

    for player in loaded_list:
        print(player)

def main():
    rewind_high_scores()
    tries = 1
    check_endgame = False
    print("----- Number Guesser -----")
    computer_number = make_random_number()
    while check_endgame == False:
        try:
            guess = int(input("Make a guess: "))
            check_endgame = compare(computer_number, guess)
            print(f"Tries: {tries}")
            tries += 1
        except ValueError:
            print("Input must be an integer")
    name = input("Tell me your name: ")
    submit_score(name, tries)
    endgame()

if __name__ == "__main__":
    main()

