#!/usr/bin/env python3

# Jordan Banks
# Palomar College CSIT 175
# Lab 8 Excercise 2

# Stores - Python Dictionary Excercise

# if there is no valid data to import 'store' will be set to None
from StoreInfo import store_info as store

def name():
    return f"\t Welcome to {store.information["name"]}"

def phone():
    return f"\t call {store.information["phone_number"]}"

def specials():
    services = ""
    for item in store.information["specials"]:
        services += f"\t {item} ... {store.information["specials"][item]}\n"
    return services

def main():
    print("\n" + name() + "\n"
          + specials() + "\n"
          + phone() + "\n")
    
if __name__ == "__main__":
    if store is not None:
        main()