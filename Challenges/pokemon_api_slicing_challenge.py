import requests

def main():
    pokenum = input("Pick a number between 1 and 151!\n>")
    pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    # Part 1 - Slicing (NO for loop!)
    front_default_url = pokeapi["sprites"]["front_default"]
    print("Front Default Image URL:", front_default_url)

    # Part 2 - Slicing WITH a for loop!
    print("\nMoves:")
    for move in pokeapi["moves"]:
        print(move["move"]["name"])

    # Part 3 - Loop or NOT to Loop
    total_games = len(pokeapi["game_indices"])
    print("\nTotal Number of Games:", total_games)

    # Bonuses
    # Try solving Part 3 with a loop if initially done without, and vice versa
    # Without a loop
    total_games_without_loop = len(pokeapi["game_indices"])
    print("\nTotal Number of Games Without a Loop:", total_games_without_loop)

    # With a loop
    total_games_with_loop = 0
    for game_index in pokeapi["game_indices"]:
        total_games_with_loop += 1
    print("Total Number of Games With a Loop:", total_games_with_loop)

main()