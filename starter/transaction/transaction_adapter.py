# transaction_adapter.py

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory

class TransactionAdapter:
    def __init__(self, external_transaction):
        self.external_transaction = external_transaction

    def to_transaction(self):
        """Convert an external transaction to a standard Transaction."""
        amount = self.external_transaction.amount
        type = self.external_transaction.typ
        if type == "income":
            return Transaction(amount, TransactionCategory.INCOME)
        elif type == "expense":
            return Transaction(amount, TransactionCategory.EXPENSE)

        
        
