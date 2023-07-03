class people:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(self.name, self.age, self.gender)


p1 = people('Maggie', 18, 'Female')
p1.display()
p2 = people('Jack', 26, 'Male')
p2.display()
p3 = people('Jill', 23, 'Female')
p3.display()
