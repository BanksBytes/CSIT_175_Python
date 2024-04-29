#!/usr/bin/env python3

# Jordan Banks
# Palomar College CSIT 175
# Lab 8 Excercise 1, Country Code program from Murach's Python Programming, chap 12

def display_menu():
    print()
    # Q: What does the '\t' do in the code?
    # A: Adds a tab before the string
    print("\tCOMMAND MENU")
    print("\tview - View country name")
    print("\tadd - Add a country")
    print("\tdel - Delete a country")
    print("\texit - Exit program")
    print()

def display_codes(countries):
    # Q: why is the list() command here?
    # A: This will covnert the keys from countries to a string  so we can use sort()
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)

def view(countries):
    display_codes(countries)
    code = input("Enter coutnry code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}.\n")
    else:
        print("There is no country with that code.\n")
def add(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code.\n")
    else:
        name = input("Enter country name: ")
        # Q: WHat does title() do?
        # A: This keeps uniformity, so that when a new 
        # A: country gets added it has the first initial
        # A: capatlized and the rest lowercase
        name = name.title()
        countries[code] = name
        print(f"{name} was added.\n")

def delete(countries):
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries.pop(code)
        print(f"{name} was deleted.\n")
    else:
        print(f"There is no country with that code.\n")


def main():
    countries = {"CA": "Canada",
                 "US": "United States",
                 "MX": "Mexico"}
    
    display_menu()
    while True:
        command = input("Command: ")
        if command.lower() == "view":
            view(countries)
        elif command.lower() == "add":
            add(countries)
        elif command.lower() == "del":
            delete(countries)
        elif command.lower() == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

if __name__ == "__main__":
    main()