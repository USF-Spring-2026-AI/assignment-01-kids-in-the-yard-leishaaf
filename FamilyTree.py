from PersonFactory import PersonFactory
from Person import Person

class FamilyTree:
    """ FamilyTree is the driver and keeps reference to ALL person instances """
    def __init__(self, person_one, person_two):
        self.person_one = person_one
        self.person_two = person_two
        self.tree = [self.person_one, person_two]
        self.direct_descendants = [self.person_one, self.person_two] # keep track of direct descendants 
        self.tree_count = 2 # we start off the tree with two people
        self.duplicates = []

    def generate_tree(self, person_fac):
        """ Generates new people given PersonFactory() object """
        print("Generating family tree...")
        queue = self.tree.copy() # make the tree list a queue
        while queue:
            if person_fac.terminate_generation:  # check for going over year 2120 in generation
                break
            person = queue.pop(0) # pop from top
            if person.get_year_born() >= 2120:
                break # we've reached year 2120, terminate generation
            if person in self.direct_descendants: # if person is a direct descendant then curr generation being created will also be descendants
                person_fac.set_is_descendant(True)
                person_fac.set_person_one_lastname(self.person_one.get_last_name())
                person_fac.set_person_two_lastname(self.person_two.get_last_name())
            else:
                person_fac.set_is_descendant(False)
            if person.get_partner() is None:
                if person_fac.calc_marriage(person.get_year_born()):
                    partner = person_fac.generate_partner(person, person.get_year_born())
                    queue.append(partner)
                    self.tree.append(partner) # add persons partner if there got oen
                    # else partner will remain set to None
            if not person.get_children():
                children_amount = person_fac.calc_children(person, person.get_year_born())
                person_fac.generate_children(person, person.get_year_born(), children_amount) # generate kids and sets children attribute to new person and their partner if they exist
            for child in person.get_children(): # add all children
                if child not in self.tree:
                    queue.append(child)
                    self.tree.append(child)
                    if (child.get_last_name() == self.person_one.get_last_name()) or (child.get_last_name() == self.person_two.get_last_name()):
                        self.direct_descendants.append(child)
          
    def get_tree_count(self):
        return len(self.tree)
    
    def populate_duplicate_list(self):
        """ Populates the duplicate names list in the tree """
        my_map = {}
        for person in self.tree:
            full_name = person.get_first_name() + " " + person.get_last_name()
            my_map[full_name] = my_map.get(full_name, 0)+1 # Gemini Google search for syntax ref
            if my_map[full_name] == 2:
                self.duplicates.append(full_name)

    def get_duplicate_names(self):
        return self.duplicates
    
    def print_people_by_decade(self):
        """ Prints people in tree by decade given the spec """
        # Used Claude to assist me with this method to make it more efficient/clean
        decade_counts = {} # make a dictionary to get all people born in the their respective decades
        for person in self.tree: 
            decade = (person.year_born // 10) * 10 #  the //10 part gets the first three digits and multiplying it gives us the 0 at the end so 1971 becomes 197 * 10 = 1970
            decade_counts[decade] = decade_counts.get(decade, 0) + 1 # looks for the decade in decade count map and increment its freq
        for decade in sorted(decade_counts.keys()): # sorts the decades by ascending order so looks cleaner while printing
            print(f"{decade}: {decade_counts[decade]}")

    def respond(self):
        """ Prints menu and acts accordingly given user input """
        self.populate_duplicate_list()
        user_in = ""
        while user_in != "E":
            print(f"Are you interested in:\n(T)otal number of people in the tree by (D)ecade")
            print(f"(N)ames duplicated")
            print(f"(E)nd")
            user_in = input("> ").strip().upper() # convert to upper and strip just in case
            if user_in == 'T':
                print(f"The tree contains {self.get_tree_count()} people total")
            if user_in == 'N':
                duplicates = self.get_duplicate_names()
                print(f"There are {len(duplicates)} duplicate names in the tree:")
                for name in duplicates:
                    print(f"* {name}")
            if user_in == 'D':
                self.print_people_by_decade()
                
def main():
    person_fac = PersonFactory()
    person_one = person_fac.get_person(1950) # first two people
    person_two = person_fac.get_person(1950)
    person_one.set_partner(person_two) # set them as partners
    person_two.set_partner(person_one)
    family_tree = FamilyTree(person_one, person_two)
    family_tree.generate_tree(person_fac) # start generation
    family_tree.respond()

if __name__ == "__main__":
    main()