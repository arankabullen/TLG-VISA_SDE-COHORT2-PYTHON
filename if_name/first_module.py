# !usr/bin/env python3

print("This code will always execute.")
def main():
    print("Module #1 Name=", __name__)
    print("This code belongs to main function in Module 1")

if __name__ == "__main__":
    main()
    print("code is being directed by python")

else:
    print("Code is being run indirectly from an import")
