import pytest
from account import *

class MyTestCase:

    def setUp(self):
        self.name = Account('name')
    def tearDown(self):
        del self.name

    def test_init(self):
        assert self.name.get_name() == 'name'
        assert self.name.get_balance() == 0

    def test_deposit(self):
        assert self.name.deposit(-1) == False
        assert self.name.get_balance() == 0
        assert self.name.deposit(0) == False
        assert self.name.get_balance() == 0
        assert self.name.deposit(1) == True
        assert self.name.get_balance() == 1

    def test_withdraw(self):
        assert self.name.withdraw(-1) == False
        assert self.name.get_balance() == 0
        assert self.name.withdraw(0) == False
        assert self.name.get_balance() == 0
        self.name.deposit(2)
        assert self.name.withdraw(1) == True
        assert self.name.get_balance() == 1
