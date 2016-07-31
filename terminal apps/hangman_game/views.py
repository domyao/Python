
gallows = ["""
    _________
    |       |
            |
            |
            |
            |
            |
            |
------------+---
""",
"""
    _________
    |       |
    O       |
            |
            |
            |
            |
            |
------------+---
""",
"""
    _________
    |       |
    O       |
    |       |
            |
            |
            |
            |
------------+---
""",
"""
    _________
    |       |
    O       |
   \|       |
            |
            |
            |
            |
------------+---
""",
"""
    _________
    |       |
    O       |
   \|/      |
            |
            |
            |
            |
------------+---
""",
"""
    _________
    |       |
    O       |
   \|/      |
    |       |
            |
            |
            |
------------+---
""",
"""
    _________
    |       |
    O       |
   \|/      |
    |       |
   /        |
            |
            |
------------+---
""",
"""
    _________
    |       |
    Q       |
   \|/      |
    |       |
   / \      |
            |
            |
------------+---
"""
][::-1]



class View:

    def welcome_user(self):
        print("Welcome to hangman game!")
        username = input("What's yourname ?\n")
        print("\nHi {}, Best luck to you! \n(you may have up to 7 incorrect guesses each round)\n".format(username))
        input("press any keys to continue...")

    def ask_difficulty(self):
        print("""
Please choose the difficulty
1 for Easy (words of length 3-5)
2 for Medium(words of length 5-7)
3 for Hard (words of length 8+)
(You may not change the difficulty for future rounds)
""")
        return input()


    def ask_difficulty_error(self):
        input("\nplease choose a difficulty level\n (press anykey to continue...)")

    def print_loading_info(self):
        print("\ngenerating the word... initializing the game...")

    def are_you_ready(self):
        return input("\nAre you ready to play (y/n) ")

    def not_ready_response(self):
        return input("whenever you are ready!\n(press any keys to continue, or press q to quit,)....  ")


    def display_round(self, wins, loses):
        print("""

-------------------------- ROUND {} ------------------------------------

        """.format(wins + loses + 1))


    def print_word_display(self, display): #display is a list
        print("".join(display))


    def display_gallows(self, chances):
        print(gallows[chances])

    def remind_chances_left(self, chances):
        print("{} incorrect guesses left\n".format(chances))


    def ask_for_letter(self):
        return input("\nguess a letter: \n")

    def ask_for_letter_again(self):
        return input("Guess either one letter or the complete phrase: \n")

    def print_letters_guessed(self, letter_guessed):
        print(list(letter_guessed) )

    def print_answer(self, chosen_word):
        print("\nThe answer is {}\n".format(chosen_word))

    def print_winning(self):
        print("you win! well done OvO")

    def ask_to_play_again(self):
        return input("Play again? (y/n)\n")

    def say_goodbye(self, difficulty, wins, loses):

        if difficulty == '1':
            diff_str = "Easy"
        elif difficulty == '2':
            diff_str = "Medium"
        else: #difficulty is 3
            diff_str = "Hard"

        input("\nGamePlay Review...")
        print("\nDifficulty {}\nWins {}\nLoses {}\n".format(diff_str, wins, loses))

        if wins >= loses:
            print("You've done great job! See you next time :D\n\n\n")
        else:
            print("good Luck next time! LoL")




if __name__ == "__main__":
    v = View()
