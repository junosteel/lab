from account import *

class Test:
    def test_init(self):
        self.a1 = Account('Jane')
        self.a2 = Account('John')

        assert self.a1.get_name() == 'Jane'
        assert self.a1.get_balance() == 0
        assert self.a2.get_name() == 'John'
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        self.a1 = Account('Jane')
        self.a2 = Account('John')

        assert self.a1.deposit(-50) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(50) is True
        assert self.a1.get_balance() == 50

    def test_withdraw(self):
        self.a1 = Account('Jane')
        self.a2 = Account('John')

        assert self.a1.withdraw(-50) is False
        assert self.a1.get_balance() == 0

        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 0

        assert self.a1.withdraw(50) is False
        assert self.a1.get_balance() == 0

        assert self.a1.deposit(50) is True
        assert self.a1.get_balance() == 50
        assert self.a1.withdraw(25) is True
        assert self.a1.get_balance() == 25
