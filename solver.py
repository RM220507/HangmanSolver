import json
import re
from string import ascii_lowercase as alphabet

from baseclass import BaseClass

class Solver(BaseClass):
    def __init__(self):
        super().__init__()

        with open("refined-words.json", "r") as f:
            self.words = json.load(f)

    def begin(self, num_letters):
        self.current_state = ["_" for i in range(num_letters)]
        self.num_letters = num_letters

        self.possible_words = self.words[str(num_letters)]

        self.reset_counters()

    def attempt_results(self, letter, positions):
        # function to append a tried letter to the tried_letters list and update the possible_words list according to new information
        self.letter_tried(len(positions) > 0, letter)

        if len(positions) > 0:
            for position in positions: # set each position to the letter
                self.current_state[position] = letter

        ignore_chars = f"[^{''.join(l for l in self.tried_letters)}]"
        regex_string = "".join(l if l != "_" else ignore_chars for l in self.current_state)

        old_words = self.possible_words.copy()
        self.possible_words = []

        for word in old_words:
            if re.search(regex_string, word):
                self.possible_words.append(word)

    def get_next(self):
        letter_frequency = {}
        
        for letter in alphabet:
            if letter in self.tried_letters:
                continue

            frequency = 0
            for word in self.possible_words:
                frequency += word.count(letter)

            letter_frequency[letter] = frequency

        values = list(letter_frequency.values())

        return list(letter_frequency.keys())[values.index(max(values))]
    
solver = Solver()
solver.begin(10)

