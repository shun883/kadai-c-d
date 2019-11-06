class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        print(self.first_name, self.family_name)

    def entry_fee(self):
        if self.age < 20:
            return 1000
        if self.age < 65:
            return 1500
        return 1200

# c-1
# ken = Customer(first_name='Ken', family_name='Tanaka')
# ken.full_name()
#
# tom = Customer(first_name='Tom', family_name='Ford')
# tom.full_name()

# c-2
# ken = Customer(first_name='Ken', family_name='Tanaka', age=15)
# ken_age = ken.age
# print(ken_age)
#
# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# tom_age = tom.age
# print(tom_age)
#
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu_age = ieyasu.age
# print(ieyasu_age)

# c-3
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken_fee = ken.entry_fee()
print(ken_fee)

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom_fee = tom.entry_fee()
print(tom_fee)

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu_fee = ieyasu.entry_fee()
print(ieyasu_fee)
