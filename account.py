class Account:

    def __init__ (self,name: str) -> None:
        """ Constructor to create initial state of a person object.
        :param name: Person's account name.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self,amount: float) -> bool:
        """Function to deposit into account.
        :param: amount: The amount deposited.
        :return: False if transaction was unsuccessful and True if the transaction was successful."""
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self,amount: float) -> bool:
        """Function to withdraw from account.
        :param: amount: The amount withdrawn.
        :return: False if transaction was unsuccessful and True if the transaction was successful."""
        if amount <= 0:
            return False
        elif amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True
    def get_balance(self) -> float:
        """ Function to return balance of the account.
        :return: return account balance. """
        return self.__account_balance
    def get_name(self) -> str:
        """ Function to return name on the account.
                :return: return account name. """
        return self.__account_name

