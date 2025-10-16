from itertools import count
from datetime import datetime
from person import Person


class FamilyTree:

    # defining dictionary of objects
    def __init__(self):
        self.family = {}

    #method to access list of family members details looping information for each member according to person class
    def create_family(self, tree_data):

        #for loop to go through each element of the list of lists set in main
        for member_data in tree_data:
            name, dob, dod, parent1_name, parent2_name, spouse_name = member_data

            #creating an instance of person class for each member passing the details to Person class
            person = Person(name, dob, dod, parent1_name, parent2_name, spouse_name)


            self.family[name] = person #adding person object to the dictionary family

    #method to get children
    def get_children(self, name):
        children = [] #empty list to store children's name
        #loop that iterates the dictionary's values to check if parent1 or parent2 matches the given name passed in the method
        for member in self.family.values():
            if member.parent1 == name or member.parent2 == name:
                children.append(member.name)
        return children

    #method to get grandchildren (children of children)
    def get_grandchildren(self, name):
        grandchildren = [] #empty list to store names
        children = self.get_children(name) #finding the children of the given person in the method using get_children
        for child in children: #loop to check each child of children
            grandchildren.extend(self.get_children(child))
        return grandchildren


    #method to find siblings of given person
    def get_siblings(self, name):
        target_person = self.family.get(name) #targeting the object if exists in dictionary
        if not target_person:
            return []

        siblings = [] #empty list to store siblings names
        for member in self.family.values(): #loop to check all values in self.family
            #ensuring name taken into consideration is not going to be checked
            #check if members have parent1 and parent2 in common which means they are siblings
            if member.name != name and (
                    (member.parent1 and member.parent1 in target_person.get_parents()) or
                    (member.parent2 and member.parent2 in target_person.get_parents())
            ):
                siblings.append(member.name)

        return siblings

    #methos to find aunties or uncles of given name by checking parents' siblings and their spouses
    def get_auntsOrUncles(self, name):
        target_person = self.family.get(name) #targeting the object name
        if not target_person:
            return []

        aunts_uncles = set() #add set method so duplicates are not added here (problem with printing cousins twice)


        parent1, parent2 = target_person.parent1, target_person.parent2 #extracting the parents of given member

        #check siblings of parent 1 using get_sibling
        if parent1:
            parent1_siblings = self.get_siblings(parent1)
            aunts_uncles.update(parent1_siblings)

        #check sibling of parent 2 using get_sibling
        if parent2:
            parent2_siblings = self.get_siblings(parent2)
            aunts_uncles.update(parent2_siblings)

        #check spouses for each sibling using for loop checking if they have a spouse
        for member in self.family.values():
            if member.spouse in aunts_uncles and member.name not in aunts_uncles:
                aunts_uncles.add(member.name)

        return list(aunts_uncles)

    #method to check cousins of given name by using get_children and get_auntsorUncles
    def get_cousin(self, name):
        cousin = [] #empty list to append cousins'names

        aunts_uncles = self.get_auntsOrUncles(name)

        for uncle_aunt in aunts_uncles:
            cousin.extend(self.get_children(uncle_aunt))

        return list(set(cousin)) #set method applied so there is no duplicate

    #method to check immediate family (children, siblings, parents, spouses)
    def get_immediate_family(self, name):
        target_person = None
        for member in self.family.values():
            if member.name == name:
                target_person = member
                break

        immediate_family = [] #empty list to append names retrieved from method already checked above
        immediate_family.extend(self.get_children(name)) #checking if given person has children
        immediate_family.extend(self.get_siblings(name)) #checking if given person has siblings
        parents = target_person.get_parents()
        if parents:
            immediate_family.extend(parents) #checking if person has parents
        spouse = target_person.get_spouse()
        if spouse:
            immediate_family.append(spouse) #checking if given person has spouse

        return immediate_family

    #method to get extended family of a given person (immediate family, cousins, aunties or uncles, all alive)
    def get_extended_family(self, name):
        target_person = self.family.get(name)
        if not target_person:
            return []

        extended_family = [] #empty list to store all names
        extended_family.extend(self.get_immediate_family(name)) #check immediate family (siblings, parents, spouses, children)
        extended_family.extend(self.get_auntsOrUncles(name)) #check if person has aunties or uncles
        extended_family.extend(self.get_cousin(name)) #check if person has cousins
        extended_family.extend(self.get_grandchildren(name))


        return [member for member in extended_family if
                member in [person.name for person in self.family.values() if person.get_alive()]] #every single person must be alive, used get_alive from Person Class

    #method to calculate average age of death of all dead people in the list of all_people
    def average_death_age(self, all_people):

        deceased_people = [person for person in all_people if person.dod] #retrieving only dead people (people with dod inserted in the list)
        date_format = "%d/%m/%Y" #chaning format of string to specify the way it has been written, using datetime imported
        death_age = 0 #intialised variable to 0 to accumulate ages at death

        #for loop that checks only dead people and converts the date of death into a string and retrieved only the year (.year)
        for dead in deceased_people:
            dob_year = datetime.strptime(dead.dob, date_format).year
            dod_year = datetime.strptime(dead.dod, date_format).year

            #difference between year of death and year of birth = age at death and added to variable death_age
            death_age += dod_year - dob_year
        average_death_age = death_age/len(deceased_people) #once all ages are checked they are divided by the number (length) of dead people

        return average_death_age

    #method to calculate number of children of every single object in the list using get_children accepting all_people
    def number_of_children(self, all_people):
        child_count = {} #because we are checking all the people, we need to initialise an empty dictionary

        #loop to go through every single person
        for person in all_people:
            children = self.get_children(person.name) #checking children for every single person
            child_count[person.name] = len(children) #returning count = number (length) of found children

        return child_count

    #method to check average number of children of all people considering all_people and number of children calculated above
    def average_number_children(self, all_people):

        total_children = sum(self.number_of_children(all_people).values()) #values = number of children
        total_people = len(all_people) #calculating the number (length) of people in all_people

        average_children = total_children / total_people #average = tot number of children divided by tot number of people
        return average_children


























