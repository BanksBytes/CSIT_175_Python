#!/usr/bin/env python3

# Jordan Banks
# Palomar College CSIT 175
# Lab 7 Excercise 3, Calculate student grades and save gradebook

import csv
import random

# Variable
test_score_filename = "test_scores.csv"

# declare constants
NUM_ASSIGNMENTS = 12
MIN_SCORE = 76
MAX_SCORE = 100
ASSIGNMENTS = NUM_ASSIGNMENTS
students = ["Alice", "Bob", "Charlie", "David", "Emma",
            "Frank", "Grace", "Henry", "Ivy", "Jack",]

# be careful with indentation!

# build the file header
def build_header():
    header = ["Name"]
    for i in range(ASSIGNMENTS):
        header.append(f"ex.{i}")
        header.append("average")
        header.append("grade")
        return header

# calculate final grade
def assign_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

# get (pseudo-random) assignement scores
def get_scores(student_name):
    # reset grades
    total = 0
    grades = []
    grades.append(student_name)
    for i in range(ASSIGNMENTS):
        # Changed hardcoded numbers to their constants
        score = random.randint(MIN_SCORE, MAX_SCORE)
        total += score
        grades.append(score)
    average_score = round(total / ASSIGNMENTS)
    grades.append(round(average_score))
    grades.append(assign_grade(average_score))
    return grades

def main():
    # create the new file
    with open("gradebook.csv", "w", newline="") as output_file:
        gradebook = csv.writer(output_file)
        #build and write the file header
        gradebook.writerow(build_header())
        # build and write each student record
        for student in students:
            gradebook.writerow(get_scores(student))
        print(f"{len(students)} records written.")

try:
    with open(test_score_filename, "r") as file:
        # if the file exists prompt the user
        print(f"The file {test_score_filename} already exists.")
        choice = input("Do you want to overwrite the file? (yes/no): ").lower() # keep the input to lowercase
        # if the user chooses yes write the file
        if choice =="yes":
            with open(test_score_filename, "w") as file:
                print(f"The file {test_score_filename} has been overwritten.")
        # if no exit program
        else:
            print("Exiting the program")
    
except FileNotFoundError:
    # If the file does not exist, create it
    with open(test_score_filename, "w") as file:
        print(f"The file {test_score_filename} has been created")


if __name__ == "__main__":
    # initialize random object to create repeatable randomness
    random.seed(42)
    main()




