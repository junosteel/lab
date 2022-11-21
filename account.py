class Account:
    """
    A class representing details for an account object
    """
    def __init__(self, name: str) -> None:
        """
        Constructor to create the default state of an account object
        :param name: Name of the person who owns account
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Method to add specified amount to an account and indicate success or failure
        :param amount: Money being added
        :return: True on success, False on failure
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Method to subtract specified amount to an account and indicate success or failure
        :param amount: Money being removed
        :return: True on success, False on failure
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Method to access an account's balance
        :return: Account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Method to access an aacount's name
        :return: Account name
        """
        return self.__account_name
