class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f'{self.first_name} {self.family_name}'


    def entry_fee(self):
        if self.age <= 3:
            return '無料'
        if self.age < 20:
            return 1000
        if self.age < 65:
            return 1500
        if self.age < 75:
            return 1200
        return 500

    def info_csv(self, sep=','):
        info_list = [self.full_name(), str(self.age), str(self.entry_fee())]
        return sep.join(info_list)


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
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken_fee = ken.entry_fee()
# print(ken_fee)
#
# tom = Customer(first_name="Tom", family_name="Ford", age=57)
# tom_fee = tom.entry_fee()
# print(tom_fee)
#
# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu_fee = ieyasu.entry_fee()
# print(ieyasu_fee)

# c-4
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken_info = ken.info_csv()
# print(ken_info)

# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# tom_info = tom.info_csv()  # "Tom Ford,57,1500" という値を返す
# print(tom_info)

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu_info = ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
# print(ieyasu_info)

# c-5
# ikura = Customer(first_name='ikura', family_name='Namino', age=2)
# print(ikura.entry_fee())

# c-6
# namihei = Customer(first_name='Namihei', family_name='Isono', age=76)
# print(namihei.entry_fee())

# c-7
ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
info_tap = ken.info_csv('\t')  # "en Tanaka 15  1000" という値を返す
print(info_tap)

tom = Customer(first_name="Tom", family_name="Ford", age=57)
csv = tom.info_csv('\t')  # "Tom Ford   57  1500" という値を返す
print(csv)

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
csv = ieyasu.info_csv('\t')  # "Ieyasu  Tokugawa    73  1200" という値を返す
print(csv)

# c-8
csv = ken.info_csv(sep='|')  # "Ken Tanaka|15|1000" という値を返す
print(csv)
csv = tom.info_csv(sep='|')  # "Tom Ford|57|1500" という値を返す
print(csv)
csv = ieyasu.info_csv(sep='|')  # "Ieyasu Tokugawa|73|1200" という値を返す
print(csv)
