import customtkinter as ctk
import tkinter as tk
from string import ascii_lowercase as alphabet

from setter import Setter
from solver import Solver

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Desktop Hangman")
        #self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.setter = Setter()
        self.solver = Solver()

        self.large_font = ctk.CTkFont("sans-serif", 40, "bold")

        self.menu_screen()

    def clear(self):
        for child in self.winfo_children():
            child.destroy()

    def menu_screen(self):
        self.clear()

        self.menu_frame = ctk.CTkFrame(self)
        self.menu_frame.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="NSEW")

        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.rowconfigure((0, 1, 2), weight=1)

        ctk.CTkLabel(self.menu_frame, text="Desktop Hangman", font=self.large_font).grid(row=0, column=0, padx=20, pady=(10, 10))

        ctk.CTkButton(self.menu_frame, text="Test Yourself", command=self.use_setter).grid(row=1, column=0, padx=20, pady=(10, 10), sticky="NSEW")
        ctk.CTkButton(self.menu_frame, text="Get the Help of the Solver").grid(row=2, column=0, padx=20, pady=(10, 10), sticky="NSEW")

    def use_setter(self):
        self.clear()

        word_len = self.setter.begin()

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="NSEW")

        self.main_frame.columnconfigure(0, weight=2)
        self.main_frame.columnconfigure(1, weight=1)

        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=25)

        # word
        self.word_frame = ctk.CTkFrame(self.main_frame)
        self.word_frame.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="EW", columnspan=2)
        self.word_frame.columnconfigure(list(range(word_len)), weight=1)

        self.letter_labels = []
        for i in range(word_len):
            self.letter_labels.append(ctk.CTkLabel(self.word_frame, text="_", font=self.large_font))
            self.letter_labels[i].grid(row=0, column=i, padx=20, pady=(10, 10), sticky="NSEW")

        # alphabet buttons
        self.button_frame = ctk.CTkFrame(self.main_frame)
        self.button_frame.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="NSEW")
        self.button_frame.rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.button_frame.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

        self.letter_buttons = []
        for i, letter in enumerate(alphabet):
            self.letter_buttons.append(ctk.CTkButton(self.button_frame, text=letter, font=self.large_font, command=lambda ix=i, l=letter: self.letter_selected(l, ix)))
            self.letter_buttons[i].grid(row=i//6, column=i%6, padx=20, pady=(10, 10), sticky="NSEW")

        self.status_frame = ctk.CTkFrame(self.main_frame)
        self.status_frame.grid(row=1, column=1, padx=20, pady=(10, 10), sticky="NSEW")
    
    def letter_selected(self, letter, index):
        results = self.setter.try_letter(letter)

        if len(results) > 0:
            for result in results:
                self.letter_labels[result].configure(text=letter)

        self.letter_buttons[index].configure(state="disabled")

        if self.setter.check_game_end():
            for button in self.letter_buttons:
                button.configure(state="disabled")

            for i, letter in enumerate(self.setter.word):
                self.letter_labels[i].configure(text=letter)

app = App()
app.mainloop()