class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def print_name(self):
        print(self.fname, self.lname)

class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.grad_year = year
    def welcome(self):
        print("welcome", self.fname, self.lname, "class of", self.grad_year)


p1= student("sam", "anders", 2023)
p1.print_name()
p1.welcome()


