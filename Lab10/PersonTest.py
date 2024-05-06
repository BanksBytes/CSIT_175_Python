#!/usr/bin/env python3
# Jordan Banks
# Lab 10 ex.5 Person Class Fixtures

from Employee import Employee
from Student import Student

# Employee Class Object
print("\nEmployee: ")
name = input("Enter Name: ")
address = input("Enter Address: ")
age = int(input("Enter Age: "))
job_skill = input("Enter Job Skill: ")
years_worked = int(input("Enter Years Worked: "))

employee_info = Employee(name, address, age, job_skill, years_worked)

print(employee_info.to_string())

# Student Class Object
print("\nStudent: ")
name = input("Enter Name: ")
address = input("Enter Address: ")
age = int(input("Enter Age: "))
major = input("Enter Major: ")
units = int(input("Enter # of Units Completed: "))

student_info = Student(name, address, age, major, units)

print(student_info.to_string())