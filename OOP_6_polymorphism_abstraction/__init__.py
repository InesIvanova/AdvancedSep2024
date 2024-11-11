from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def calculate_area(self):
        return "calculating the area"
    def __str__(self):
        return "I am a rectangle"


class PaymentMethod(ABC):
    def __init__(self, recipient):
        self.recipient = recipient
        
    @property
    def recipient(self):
        return 
    
    @recipient.setter
    def recipient(self, value):
        pass
    @abstractmethod
    def pay(self):
        pass


class BankPayment(PaymentMethod):
    def __init__(self, recipient, date_of_payment):
        super().__init__(recipient)
        self.date_of_payment = date_of_payment
        
    @property
    def date_of_payment(self):
        return 
    
    @date_of_payment.setter
    def date_of_payment(self, value):
        pass
    def pay(self):
        return "pay via bank"


class CardPayment(PaymentMethod):
    def pay(self):
        return "pay via card"


s = Rectangle()
print(s)