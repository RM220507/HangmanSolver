class BaseClass:
    def __init__(self):
        self.incorrect_attempts = 0
        self.attempts_made = 0

        self.tried_letters = []

    def letter_tried(self, correct, letter):
        self.tried_letters.append(letter)
        self.attempts_made += 1
        if not correct:
            self.incorrect_attempts += 1

    def reset_counters(self):
        self.incorrect_attempts = 0
        self.attempts_made = 0

    def game_end(self):
        return self.incorrect_attempts >= 9 or self.current_state.count("_") == 0