from datetime import datetime

#defining single person with a class, initialising same attributes of the given list in the main file
class Person:

    def __init__(self, name,dob,dod=None,parent1=None,parent2=None,spouse=None):
        self.name = name
        self.dob = dob
        self.dod = dod
        self.parent1 = parent1
        self.parent2 = parent2
        self.spouse = spouse

    #method to return name of person object
    def get_name(self):
        return self.name

    #method to return person date of birth
    def get_dob(self):
        return self.dob

    #method to return a list of object's parents checking given parent 1 and parent 2 if present
    def get_parents(self):
        parents = []
        if self.parent1:
            parents.append(self.parent1)
        if self.parent2:
            parents.append(self.parent2)
        return parents

    #method to return spouse if present
    def get_spouse(self):
        return self.spouse

    #method to return whether object is alive or not by checking the presence of date fo death
    def get_alive(self):
        return self.dod is None

    #method to return date of death
    def get_dod(self):
        return self.dod










