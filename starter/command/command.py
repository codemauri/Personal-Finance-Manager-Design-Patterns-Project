from balance.balance import Balance
from abc import ABC, abstractmethod
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory

# Step 1: Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass


# Step 2: Concrete Commands
class ApplyTransactionCommand(Command):
    # DONE: Implement constructor and execute
    def __init__(self, balance: Balance, transaction: Transaction):
        self.balance = balance
        self.transaction = transaction
        
    def execute(self):
        self.balance.apply_transaction(self.transaction)
    
    def undo(self):
        if self.transaction.category == TransactionCategory.INCOME:
            transaction = Transaction(self.transaction.amount, TransactionCategory.EXPENSE)
            self.balance.apply_transaction(transaction)
        elif self.transaction.category == TransactionCategory.EXPENSE:
            transaction = Transaction(self.transaction.amount, TransactionCategory.INCOME)
            self.balance.apply_transaction(transaction)

# Invoker
class CommandManager:
    def __init__(self):
        self._history = []

    def execute_command(self, command: Command):
        command.execute()
        self._history.append(command)

    def undo_last(self):
        if self._history:
            command = self._history.pop()
            command.undo()       





