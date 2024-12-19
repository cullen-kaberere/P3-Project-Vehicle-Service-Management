
def validate_input(prompt, valid_options):
    while True:
        value = input(prompt)
        if value in valid_options:
            return value
        print("Invalid input. Please try again.")
