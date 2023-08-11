from string import ascii_lowercase as alphabet

from solver import Solver
from setter import Setter

def use_setter():
    print("Test Yourself!")
    
    setter = Setter()
    setter.begin()

    while not setter.game_end():
        print(" ".join(letter for letter in setter.current_state), ":", setter.incorrect_attempts, "incorrect attempts")

        guess = "1"
        while guess not in alphabet or guess in setter.tried_letters:
            guess = input("Pick a letter: ")

        setter.try_letter(guess)

    print(" ".join(letter for letter in setter.word), ":", setter.incorrect_attempts, "incorrect attempts")
    print("Game Over!")

    input("Press ENTER to continue")

def use_solver():
    print("Use the Solver!")

    solver = Solver()

    choice = ""
    while not choice.isdigit():
        choice = input("Number of letters: ")
    solver.begin(int(choice))

    while not solver.game_end():
        print(" ".join(letter for letter in solver.current_state), ":", solver.incorrect_attempts, "incorrect attempts")
        
        next_letter = solver.get_next()
        print("Try:", next_letter)

        print("Enter the indices of the tried letter [leave blank to finish]")
        positions = []
        user_input = "A"
        while user_input != "":
            user_input = input("Next Position: ")
            if user_input.isdigit():
                positions.append(int(user_input))     

        solver.attempt_results(next_letter, positions)

    print(" ".join(letter for letter in solver.current_state), ":", solver.incorrect_attempts, "incorrect attempts")
    print("Game Over!")

    input("Press ENTER to continue")    

def main():
    print("--------------------------------")
    print("What would you like to do?")
    print("1] Test yourself")
    print("2] Use the solver")
    print("3] Exit")

    choice = ""
    while choice not in ["1", "2", "3"]:
        choice = input("Select an option [1/2]: ")

    print("--------------------------------")

    if choice == "1":
        use_setter()
    elif choice == "2":
        use_solver()
    else:
        print("Goodbye!")
        quit()

while True:
    main()