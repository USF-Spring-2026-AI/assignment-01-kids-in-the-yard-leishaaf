
"""
Person class
Responsible for keeping details of each person simulated in our model
Each member of the family tree is an instance of person class
"""
class Person:
    def __init__(self):
        self.year_born = None
        self.year_died = None
        self.first_name = None
        self.last_name = None
        self.full_namme = None
        self.partner = None
        self.children = []

    def set_year_born(self, year_born):
        self.year_born = year_born
    
    def set_year_died(self, year_died):
        self.year_died = year_died
   
    def set_first_name(self, first_name):
        self.first_name = first_name
    
    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_partner(self, partner):
        self.partner = partner

    def set_children(self, children):
        self.children = children

    def get_year_born(self):
        return self.year_born
    
    def get_year_died(self):
        return self.year_died
    
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_partner(self):
        return self.partner
    
    def get_children(self):
        return self.children
    
    def print(self):
        partner_name = "None"
        if self.partner != None:
            partner_name = self.partner.get_first_name() + " "  + self.partner.get_last_name()
        print(f"Name: {self.first_name} {self.last_name} Year Born: {self.year_born} Year died: {self.year_died} Partner: {partner_name} Children: {self.children} ")