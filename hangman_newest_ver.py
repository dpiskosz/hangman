from fig import lista
import random


class Hangman:
    words = "python django framework engineering science".split()

    def __init__(self):
        self.mistake = 0
        self.hit = 0
        print(20*"*")
        print("Welcome to game 'Hangman'")
        print("(1) Play")
        print("(2) Exit")
        choice = input("Choose what do you want to do: ")
        print(20*"*")
        print()

        if choice == "1":
            print("Okay, we can start.")
            self.start()
        elif choice == "2":
            exit()
        else:
            print("I don't understand. Once again.")
            self.__init__()

    def choose_word(self):
        return self.words[random.randint(0, len(self.words) - 1)]

    def enter_letter(self):
        while True:
            sth = input("Enter letter: ")
            if not (len(sth) == 1 and sth.isalpha()):
                print("It's not a letter.")
            else:
                return sth

    def print_hangman(self):
        print(lista[self.mistake-1])

    def print_chars(self, list_with_chars):
        for x in list_with_chars:
            print(x, end=" ")
        print()

    def logic(self, word, tmp):
        guessed = []
        while True:
            letter = self.enter_letter()
            if letter in word and letter not in guessed:
                for x in range(len(word)):
                    if word[x] == letter:
                        self.hit += 1
                        tmp[x] = letter
                        guessed.append(letter)
                self.print_chars(tmp)
                if self.hit == len(word):
                    print("Winner!")
                    break
            else:
                self.mistake += 1
                self.print_hangman()
                self.print_chars(tmp)
                if self.mistake == 10:
                    print("Game over")
                    break

    def start(self):
        word = self.choose_word()
        tmp = ["?"] * len(word)
        print("Word to guess: ")
        self.print_chars(tmp)
        self.logic(word, tmp)


if __name__ == '__main__':
    hangman = Hangman()
