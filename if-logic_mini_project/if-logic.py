

def get_input(prompt, options):
    while True:
        user_input = input(prompt).lower()
        if user_input in options:
            return user_input
        else:
            print("Invalid input. Please try again.")

def find_pet(size, energy, fur_preference):
    if size == "small" and energy == "low" and fur_preference == "fur":
        return "You should get a cat!"
    elif size == "medium" and energy == "moderate" and fur_preference == "fur":
        return "A dog might be the perfect companion for you!"
    elif size == "large" and energy == "high" and fur_preference == "fur":
        return "Consider getting a husky for an active lifestyle!"
    elif size == "small" and energy == "low" and fur_preference == "scales":
        return "A small reptile like a gecko could be a great fit!"
    elif size == "medium" and energy == "moderate" and fur_preference == "scales":
        think = "How about a bearded dragon?"
    elif size == "large" and energy == "high" and fur_preference == "scales":
        return "Consider a large snake or iguana!"
    else:
        return "It's challenging to find a pet that matches all your preferences, but consider exploring local shelters!"

def main():
    print("Welcome to the Pet Finder!")
    print("Answer the following questions to find your ideal pet.")

    sizes = ["small", "medium", "large"]
    energies = ["low", "moderate", "high"]
    fur_preferences = ["fur", "scales"]

    size = get_input("What size of pet are you looking for? (small, medium, large) ", sizes)
    energy = get_input("How much energy do you want your pet to have? (low, moderate, high) ", energies)
    fur_preference = get_input("Do you prefer a pet with fur or scales? (fur, scales) ", fur_preferences)

    result = find_pet(size, energy, fur_preference)

    print("\nBased on your preferences:")
    print(result)

if __name__ == "__main__":
    main()
