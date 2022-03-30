from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=100, pady=50)
window.title("Flash card")

CURRENT_WORD = ""

CARD_FRONT_IMG = PhotoImage(file="images/card_front.png")
CARD_BACK_IMG = PhotoImage(file="images/card_back.png")


card_f = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_b = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)



def create_card():
    global CURRENT_WORD
    data = pandas.read_csv(filepath_or_buffer="data/french_words.csv")
    row_index = random.randint(0, 99)
    card_front = card_f.create_image(400, 263, image=CARD_FRONT_IMG)
    card_f_language = card_f.create_text(400, 150, text="French", font=("Calibri", 15))
    french_word = data.French[row_index]
    card_f_word = card_f.create_text(400,200, text=french_word, font=("Calibri", 40))

    card_back = card_b.create_image(400, 263, image=CARD_BACK_IMG)
    card_b_language = card_b.create_text(400, 150, text="English", font=("Calibri", 15))
    english_word = data.English[row_index]
    card_b_word = card_b.create_text(400, 200, text=english_word, font=("Calibri", 40))
    CURRENT_WORD = french_word
    with open("learned_words.txt") as file:
        data = file.readlines()
        if CURRENT_WORD in data:
            create_card()



def display_front_card():
    card_b.grid_remove()
    return card_f.grid(column=0, row=0, columnspan=2)


def display_back_card():
    card_f.grid_remove()
    return card_b.grid(column=0, row=0, columnspan=2)

def add_to_known():
    with open("learned_words.txt", "a") as file:
        file.write(f"{CURRENT_WORD}, ")

    game()

def game():
    create_card()
    display_front_card()
    window.after(3000, display_back_card)

game()

right_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=add_to_known)
right_button.grid(column=1, row=1)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=game)
wrong_button.grid(column=0, row=1)


window.mainloop()

