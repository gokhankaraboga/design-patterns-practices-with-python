class Person:
    def wear_a_cloth(self) -> str:
        return "Person wore a sweater"


class PersonDecorator:
    def __init__(self, person: Person) -> None:
        self.__person = person

    def wear_a_cloth(self) -> str:
        return self.__person.wear_a_cloth() + " and also a coat"


if __name__ == "__main__":
    person = Person()
    print(person.wear_a_cloth())
    deccorated_person = PersonDecorator(person)
    print(deccorated_person.wear_a_cloth())
