class Person():
    """Base class for a person.
    """
    def __init__(self, name : str, accounts = None, incomes = None):
        """Constructor for the person class.
        """
        # Attributes 
        self.name = name
        self.accounts = accounts
        self.incomes = incomes
    
    def get_name(self)->str:
        """Gets the name of person

        :return: Name of the person
        :rtype: str
        """
        return self.name
    
    def set_name(self, new_name : str):
        """Set a new name for the person

        :param new_name: New name.
        :type new_name: str
        """
        self.name = new_name
    
class PersonManager():
    def __init__(self, people : list[Person] = []):
       """Constructor for the Person Manager class

       :param people: List of people.
       :type people: list[Person]
       """

       # Attributes
       self.people = people
   
    def get_people(self)->list[Person]:
        """Get the list of managed people.

        :return: List of People.
        :rtype: list[Person]
        """
        return self.people
    
    def get_person_by_name(self, person_name : str):
        """Get a person from the manager by their name

        :param person_name: Name of the person to retrieve.
        :type person_name: str
        :return: Matched person.
        :rtype: Person
        """
        for person in self.people:
            if person.get_name() == person_name:
                return person
    
    def add_person(self, Person):
        """Add an existing person to the manager.

        :param Person: Reference to the person.
        :type Person: Person
        """
        self.people.append(Person)

    def add_person_by_name(self, person_name : str):
       """Initialise a new person using the manager by providing their name.

       :param name: Name of the person to create.
       :type name: str
       """
       person = Person(person_name)
       self.people.append(person)

    def remove_person(self, Person):
        """Remove a person from the manager.

        :param Person: Reference to the person. 
        :type Person: Person
        """
        self.people.remove(Person)

    def remove_person_by_name(self, person_name : str):
        """Remove a person by their name

        :param person_name: The persons name.
        :type person_name: str
        """
        for person in self.people:
            if person.get_name() == person_name:
                self.people.remove(person)
                break
       
       
       
Manager = PersonManager()
Person1 = Person("Jeff")
Manager.add_person(Person1)
Manager.add_person_by_name("Clinton")
Manager.add_person_by_name("Wilhelm")
Manager.remove_person(Person1)
People = Manager.get_people()
for person in People:
    print(person.get_name())