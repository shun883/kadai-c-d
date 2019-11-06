class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        print(self.first_name, self.family_name)


# c-1
# ken = Customer(first_name='Ken', family_name='Tanaka')
# ken.full_name()
#
# tom = Customer(first_name='Tom', family_name='Ford')
# tom.full_name()

# c-2
ken = Customer(first_name='Ken', family_name='Tanaka', age=15)
age = ken.age
print(age)
