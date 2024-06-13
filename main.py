import random

def computer_guess_number(x):
    """
    Let the computer guess the user's number within a given range.

    Args:
        x (int): The upper limit of the range for the user's number.

    Returns:
        None
    """
    # Define the lower and upper bounds of the range
    low = 1
    high = x

    # Initialize feedback variable
    feedback = ' '

    # Continue guessing until correct
    while feedback != 'c':
        # Generate a random guess within the current range
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        # Ask for feedback
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        # Update the range based on feedback
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    # Once correct number is guessed, print a congratulatory message
    print(f"Yay! The computer guessed your number {guess} correctly!")

# Test the function with an upper limit of 10
computer_guess_number(10)

