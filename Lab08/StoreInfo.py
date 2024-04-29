#!/usr/bin/env python3

# Jordan Banks
# Palomar College CSIT 175
# Lab 8 Excercise 2

# StoreInfo - Python Dictionary Excercise
# import store information based on user selection

import importlib # for import_module()

# map the list of stores to their info (.py dictionart) files
STORE_INFO_LIST = {
    "tacos": "Taqueria", # if user slects tacos, find file taqueria.py
    "burgers": "BurgerWorld",
    "plants": "Nursery",
    "pets": "Animals",
    "tires": "Tires"
}


def select_store():
    print()
    for store in list(STORE_INFO_LIST):
        print(f"\t", store)
    selection = input("\nchoose a store from the list: ").lower()
    if selection in STORE_INFO_LIST:
        return STORE_INFO_LIST[selection]
    return None

def get_store_info():
    try:
        module = select_store()
        if module is None:
            print("\t no store found.")
            exit()
        return importlib.import_module(module)
    except ImportError:
        print("\t error opening store information file.")
    except Exception:
        print("\tCan't import specified file.")

if __name__ == "__main__":
    print("Did you mean to start this file? Try opening the StoreFront.")

else:
    store_info = get_store_info()