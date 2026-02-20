from Person import Person
import pandas as pd
import random
"""
PersonFactory reads the data files and generated new instances of person class
"""
class PersonFactory:
    def __init__(self):
        self.read_files() # read all the files and create data frames for each
        self.terminate_generation = False
        self.is_descendant = True 
        self.person_one_lastname = None # if not set, then they're the first two people
        self.person_two_lastname = None
    
    def get_person(self, year_born):
        # got examples of boolean indexing w/pandas with gemini google search and followed exmaples
        # searched "how to query df in pandas python boolean with multiple conditions" and how to get spec col data once queried
        person = Person()
        str_year_born = str(year_born)
        str_year_born = str_year_born[:3] # get the first three digits of year
        person.set_year_born(year_born)
        person.set_year_died(self.calc_life_expectancy(year_born))
        person.set_first_name(self.generate_first_name(str_year_born))
        person.set_last_name(self.generate_last_name(str_year_born)) 
        # person.set_partner(self.generate_partner(str_year_born, year_born))
        # print(person.get_year_born())
        # print(person.get_year_died())
        # print(person.get_first_name(), " ", person.get_last_name)
        # print(person.get_last_name())
        return person
    
    def set_is_descendant(self, is_descendant, person_one_lastname, person_two_lastname):
        self.is_descendant = is_descendant 
        self.person_one_lastname = person_one_lastname
        self.person_two_lastname = person_two_lastname

    def read_files(self):
        print("Reading files...")
        # for pandas documentation https://www.w3schools.com/python/pandas/pandas_csv.asp on indexing using boolean mask
        # for printing data in df https://www.w3schools.com/python/pandas/pandas_analyzing.asp
        self.first_names_df = pd.read_csv("first_names.csv")
        self.last_names_df = pd.read_csv("last_names.csv")
        self.life_expectancy_df = pd.read_csv("life_expectancy.csv")
        self.rank_to_prob_df = pd.read_csv("rank_to_probability.csv", header=None) # header=None from ChatGpt
        self.birth_and_marriage_df = pd.read_csv("birth_and_marriage_rates.csv")

    def calc_life_expectancy(self, year_born):
        year_mask = self.life_expectancy_df['Year'] == year_born
        life_expectancy = self.life_expectancy_df.loc[year_mask, 'Period life expectancy at birth'].iloc[0] # .iloc[0] from ChatGPT to get a double version of life expectancy
        # print("res ", life_expectancy)
        beg_period = int((life_expectancy - 10) + year_born) # add life expec - 10
        end_period = int((life_expectancy + 10) + year_born) # add life expec + 10
        # print(beg_period)
        # print(end_period)
        year_died = random.randint(beg_period, end_period)
        # print("year make(olelo) ", year_died)
        return year_died
    
    def generate_first_name(self, year_born):
        decade_mask = self.first_names_df['decade'].str.contains(year_born) # selects single col from df
        first_names_filtered = self.first_names_df.loc[decade_mask, ['name', 'frequency']] # gets all the rows that is true in the bool mask
        # print(first_names_filtered)
        # ChatGpt was used for the idea of using random.choices to apply weights and Gemini google searched was used for examples on documentation
        # convert the res of filtered results organized by col to regular list so we can use random.choices() proper arg types
        chosen_names = random.choices(first_names_filtered['name'].tolist(), weights=first_names_filtered['frequency'].tolist(), k=1)#[first_names_list], [weights corresponding to first names], amount of names to chose 
        first_name = chosen_names[0] # chose the first elem in list
        # print(first_name)
        return first_name
    
    def generate_last_name(self, year_born):
        last_name = ""
        if self.is_descendant and self.person_one_lastname != None:
            last_name = random.choices([self.person_one_lastname, self.person_two_lastname], weights=None, k=1)[0]
        else: # (self.is_descendant and self.person_one_lastname == None) or not self.is_descendant -- either the first two people of not a descendant
            decade_mask = self.last_names_df['Decade'].str.contains(year_born) # selects single col from df
            lastnames = self.last_names_df.loc[decade_mask, 'LastName'].tolist() # gets all the rows that is true in the bool mask
            # print("last names ", lastnames)
            # print("rank df ", self.rank_to_prob_df)
            prob_list = self.rank_to_prob_df.iloc[0].tolist() # adding the iloc[0] from ChatGpt
            # print("prob list ", prob_list)
            chosen_names = random.choices(lastnames, weights=prob_list, k=1)
            last_name = chosen_names[0]

        # print(last_name)  
        return last_name

    def calc_marriage(self, year_born,):
        str_year_born = str(year_born)
        str_year_born = str_year_born[0:3]
        decade_mask = self.birth_and_marriage_df['decade'].str.contains(str_year_born)
        marriage_weight = self.birth_and_marriage_df.loc[decade_mask, 'marriage_rate'].iloc[0] # .iloc[0] from ChatGpt
        # print(marriage_weight)
        is_married = random.choices([True, False], weights=[marriage_weight, (1-marriage_weight)], k=1)[0]
        # print(is_married)
        return is_married

    def generate_partner(self, person, year_born):
            beg_period = int(year_born - 10)
            end_period = int(year_born + 10)
            if (year_born - 10) < 1950:
                beg_period = year_born # can't have 1950-10
            partner_year_born = random.randint(beg_period, end_period)
            # print(partner_year_born)
            str_partner_year_born = str(partner_year_born)
            str_partner_year_born = str_partner_year_born[:3]
            partner = Person() # generate a new person to be the partner for the current person
            partner.set_year_born(partner_year_born)
            partner.set_year_died(self.calc_life_expectancy(partner_year_born))
            partner.set_first_name(self.generate_first_name(str_partner_year_born))
            partner.set_last_name(self.generate_last_name(str_partner_year_born))
            partner.set_partner(person) # set the partners partner to curr person
            person.set_partner(partner)
        # make sure partner is set for both
        # curr partner = partner 
        # partner = curr
        # get first and last name, get year died and year born according to partner, children none yet
            return partner
    def calc_children(self, person, year_born):
        str_year_born = str(year_born)
        str_year_born = str_year_born[0:3]
        decade_mask = self.birth_and_marriage_df['decade'].str.contains(str_year_born)
        birth_rate = self.birth_and_marriage_df.loc[decade_mask, 'birth_rate'].iloc[0] # .iloc[0] from ChatGpt
        amount_children = random.randint(int(birth_rate - 1.5), int(birth_rate + 1.5))
        print(amount_children)
        return amount_children  # returns true if person can have a child, if not returns false
    def generate_children(self, person, year_born, children_amount):
        elder_parent_year_born = None
        if person.get_partner() != None:
            print("partner ",person.get_partner())
            elder_parent_year_born = max(person.get_year_born(), person.get_partner().get_year_born()) # get 
        else:
            elder_parent_year_born = person.get_year_born()
        beg_period = int(elder_parent_year_born + 25)
        end_period = int(elder_parent_year_born + 45)
        time_period = end_period - beg_period
        gap = int(time_period / children_amount)
        child_year = beg_period
        for i in range(children_amount):
            child = self.get_person(child_year) # is descendant is set based on parent for this generation
            children = person.get_children()
            children.append(child)
            child_year += gap
            # person.print()
            # child.print()

        # children have to be evenly distributed with elder parent
        # check if curr person has a partner and then check for their age
        # if partner then partner has to have the same children as well
        # single ppl can still have children partner just wont share with them
        if person.get_partner() != None:
            person.get_partner().set_children(person.get_children()) # set partners children so that they match

    # method that gets the year died based on reading life expectancy
    # randomly generate the length of the person's life based on the contents 
    # of the file life_expectancy.csv + or - 10 years
    # ex life expectancy of 81.51 plus or minus 10 years


    # first_names.csv based on the year born gender and freq of names found during that
    # year. 

# def main():
#     person = PersonFactory()
#     person.get_person(2067)

# if __name__ == "__main__":
#     main()
