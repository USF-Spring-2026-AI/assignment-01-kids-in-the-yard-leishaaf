from PersonFactory import PersonFactory
from Person import Person
"""
FamilyTree is the driver and keeps reference to ALL person instances
"""

# have methods for generating family tree and 
# responding to user queries 


# function to get the total count of people in tree
# total number of people in tree by year (level?)
# function to get the duplicate names 
class FamilyTree:
    def __init__(self, person_one, person_two):
        self.person_one = person_one
        self.person_two = person_two
        self.tree = [self.person_one, person_two]
        self.direct_descendants = [self.person_one, self.person_two] # keep track of direct descendants 
        self.tree_count = 2 # we start off the tree with two people
        self.names_duplicated = 0

    def generate_tree(self, person_fac):
        print("Generating family tree...")
        queue = self.tree.copy() # make the tree list a queue
        while queue:
            person = queue.pop()
            person.print()
            if person in self.direct_descendants:
                person_fac.set_is_descendant(True, self.person_one.get_last_name(), self.person_two.get_last_name())
            else:
                person_fac.set_is_descendant(False)
            # new_person = person_fac.get_person(person.get_year_born()) # year parent is born
            if person.get_year_born() >= 2120:
                break # we've reached year 2120, terminate generation
            if new_person.get_last_name() == self.person_one.get_last_name() or new_person.get_last_name() == self.person_two.get_last_name(): # direct descendant
                self.direct_descendants.append(new_person) # add to direct descendant list
            if new_person.get_partner() != None:
                if person_fac.calc_marriage(new_person.get_year_born()):
                    person_fac.generate_partner(new_person, new_person.get_year_born())
                    self.tree.append(new_person.get_partner()) # add persons partner if there got oen
                    # else partner will remain set to None
            children_amount = person_fac.calc_children(new_person, new_person.get_year_born())
            if  children_amount != 0: # if person's children rate != 0, generate kids
                person_fac.generate_children(new_person, new_person.get_year_born(), children_amount) # generate kids and sets children attribute to new person and their partner if they exist
            if new_person.get_children() != []:
                self.tree.append(new_person.get_children()) # add all children to the queue
                
    def get_tree_count(self):
        return len(self.tree)
    
    def get_duplicate_names(self):
        pass

    def respond(self):
        pass
    """
    main idea, generate a family tree starting with two people year by year
    and before every new person generates, check for a few rules first
    """


def main():
    # pass
    # person_one = Person("Charles", "Smith", "Mary Miller", None, 1950)
    person_fac = PersonFactory()
    person_one = person_fac.get_person(1950) # first two people
    person_two = person_fac.get_person(1950)
    person_one.set_partner(person_two) # set them as partners
    person_two.set_partner(person_one)
    family_tree = FamilyTree(person_one, person_two)
    family_tree.generate_tree(person_fac) # start generation
    # person.get_person(2067)

    #  ADD USER INPUT AND INTERACTION

if __name__ == "__main__":
    main()