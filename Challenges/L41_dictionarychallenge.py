marvelchars = {
    "Starlord": {"real name": "peter quill", "powers": "dance moves", "archenemy": "Thanos"},
    "Mystique": {"real name": "raven darkholme", "powers": "shape shifter", "archenemy": "Professor X"},
    "Hulk": {"real name": "bruce banner", "powers": "super strength", "archenemy": "adrenaline"}
}

def get_input(prompt):
    return input(prompt).lower()

def get_character_info(char_name, char_stat):
    char_name_lower = char_name.lower()
    char_stat_lower = char_stat.lower()

    if char_name_lower in marvelchars and char_stat_lower in marvelchars[char_name_lower]:
        value = marvelchars[char_name_lower][char_stat_lower]
        if char_stat_lower == "real name":
            value = value.title()  # Capitalize the first letters of each word for real name
        return value
    else:
        return None

def main():
    while True:
        char_name = get_input("Which character do you want to know about? (Starlord, Mystique, Hulk) ")
        char_stat = get_input("What statistic do you want to know about? (real name, powers, archenemy) ")

        character_info = get_character_info(char_name, char_stat)

        if character_info is not None:
            print(f"{char_name.title()}'s {char_stat} is: {character_info}")
        else:
            print("Invalid input. Please try again.")

        try_again = get_input("Do you want to try again? (yes/no) ")
        if try_again != "yes":
            break

if __name__ == "__main__":
    main()