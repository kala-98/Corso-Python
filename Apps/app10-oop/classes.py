
class User:
    def __init__(self, name, birthyear):
        self.name = name 
        self.birthyear = birthyear
    
    def get_name(self):
        x = self.name
        return x.upper()

    def get_age(self, current_year):
        age = current_year - self.birthyear
        print(age)


user1 = User("Matteo", 15)
print(user1.get_name())
