class MyClass:

    def __init__(self, full_name):
        self.full_name=full_name

    def displayName(self):
        print("Le nom complet est :",self.full_name)


class OtherClass:

    def __init__(self, first_name, name):
        self.first_name=first_name
        self.name=name

    def display_name(self):
        print(f"Nom complet : {self.first_name} {self.name}")

full_name = "fabien le berre"
testmyclass = MyClass(full_name)

first_name = "fabien"
last_name = "le berre"
testoctheclass = OtherClass(first_name, last_name)

testmyclass.displayName()
testoctheclass.display_name()