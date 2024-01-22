def bottles_of_beer(num):
    if num == 0:
        return "No more bottles of beer on the wall!"
    elif num == 1:
        return f"1 bottle of beer on the wall!\n1 bottle of beer! You take one down, pass it around!"
    else:
        return f"{num} bottles of beer on the wall!\n{num} bottles of beer! You take one down, pass it around!"

def main():
    max_bottles = 100

    try:
        num_bottles = int(input(f"How many bottles of beer do you want to count down from? (1-{max_bottles}): "))
        if num_bottles < 1 or num_bottles > max_bottles:
            raise ValueError("Invalid input. Please enter a number between 1 and 100.")
    except ValueError as e:
        print(e)
        return

    for i in range(num_bottles, 0, -1):
        print(bottles_of_beer(i))
        if i - 1 > 0:
            print(f"{i - 1} bottles of beer on the wall!\n")
        else:
            print("No more bottles of beer on the wall!")

if __name__ == "__main__":
    main()