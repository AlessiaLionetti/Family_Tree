from person import Person
from family_tree import FamilyTree
import unittest

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
#creation of a class to test every single method or scenario created between the Person class and the FamilyTree class
# usage of selfassertEqual to make sure actual output matches expected output
class TestFamilyMethods(unittest.TestCase):

    #setup methods to access the data above the same way have been accessed on the main
    def setUp(self):
        self.fam1 = FamilyTree()
        self.fam1.create_family(tree1)
        self.all_people = list(self.fam1.family.values())

    #creation of a method to check if correct parents were display of a person with parents present
    def test_person_with_parent(self):
        person = self.fam1.family['Gaia Three']
        parents = person.get_parents()

        self.assertEqual(parents, ['Gabriela Lions' , 'Daniel Three'], f'{parents} are not correct')

    #creation of a method to test outoput of a person without parents data inserted in the list
    def test_person_without_parent(self):
        person = self.fam1.family['Daniel Three']
        parents = person.get_parents()

        self.assertEqual(parents, [], f'{person} shoulf not have parents')

    #creation of a method to test if correct output is displayed if person is alive
    def test_if_person_alive(self):
        person = self.fam1.family['Daniel Three']
        alive = person.get_alive()

        self.assertEqual(alive, True)

    #creation of a method to test if correct output will be displayed if a person is dead
    def test_if_not_alive(self):
        person = self.fam1.family['Cristian Blackwidow']
        alive = person.get_alive()

        self.assertEqual(alive, False)

    #method to test if correct list of children will be displayed when running get_children()
    def test_children(self):
        person_name = 'Angel Raciops'
        child = self.fam1.get_children(person_name)

        expected_children = ['Cornelia Emmersohn', 'Gabriela Lions', 'Dominique Lions'] #added expected_children to make sure list was correctc

        self.assertEqual(child,expected_children , f'{person_name} should have children')

    #method to test if a person has no children
    def test_no_children(self):
        person_name = 'Cornelia Emmersohn'
        child = self.fam1.get_children(person_name)

        self.assertEqual(child,[], f'{person_name} should have no children')

    #method to test grandparents of a given person
    def test_grandchildren(self):
        person_name = 'Nick Lions'
        grandchild = self.fam1.get_grandchildren(person_name)

        expected_grandchildren = ['Gaia Three', 'Michael Three', 'Josephine Budwise']

        self.assertEqual(grandchild,expected_grandchildren , f'{person_name} should have grandchildren')

    #method to test scenario whether a poerson has no grandchildren
    def test_no_grandchildren(self):
        person_name = 'Richard Smith'
        grandchild = self.fam1.get_grandchildren(person_name)

        self.assertEqual(grandchild,[], f'{person_name} should have no grandchildren')

    #method to test list of siblings name of a given person
    def test_siblings(self):
        person_name = 'Dominique Lions'
        sibling = self.fam1.get_siblings(person_name)

        expected_siblings = ['Cornelia Emmersohn', 'Gabriela Lions']

        self.assertEqual(sibling,expected_siblings, f'{person_name} should have siblings')

    #method to test scenario where person on the list does not have siblings
    def test_no_siblings(self):
        person_name = 'Angel Raciops'
        sibling = self.fam1.get_siblings(person_name)

        self.assertEqual(sibling,[], f'{person_name} should have no siblings')


    #method to test immediate family of a given person
    def test_immediate_family(self):
        person_name = 'Gabriela Lions'
        immediate_family = self.fam1.get_immediate_family(person_name)

        expected_immediate_family = ['Gaia Three','Michael Three','Cornelia Emmersohn','Dominique Lions','Angel Raciops','Nick Lions','Daniel Three']

        self.assertEqual(immediate_family, expected_immediate_family, f'{person_name} should have immediate family')

    #method to test uncle or aunties of a person
    def test_Uncle_Auntie(self):
        person_name = 'Josephine Budwise'
        uncle_auntie = self.fam1.get_auntsOrUncles(person_name)

        expected_auntie_uncle = ['Gabriela Lions', 'Daniel Three', 'Cornelia Emmersohn', 'Otto Emmersohn']

        self.assertEqual(sorted(uncle_auntie), sorted(expected_auntie_uncle), f'{person_name} should have uncle auntie') #had to sort the names because it was bugging at every test run

    #method to check scenario where uncle or aunite is not present in the list of given names
    def test_person_without_Uncle_Auntie(self):
        person_name = 'Nick Lions'
        uncle_auntie = self.fam1.get_auntsOrUncles(person_name)

        self.assertEqual(uncle_auntie, [], f'{person_name} should not have uncle or auntie')

    #method to test cousin of given person
    def test_cousin(self):
        person_name = 'Michael Three'
        cousin = self.fam1.get_cousin(person_name)

        expected_cousin = ['Josephine Budwise']

        self.assertEqual(cousin, expected_cousin, f'{person_name} should have cousin')

    #method to test scenario where cousin is not present
    def test_person_without_cousin(self):
        person_name = 'Cornelia Emmersohn'
        cousin = self.fam1.get_cousin(person_name)

        self.assertEqual(cousin, [], f'{person_name} should not have cousin')

    #method to check extended family of a person
    def extended_family(self):
        person_name = 'Josephine Budwise'
        extended_family = self.fam1.get_extended_family(person_name)

        expected_extended_family = ['Dominique Lions', 'Aniket Budwise', 'Daniel Three', 'Gabriela Lions', 'Cornelia Emmersohn', 'Gaia Three', 'Michael Three']

        self.assertEqual(extended_family, expected_extended_family, f'{person_name} should have extended family')

    #method to check number of children
    def test_number_children(self):
        people = self.all_people

        child_count = self.fam1.number_of_children(people)

        #creation of a dictionary with expected output including all the people in the list
        expected_count = {
            'Angel Raciops': 3,
            'Nick Lions': 3,
            'Gabriela Lions': 2,
            'Dominique Lions': 1,
            'Daniel Three': 2,
            'Aniket Budwise': 1,
            'Cornelia Emmersohn': 0,
            'Gaia Three': 0,
            'Michael Three': 0,
            'Cristian Blackwidow': 0,
            'Richard Smith': 0,
            'Josephine Budwise': 0,
            'Otto Emmersohn': 0,
        }

        self.assertEqual(child_count, expected_count,'child count is not correct ')

    #method to test average number of children within all the given list of people
    def test_average_children(self):
        people = self.all_people
        average = self.fam1.average_number_children(people)

        expected_average = 0.9230769230769231

        self.assertEqual(average, expected_average, 'average is not correct')

    #method to check the average age of death where only dead people are taken into consideration
    def test_average_age_death(self):
        people = self.all_people
        average_age_death = self.fam1.average_death_age(people)

        expected_average_age_death = 19.5

        self.assertEqual(average_age_death, expected_average_age_death, 'average_age_death is not correct')

if __name__ == '__main__':
    unittest.main()

