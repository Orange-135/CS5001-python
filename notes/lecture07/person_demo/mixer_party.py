from person import Person

def main():
    my_person1 = Person("Marge Simpson", 32)
    my_person2 = Person("Asterix the Gaul", 55)
    another_guest = Person("Lsia Organa", 25)

    my_person1.introduce_self()
    my_person2.introduce_self()
    another_guest.introduce_self()

    my_person1.befriend(my_person2)
    my_person1.befriend(another_guest)

    my_person1.introduce_self()
    my_person2.introduce_self()



main()