from random import choice
from tkinter.font import names

import family_tree
import person
from family_tree import FamilyTree
from person import Person


#defining the data

tree1 = [['Cornelia Emmersohn', '19/01/1999', None, 'Angel Raciops', 'Nick Lions', 'Otto Emmersohn'],
         ['Angel Raciops', '09/06/1971', None, None, None,'Nick Lions'],
         ['Nick Lions', '21/02/1967', None,None,None,'Angel Raciops'],
         ['Gabriela Lions', '27/06/2003', None,'Angel Raciops', 'Nick Lions','Daniel Three'],
         ['Dominique Lions','02/08/1995',None,'Angel Raciops','Nick Lions','Aniket Budwise'],
         ['Cristian Blackwidow','12/01/1999','12/06/2020',None,None,None],
         ['Daniel Three','04/09/1993',None,None,None,'Gabriela Lions'],
         ['Aniket Budwise','05/05/1996',None,None,None,'Dominique Lions'],
         ['Gaia Three','25/12/2023',None,'Gabriela Lions','Daniel Three',None],
         ['Michael Three','25/12/2023',None,'Gabriela Lions','Daniel Three',None],
         ['Richard Smith','20/04/1998', '13/05/2016', None,None,None],
         ['Josephine Budwise','17/01/2018',None,'Dominique Lions','Aniket Budwise',None],
         ['Otto Emmersohn','07/10/1991',None,None,None,'Cornelia Emmersohn'],
         ]

fam1 = FamilyTree()
fam1.create_family(tree1)
all_people = list(fam1.family.values())





#definition of a menu to play with set methods from family_tree and person files
def menu():

    print('Hello! Welcome to my family tree coursework')
    print('Here there is a list of names that you can choose and below a set menu of functions written, have fun!')
    print('')
    print('Available names: ')
    for member in all_people:
        print(member.name)

    while True:
        print('')
        print('Enter the full name of the person you would like to retrieve info from in lowercase.')
        print('Type 11 to see the list again or exit to exit the code: ')
        name = input().strip().lower()

        if name == 'exit':
            break
        elif name == '11':
            print('Available names: ')
            for member in all_people:
                print(member.name)
            continue

        person = None
        for member in all_people:
            if member.name.lower() == name:
                person = member
                break

        if person is None:
            print(f'error, {name} does not exist')
            continue

        print('')
        print(f'What would you like to know about {name}')

        print('1. View parents')
        print('2. View children')
        print('3. View grandchildren')
        print('4. View sibling(s)')
        print('5. View immediate family')
        print('6. View extended family')
        print('7. View cousin(s).')
        print('8. Check if person is alive')
        print('9. Check average death of everyone combined in family tree')
        print('10. Check number of children of each person on family tree')
        print('11. Check average number of children per person')
        print('')

        action = input('Enter the chosen number: ').strip()
        print('')


        if action == '1':
            parents = person.get_parents()
            parent_str = ' and '.join(parents)
            if parents:
                print(f'the parents of {name} are: {parent_str}')
            else:
                print('no parents data has been added in the code for this person')

        if action == '2':
            child = fam1.get_children(person.name)
            child_str = ' and '.join(child)
            if child:
                print(f'the children of {name} are: {child_str}')
            else:
                print('no children data has been added in the code for this person')

        if action == '3':
            grandchildren = fam1.get_grandchildren(person.name)
            gchild_str = ', '.join(grandchildren)
            if grandchildren:
                print(f'the grandchildren of {name} are: {gchild_str}')
            else:
                print(f'{name} has no grandchildren')

        if action == '4':
            sibling = fam1.get_siblings(person.name)
            sibling_str = ', '.join(sibling)
            if sibling:
                print(f'the sibling(s) of {name} are: {sibling_str}')
            else:
                print(f'{name} has no sibling(s)')

        if action == '5':
            imm_family = fam1.get_immediate_family(person.name)
            parent = person.get_parents()
            sibling = fam1.get_siblings(person.name)
            spouse = person.get_spouse()
            child = fam1.get_children(person.name)

            imm_family_str = ', '.join(imm_family)
            if imm_family:
                print(f'the immediate family (parents,siblings,spouse and children) names of {name} are: {imm_family_str}')
            else:
                print(f'{name} has no immediate family')
            if parent:
                parent_str = ' and '.join(parent)
                print(f'the parents: {parent_str}')
            if sibling:
                siblings_str = ', '.join(sibling)
                print(f'the sibling(s) are: {siblings_str}')
            if spouse:
                print(f'the spouse: {spouse}')
            if child:
                child_str = ' and '.join(child)
                print(f'the children: {child_str}')

        if action == '6':
            extended_family = fam1.get_extended_family(person.name)
            parent = person.get_parents()
            sibling = fam1.get_siblings(person.name)
            spouse = person.get_spouse()
            children = fam1.get_children(person.name)
            aunt_uncle = fam1.get_auntsOrUncles(person.name)
            cousin = fam1.get_cousin(person.name)
            grandchildren = fam1.get_grandchildren(person.name)

            if extended_family:
                extended_family_str = ', '.join(extended_family)
                print(f'the extended family (immediate family, aunts, uncle, cousins) alive of {name} are: {extended_family_str}')
            else:
                print(f'{name} has no extended family')

            if parent:
                parent_str = ' and '.join(parent)
                print(f'the parents: {parent_str}')
            if children:
                children_str = ', '.join(children)
                print(f'the children: {children_str}')
            if grandchildren:
                gchild_str = ', '.join(grandchildren)
                print(f'the grandchildren: {gchild_str}')
            if sibling:
                siblings_str = ', '.join(sibling)
                print(f'the sibling(s): {siblings_str}')
            if spouse:
                print(f'the spouse: {spouse}')
            if aunt_uncle:
                aunt_uncles_str = ', '.join(aunt_uncle)
                print(f'the aunt/uncle: {aunt_uncles_str}')
            if cousin:
                cousin_str = ', '.join(cousin)
                print(f'the cousin(s): {cousin_str}')

        if action == '7':
            cousin = fam1.get_cousin(person.name)
            cousin_str = ', '.join(cousin)

            if cousin:
                print(f'the cousin(s) of {name} are: {cousin_str}')
            else:
                print(f'{name} has no cousin')

        if action == '8':
            alive = person.get_alive()
            if alive:
                print(f'{name} is alive')
            else:
                print(f'{name} is dead')

        if action == '9':
            dead_person = [person.name for person in all_people if person.dod]
            dead_person_str = ', '.join(dead_person)
            average_age_death = fam1.average_death_age(all_people)
            print(f'the dead people are {dead_person_str} and the average age of death is {average_age_death}')

        if action == '10':
            child_count = fam1.number_of_children(all_people)
            for person, count in child_count.items():
                print(f"{person} has {count} children: {fam1.get_children(person)}")

        if action == '11':
            average_numb_child_per_person = fam1.average_number_children(all_people)
            print(f'the average number of children per person is: {average_numb_child_per_person}')


    else:
        print('Invalid input, try again')

menu()














