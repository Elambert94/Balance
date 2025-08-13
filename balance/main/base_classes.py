class Account():
    def __init__(self, account_name : str, account_owner : 'Person'):
        """Constructor for the account class

        :param account_name: The account name.
        :type account_name: str
        :param account_owner: Owner of the account.
        :type account_owner: Person
        """
        self.account_name = account_name
        self.account_owner = account_owner
        self.incomes : list['Income'] = []
    
    def get_account_name(self) -> str:
        """Retrieve the account name.

        :return: The account name.
        :rtype: str
        """
        return self.account_name
    
    def set_account_name(self, name : str):
        """Sets the account name for the account.

        :param name: Intended name for the account.
        :type name: str
        """
        self.account_name = name
    
    def get_account_owner(self) -> 'Person':
        """Retrieve the owner of the account.

        :return: The account owner.
        :rtype: Person
        """
        return self.account_owner
    
    def set_account_owner(self, Person):
        """Sets the account owner of the account.

        :param Person: New owner of the account.
        :type Person: Person
        """
        self.account_owner = Person

    def add_income(self, name : str, amount : float, date : str):
        """Add a new income for the account.

        :param name: Name of the income.
        :type name: str
        :param amount: Amount to assign to the income.
        :type amount: float
        :param date: Value (e.g. 1, 31, TBD) which the income arrives.
        :type date: str
        """
        self.incomes.append(Income(name, amount, self, date))

    def remove_income(self, income : 'Income'):
        """Remove an income from the income list.

        :param income: Income to remove.
        :type income: Income
        """
        self.incomes.remove(income)

    def get_incomes(self):
        """Retrieve all incomes. 

        :return: The list of incomes.
        :rtype: list[Income]
        """
        return self.incomes

class Income():
    def __init__(self, name : str, amount : float, account : Account, date : str):
        """Constructor for the income class.

        :param name: Name of the income (e.g Salary).
        :type name: str
        :param amount: The income amount.
        :type amount: float
        :param account: The associated account for the income.
        :type account: Account
        """
        self.name = name
        self.amount = amount
        self.account = account
        self.date = date

    def get_income_name(self) -> str:
        """Retrieve the name of the income.

        :return: Returns income name.
        :rtype: str
        """
        return self.name
    
    def get_income_amount(self) -> float:
        """Retrieve the amount of income

        :return: Returns the income amount.
        :rtype: float
        """
        return self.amount
    
    def get_income_date(self)-> str:
        """Retrieve the income date. 

        :return: Returns the income date.
        :rtype: str
        """
        return self.date
    
    def get_account(self) -> Account:
        """Retrieve the account which the income is assigned.

        :return: The assigned account.
        :rtype: Account
        """
        return self.account
    
    def set_account(self, Account):
        """Set a new account for the income.

        :param Account: The new account to assign.
        :type Account: Account
        """
        self.account = Account
    
    def set_income_name(self, income_name : str):
        """Set a new name for the income.

        :param income_name: The new name of the income.
        :type income_name: str
        """
        self.name = income_name

    def set_income_amount(self, income_amount : float):
        """Set a new amount for the income.

        :param income_amount: The new amount to set.
        :type income_amount: float
        """
        self.amount = income_amount
    
    def set_income_date(self, income_date : str):
        """Set a new date for the income

        :param income_date: The new date to set.
        :type income_date: str
        """
        self.date = income_date

class Person():
    """Base class for a person.
    """
    def __init__(self, name : str):
        """Constructor for the person class.

        :param name: Name of the person.
        :type name: str
        """

        # Attributes 
        self.name = name
        self.accounts : list[Account] = []
    
    def get_name(self)->str:
        """Gets the name of person

        :return: Name of the person
        :rtype: str
        """
        return self.name
    
    def get_accounts(self) -> list['Account']:
        """Retrieve a list of the accounts owned by the person.

        :return: List of accounts owned.
        :rtype: list[Account]
        """
        return self.accounts
    
    def get_account_names(self) -> list[str]:
        """Get a list of account names for the person.

        :return: List of account names.
        :rtype: list[str]
        """
        account_names = []
        for account in self.accounts:
            account_names.append(account.get_account_name())
        return account_names
    
    def get_account_by_name(self, search_name : str) -> Account:
        """Get an account by it's name.

        :param search_name: The name of the account to retrieve.
        :type search_name: str
        :return: Returns the account matching the query, or None.
        :rtype: Account
        """
        for account in self.accounts:
            if account.get_account_name() == search_name:
                return account
        return None
    
    def set_name(self, new_name : str):
        """Set a new name for the person

        :param new_name: New name.
        :type new_name: str
        """
        self.name = new_name
    
    def create_account(self, account_name : str):
        """Create a new account for the person.

        :param account_name: The name for the account.
        :type account_name: str
        """
        self.accounts.append(Account(account_name, self))

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

Person1.create_account("JeffsAccount")
JeffsAccount = Person1.get_account_by_name("JeffsAccount")
JeffsAccount.add_income("Salary", 3000, "12")

for income in JeffsAccount.get_incomes():
    print(income.name, income.date)






