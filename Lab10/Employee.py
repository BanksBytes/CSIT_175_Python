#!/usr/bin/env python3
# Jordan Banks
# Lab 10 ex.5 Employee class implementation
#
from Person import Person

class Employee(Person):

    def __init__(self, name, address, age, job_skill, years_worked):
        # Override Person construct 
        super().__init__(name, address, age)
        self.__job_skill = job_skill
        self.__years_worked = years_worked

    # getter and setters
    def get_job_skill(self):
        return self.__job_skill
    
    def set_job_skill(self, job_skill):
        self.__job_skill = job_skill

    def get_years_worked(self):
        return self.__years_worked
    
    def set_years_worked(self, years_worked):
        self.__years_worked = years_worked

    # to string
    def to_string(self):
        return super().to_string() + " Job Skill: " + self.__job_skill + \
            " Years Worked: %d" % self.__years_worked
    



# def to_string(self):
#     return "{}\nJob Skill: {}\nYears Worked: {}".format(super().to_string(), self.__job_skill, self.__years_worked)
