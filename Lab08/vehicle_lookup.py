#!/usr/bin/env python3

# Jordan Banks
# Palomar College CSIT 175
# Lab 8 Excercise 3, Find a vehicle bby license number

import os # getcwd()
import csv # dictreader()

VEHICLE_LIST = "cars.csv"
DMV_DATABASE = "registration.csv"

class DataRecordSizeError(Exception):
    def __init__(self, message):
        super().__init__(message)

def read_registration_list(filename):
    # write the code to read the data into the python dictionary using the pattern below
    license_numbers = {} # {"lic": "vin"}
    try:
        with open(filename, "r") as datafile:
            reader = csv.reader(datafile)
            for data_entry in reader:
                if len(data_entry) != 2:
                    raise DataRecordSizeError("Data Record Size Error")
                license_numbers[data_entry[0]] = data_entry[1]
    except FileNotFoundError:
        print(filename, "not found")
    except Exception as e:
        print("Error:", e)
    return license_numbers

def read_vehicle_list(filename):
    # write the code to read the data into the pythin dictionary using the pattern below
    cars = {} # {"vin": {"year": "", "make": "", "model": ""}}
    try:
        with open(filename,"r") as datafile:
            reader = csv.reader(datafile)
            for data_entry in reader:
                cars[data_entry[0]] = {"year": data_entry[1], "make": data_entry[2], "model": data_entry[3]}
            else:
                raise DataRecordSizeError("Data Record Size Error")
    except FileNotFoundError:
        print(filename,"not found")
    except Exception as e:
        print("Error:", e)
    return cars

def main():
    license_plates = ["DTJ-720", "GUO-657", "HMQ-267", "TDJ-576", "FBD-049",
                      "AJQ-950", "KRP-582", "YAH-850", "U0Z-666", "LUW-876"
                      ]
    registration = read_registration_list(DMV_DATABASE)
    cars = read_vehicle_list(VEHICLE_LIST)
    for lic in license_plates:
        if lic in registration:
            vehicle = registration[lic]
            if vehicle in cars :
                car_details = cars[vehicle]
                print(f"{lic}: {car_details['year']} {car_details['make']} {car_details['model']}")
            else: print(f"{lic=} is valid, "
                        + f"{vehicle} not found in {VEHICLE_LIST}")
        else:
            print(f"{lic}: not in {DMV_DATABASE}")

if __name__ == "__main__":
    main()