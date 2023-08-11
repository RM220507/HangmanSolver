import json
import random

from baseclass import BaseClass

class Setter(BaseClass):
    def __init__(self):
        super().__init__()

        with open("refined-words.json", "r") as f:
            self.words = json.load(f)

    def begin(self, num_letters=None):
        self.select_word(num_letters)

        self.current_state = ["_" for l in self.word]
        self.reset_counters()

        return len(self.word)

    def select_word(self, num_letters=None):
        if num_letters:
            word_list = self.words.get(str(num_letters))
            if word_list:
                self.word = random.choice(word_list)
            else:
                self.select_word()
        else:
            self.word = random.choice(self.words[self.weighted_length()])

    def try_letter(self, letter):
        occurrences = [i for i, char in enumerate(self.word) if char == letter]
        
        self.letter_tried(len(occurrences) > 0, letter)
        
        for occurrence in occurrences:
            self.current_state[occurrence] = letter

        return occurrences

    def weighted_length(self):
        total_weight = sum(len(lst) for lst in self.words.values())
        random_number = random.randint(0, total_weight - 1)

        for key, lst in self.words.items():
            random_number -= len(lst)
            if random_number < 0:
                return key