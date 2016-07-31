

from views import View, gallows
from models import HangmanGame
import re



class HangmanController:

    """
    This is the hangman game

    1. First choose a difficulty, you cannot change change the difficulty for the futher rounds

    2. Then you will be asked if you are ready to play.
       if you are not, you will be waited until you hit any keys to continue game, or press 'q' to exit the game

    3. You can enter either one letter or the complete phrase at each guess,
       any other cases happend(enter nothing or more than one letter yet not the complete phrase), you will be asked to guess again without penalty.

    4. if you guess a wrong letter, the hangman is one step closer to be hung;
       However, if you enter a wrong letter that has been guessed before, nonthing will happen

    5. At the end of the game, you will be ask whether to play again.
       If you chose to end the game, an achievement review will be printed out.
       If you have wins more than loss, Bravo!


    """

    # WINS = 0
    # LOSES = 0
    # ROUND = 1


    def __init__(self):
        self.view = View()
        self.game = None



    def run(self):
        self.view.welcome_user()
        difficulty = self.generate_difficulty()
        play_again = 'y'

        while play_again.lower() == 'y':
            user_input = self.view.are_you_ready()
            if user_input.lower() == 'y':
                self.start_game(int(difficulty))
            else:
                if self.view.not_ready_response().lower() == 'q':
                    play_again = 'n'
                continue             #if user enter 'q', then quit the game, set play_again to 'n'

            play_again = self.view.ask_to_play_again()

        else:
            if self.game != None:    #if the user quit game before even played once, self.game is None
                self.view.say_goodbye(difficulty, HangmanGame.wins, HangmanGame.loses)


    def generate_difficulty(self):

        difficulty = self.view.ask_difficulty()

        while not re.match(r'[123]', difficulty):
            self.view.ask_difficulty_error()
            difficulty = self.view.ask_difficulty()

        return difficulty



    def start_game(self, difficulty):

        self.view.print_loading_info()
        chosen_word = HangmanGame.choose_word(difficulty)
        self.game = HangmanGame(chosen_word)
        print(HangmanGame.wins, HangmanGame.loses)
        self.view.display_round(HangmanGame.wins, HangmanGame.loses)
        print(chosen_word)

        self.view.display_gallows(self.game.chances)

        while self.game.chances > 0 and self.game.display != self.game.answer:

            self.view.print_letters_guessed(self.game.letters_guessed)
            self.view.print_word_display(self.game.display)
            letter = self.view.ask_for_letter()
            self.submit_guess(letter, chosen_word)

        self.end_game(chosen_word)



    def submit_guess(self, letter, chosen_word):


        while len(letter) != 1 and letter.lower() != chosen_word.lower():
            letter = self.view.ask_for_letter_again()
        #Should I put those here or in the models
        is_answer = self.game.check_is_answer(letter, chosen_word)

        if not is_answer:
            is_correct = self.game.guess_letter(letter)

            if not is_correct:
                self.view.display_gallows(self.game.chances)
                self.view.remind_chances_left(self.game.chances)


    def end_game(self, chosen_word):
        self.view.print_answer(chosen_word)

        if self.game.display == self.game.answer:
            self.view.print_winning()
            HangmanGame.wins+= 1
        else:
            HangmanGame.loses+= 1



if __name__ =="__main__":
    newgame = HangmanController()
    newgame.run()
