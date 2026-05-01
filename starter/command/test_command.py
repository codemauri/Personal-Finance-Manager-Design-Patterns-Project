import unittest
from command.command import CommandManager, ApplyTransactionCommand
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from balance.balance import Balance

class TestCommandPattern(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_apply_transaction_execute(self):
        remote = CommandManager()
        balance = self.balance
        transaction = Transaction(150, TransactionCategory.INCOME)
        remote.execute_command(ApplyTransactionCommand(balance, transaction))
        self.assertEqual(balance.get_balance(), 150)

    def test_apply_transaction_undo(self):
        remote = CommandManager()
        balance = self.balance
        transaction = Transaction(200, TransactionCategory.INCOME)
        remote.execute_command(ApplyTransactionCommand(balance, transaction))
        remote.undo_last()
        self.assertEqual(balance.get_balance(), 0)

    def test_no_command(self):
        remote = CommandManager()
        remote.undo_last()
        self.assertEqual(len(remote._history), 0)        

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)