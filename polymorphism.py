class India():
    def capital(self):
        print("New delhi is the capital of india")
    def language(self):
        print("Hindi is most widely spoken languages in india")
    def type(self):
        print("India is a developing country.\n")

class usa():
    def capital(self):
        print("Washington,DC is the capital of USA")

    def language(self):
        print("English is primary language of USA")

    def type(self):
        print("USA is a developing country.\n")
obj_ind=India()
obj_usa=usa()

for country in(obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()





