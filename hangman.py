from fig import lista
import random


def enter_letter():
    while True:
        sth = input("Enter letter: ")
        if sth == " ":
            print("You have to enter letter: ")
        elif sth.isdigit():
            print("Not a number. Letter!")
        else:
            return sth


def draw_hangman(counter):
    print(lista[counter])


def choose_letter(word, list):
    hit = 0
    mistake = 0
    cout_draw = 0
    while True:
        try:
            if hit < len(word) and cout_draw < 11:
                letter = enter_letter()
                if letter in word:
                    for x in range(len(word)):
                        if word[x] == letter:
                            hit = hit + 1
                            list[x] = letter
                    for x in list:
                        print(x, end=" ")
                    print()
                else:
                    mistake = mistake + 1
                    draw_hangman(mistake)
                    cout_draw = cout_draw + 1
            else:
                print("The end")
                break
        except IndexError:
            print("Game over")
            break


def main():
    words_list = ["kot", "py", "haha", "ola", "asd"]
    list = []
    word = random.choice(words_list)
    list.extend(word)

    for x in range(len(list)):
        list[x] = "?"

    for x in list:
        print(x, end=" ")
    print()

    choose_letter(word, list)


if __name__ == '__main__':
    main()
