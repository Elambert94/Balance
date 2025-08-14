class Account():
    def __init__(self, account_name : str, account_owner : 'Person'):
        """Constructor.

        :param account_name: The account name.
        :type account_name: str
        :param account_owner: The owner of the account.
        :type account_owner: Person
        """
        self.account_name = account_name
        self.account_owner = account_owner
        self.incomes : list['Income'] = []
        self.transfers_in = list['TransferIn']
        self.transfers_out = list['TransferOut']
        self.bills = list['Bill']
    
    def get_account_name(self) -> str:
        """
        :return: The account name.
        :rtype: str
        """
        return self.account_name
    
    def set_account_name(self, name : str):
        """
        :param name: Name to set for the account.
        :type name: str
        """
        self.account_name = name
    
    def get_account_owner(self) -> 'Person':
        """
        :return: The account owner.
        :rtype: Person
        """
        return self.account_owner
    
    def set_account_owner(self, Person):
        """
        :param Person: Owner of the account to set.
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
        self.incomes.append(Income(name, amount, date, self))

    def remove_income(self, income : 'Income'):
        """
        :param income: Income to remove from the account.
        :type income: Income
        """
        self.incomes.remove(income)

    def get_incomes(self):
        """
        :return: List of incomes associated with the account.
        :rtype: list[Income]
        """
        return self.incomes

class Transaction():
    def __init__(self, name : str, amount : float, date : str, account : Account):
        """
        Constructor.
        :param name: Description name for the transaction.
        :type name: str
        :param amount: Amount for the transaction.
        :type amount: float
        :param date: Date of the transaction (e.g. "1", "31", "Variable", "As & When")
        :type date: str
        """
        
        self.name = name
        self.amount = amount
        self.date = date
        self.account = account

    def get_name(self) -> str:
        """
        :return: The transaction name.
        :rtype: str
        """
        return self.name
    
    def get_amount(self)->float:
        """
        :return: The transaction amount. 
        :rtype: float
        """
        return self.amount
    
    def get_date(self) -> str:
        """
        :return: The transaction date.
        :rtype: str
        """
        return self.date
    
    def get_account(self)->Account:
        """
        :return: The account owning the transaction.
        :rtype: Account
        """
        return self.account
    
    def set_name(self, new_name : str):
        """
        :param new_name: Name to set.
        :type new_name: str
        """
        self.name = new_name
    
    def set_amount(self, new_amount : float):
        """
        :param new_amount: The amount to set for the transaction.
        :type new_amount: float
        """
        self.amount = new_amount
    
    def set_date(self, new_date : str):
        """
        :param new_date: The new date to set for the transaction.
        :type new_date: str
        """
        self.date = new_date
    
    def set_account(self, Account : Account):
        """
        :param Account: The new account to assign.
        :type Account: Account
        """
        self.account = Account

class Income(Transaction):
    def __init__(self, name : str, amount : float, date : str, account : Account):
        """
        Constructor.
        """
        super().__init__(name = name, amount = amount, date = date, account=account)

class TransferOut(Transaction):
    def __init__(self, name : str, amount : float, date : str, account : Account, target_account : 'Account'):
        super().__init__(name = name, amount = amount, date = date, account=account)    
        """
        Constructor.
        :param target_account: The account receiving the funds.
        :type target_account: Account
        """
        self.target_account = target_account

class TransferIn(Transaction):
    def __init__(self, name : str, amount : float, date : str, account : Account, transferred_by : 'Account'):
        """
        Constructor.
        :param transferred_by: The account from which the funds were transferred.
        :type transferred_by: Account
        """
        super().__init__(name = name, amount = amount, date = date, account=account)  
        
        self.transferred_by = transferred_by

class Bill(Transaction):
    def __init__(self, name : str, amount : float, date : str, account : Account, category : 'Category'):
        """
        :param category: The assigned category for the transaction
        :type category: Category
        """
        super().__init__(name, amount, date, account)

        self.category = category

    def get_category(self) -> 'Category':
        """
        :return: The category assigned to the bill.
        :rtype: Category
        """
        return self.category
    
    def set_category(self, new_category : 'Category'):
        """
        :param new_category: The new category to assign to the bill.
        :type new_category: Category
        """
        self.category = new_category

class Person():
    def __init__(self, name : str):
        """Constructor.
        :param name: Name of the person.
        :type name: str
        """

        # Attributes 
        self.name = name
        self.accounts : list[Account] = []
    
    def get_name(self)->str:
        """
        :return: Name of the person.
        :rtype: str
        """
        return self.name
    
    def get_accounts(self) -> list['Account']:
        """
        :return: List of accounts owned by the person.
        :rtype: list[Account]
        """
        return self.accounts
    
    def get_account_names(self) -> list[str]:
        """
        :return: List of account names.
        :rtype: list[str]
        """
        account_names = []
        for account in self.accounts:
            account_names.append(account.get_account_name())
        return account_names
    
    def get_account_by_name(self, search_name : str) -> Account:
        """Get an account by searching it's name.

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
        """
        :param new_name: New name to set for the person.
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

class Category():
    def __init__(self, name : str, colour : tuple):
        """
        :param name: Name of the category.
        :type name: str
        :param colour: Colour to assign to the category.
        :type colour: tuple
        """
        self.name = name
        self.colour = colour

    def get_name(self):
        """
        :return: Name of the category.
        :rtype: str
        """
        return self.name
    
    def get_colour(self):
        """
        :return: Colour assigned to the category.
        :rtype: tuple
        """
        return self.colour
    
    def set_name(self, new_name):
        """
        :param new_name: The new name for the category.
        :type new_name: str
        """
        self.name = new_name
    
    def set_colour(self, new_colour):
        """
        :param new_colour: The new colour for the category.
        :type new_colour: tuple
        """
        self.colour = new_colour

class CategoryManager():
    def __init__(self):
        self.categories : list[Category] = None

    def add_category(self, name : str, colour : tuple):
        """
        Add a new category to the manager.

        :param name: Name for the category.
        :type name: str
        :param colour: Colour to assign to the category.
        :type colour: tuple
        """
        self.categories.append(Category(name, colour))
    
    def remove_category(self, category : Category):
        """
        Remove a category from the maanger.

        :param category: Category to remove.
        :type category: Category.
        """
        self.categories.remove(category)

    def get_categories(self) -> list[Category]:
        """
        :return: List of categories owned by the manager.
        :rtype: list[Category]
        """
        return self.categories





