import logging

from setter import Setter
from solver import Solver

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Create a console handler and set level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a file handler and set level to DEBUG
file_handler = logging.FileHandler('testing-100000.log')
file_handler.setLevel(logging.DEBUG)

# Create formatters and set them for handlers
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

# Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

TEST_COUNT = int(input("Number of Tests: "))

tests_won = 0
losing_words = []

setter = Setter()
solver = Solver()

logger.info(f"Performing {TEST_COUNT} tests.")

for test in range(TEST_COUNT):
    logger.info(f"Performing TEST {test}:")

    word_len = setter.begin()
    solver.begin(word_len)

    logger.debug(f"Word is: {setter.word}.")

    while not setter.game_end():
        logger.debug(f"{len(solver.possible_words)} possible words.")

        letter = solver.get_next()
        result = setter.try_letter(letter)
        solver.letter_tried(letter, result)

        logger.debug(f"Tried letter: {letter}; with result: {result}.")
        logger.debug(f"Attempts made: {setter.attempts_made}; incorrect attempts: {setter.incorrect_attempts}; correct attempts: {(setter.attempts_made - setter.incorrect_attempts)}.")

    logger.info(f"TEST {test} complete.")

    if setter.wrong_attempts >= 9:
        logger.info(f"TEST {test}: LOSS.")
        losing_words.append(setter.word)
    else:
        logger.info(f"TEST {test}: WIN.")
        tests_won += 1

logger.info(f"{TEST_COUNT} tests completed.")
logger.info(f"{tests_won}/{TEST_COUNT} WON.")
logger.info(f"Losing words: {set(losing_words)}")