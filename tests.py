import unittest
from main import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount(initial_balance=5)
        account.deposit(50)
        # expected_result = account.get_balance()
        self.assertEqual(account.get_balance(), 55) # self.assertEqual(account.get_balance(), expected_result)

    def test_deposit_zero_amount(self):
        account = BankAccount(initial_balance=5)
        with self.assertRaises(ValueError):
            account.deposit(0)

    def test_deposit_negative_amount(self):
        account = BankAccount(initial_balance=5)
        with self.assertRaises(ValueError):
            account.deposit(-20)

    def test_withdraw_more_than_could(self):
        account = BankAccount(initial_balance=100)
        with self.assertRaises(ValueError):
            account.withdraw(150)

    def test_withdraw_negative_amount(self):
        account = BankAccount(initial_balance=5)
        with self.assertRaises(ValueError):
            account.deposit(-20)

    def test_withdraw(self):
        account = BankAccount(initial_balance=100)
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50)

    def test_transfer(self):
        account = BankAccount(initial_balance=100)
        other_account = BankAccount(initial_balance=50)
        account.transfer(other_account, 5)
        self.assertEqual(other_account.get_balance(), 55)

    def test_transfer_zero(self):
        account = BankAccount(initial_balance=100)
        other_account = BankAccount(initial_balance=50)
        with self.assertRaises(ValueError):
            account.transfer(other_account, 0)

    def test_transfer_negative_amount(self):
        account = BankAccount(initial_balance=100)
        other_account = BankAccount(initial_balance=50)
        with self.assertRaises(ValueError):
            account.transfer(other_account, -40)

if __name__ == "__main__":
    unittest.main()





