# balance.py

from transaction.transaction_category import TransactionCategory
from transaction import transaction

class Balance:
    """Singleton to track the balance."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance    

    def __init__(self):
        """Initialize the balance. Prevent direct instantiation."""
        if not hasattr(self, "balance"):
            self.balance = 0
            self._observers = []

    @classmethod
    def get_instance(cls):
        return Balance()

    def reset(self):
        """Reset the net balance to zero."""
        self.balance = 0
        self._observers = []

    def add_income(self, amount):
        """Add income to the balance."""
        self.balance += amount

    def add_expense(self, amount):
        """Subtract expense from the balance."""
        self.balance -= amount
        
    def apply_transaction(self, transaction: transaction):
        """
        Apply a Transaction object to update the balance.

        Args:
            transaction (Transaction): The transaction to apply.
        """
        if transaction.category == TransactionCategory.INCOME:
            self.add_income(transaction.amount)
        elif transaction.category == TransactionCategory.EXPENSE:
            self.add_expense(transaction.amount)
        else:
            raise ValueError("Invalid Category") 
        self.notify(transaction)           

               

    def get_balance(self):
        """Get the current net balance."""
        return self.balance
        

    def summary(self):
        """Return a summary string of the net balance."""
        return f"Current balance: ${self.balance}"
    
    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def notify(self, transaction):
        for observer in self._observers:
            observer.update(self.balance, transaction)        
