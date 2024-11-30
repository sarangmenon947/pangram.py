import pgzrun

# Set the window dimensions
WIDTH = 800
HEIGHT = 600

# Initialize variables
user_input = ""
message = ""

# Function to check if a string is a pangram
def is_pangram(input_string):
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    input_set = set(input_string.lower())
    return alphabet_set.issubset(input_set)

def draw():
    # Clear the screen with a black color
    screen.clear()
    screen.fill((0, 0, 0))  # Fill with black color

    # Display instructions and messages
    screen.draw.text("Enter a string (or type 'exit' to quit):", (50, 50), fontsize=30, color="white")
    screen.draw.text(user_input, (50, 100), fontsize=30, color="yellow")
    screen.draw.text(message, (50, 150), fontsize=30, color="green")

def update():
    pass  

def on_key_down(key):
    global user_input, message
    
    if key == keys.RETURN:
        if user_input.lower() == 'exit':
            print("Thanks for playing! Goodbye!")
            exit()
        elif is_pangram(user_input):
            message = "The given string is a pangram."
        else:
            message = "The given string is not a pangram."
        user_input = ""  # Clear input after processing

    elif key == keys.BACKSPACE:
        user_input = user_input[:-1]  # Remove last character on backspace
    else:
        # Add the pressed key character to user_input if it's a valid character
        char = key.name
        if len(char) == 1:  # Ensure it's a single character
            user_input += char

# Start the game
pgzrun.go()