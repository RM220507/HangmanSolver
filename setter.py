import json
import random

class Setter:
    def __init__(self):
        with open("refined-words.json", "r") as f:
            self.words = json.load(f)

    def begin(self, num_letters=None):
        self.select_word(num_letters)

        self.current_state = ["_" for l in self.word]
        self.unique_characters = len(set(self.word))

        self.attempts_made = 0
        self.wrong_attempts = 0

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
        
        self.attempts_made += 1

        if len(occurrences) == 0:
            self.wrong_attempts += 1
        
        for occurrence in occurrences:
            self.current_state[occurrence] = letter

        return occurrences
    
    def check_game_end(self):
        return self.wrong_attempts >= 9 or self.current_state.count("_") == 0

    def weighted_length(self):
        total_weight = sum(len(lst) for lst in self.words.values())
        random_number = random.randint(0, total_weight - 1)

        for key, lst in self.words.items():
            random_number -= len(lst)
            if random_number < 0:
                return key