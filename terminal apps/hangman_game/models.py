
import random as r

class HangmanGame:
    wins = 0
    loses = 0


    def __init__(self, chosen_word):
        self.chances = 7
        self.answer = list(chosen_word)
        self.letters_guessed = set()
        self.display = ['_' if x != ' ' else ' ' for x in self.answer]



    @staticmethod
    def choose_word(difficulty):
        with open('wordlist.txt') as nf:
            words = nf.read().splitlines()

        if difficulty == 1:
            words = [x for x in words if len(x) >= 3 and len(x) <=5 ]
        elif difficulty == 2:
            words = [x for x in words if len(x) >= 5 and len(x) <=7  ]
        elif difficulty == 3:
            words = [x for x in words if len(x) >= 8 ]

        word = words[int(r.random() * len(words))]

        return word



    def guess_letter(self, letter):
        correct = self.check_if_guessed_already(letter)

        for idx, value in enumerate(self.answer):
            if value.lower() == letter.lower():
                self.display[idx] = self.answer[idx]   # replace the _ with correctly guessed
                correct = True

        if correct == False:
            self.chances -= 1

        return correct



    def check_if_guessed_already(self, letter):
        correct = False

        if letter in self.letters_guessed:   # if the letter guessed alerady been guessed before, then just pass no matter whether it is wrong or right
            correct = True

        self.letters_guessed.add(letter)

        return correct


    def check_is_answer(self, letter, chosen_word):
        if letter.lower() == chosen_word.lower():
            self.display = self.answer
            return True

        return False
