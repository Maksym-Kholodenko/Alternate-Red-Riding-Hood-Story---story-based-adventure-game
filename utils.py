def get_choice(valid_choices):
    choice = input("> ").strip()

    while choice not in valid_choices:
        print("Please choose a valid option.")
        choice = input("> ").strip()

    return choice
    