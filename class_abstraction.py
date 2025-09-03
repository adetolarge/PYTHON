from abc import ABC, abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def make_payment(self, amount):
        pass
#Subclass for CreditCard
class CreditCard(PaymentMethod):
    def authenticate(self):
        print("Authenticating credit card details...")

    def make_payment(self, amount):
        print(f"print creidt card payment fo {amount}.")

#subclass for Pypal
class PayPal(PaymentMethod):
    def authenticate(self):
      print("Authenticating Paypal account")

    def make_payment(self, amount):
        print(f"processing PayPal payment fo {amount}.")

#Funcation to process payment
def process_payment(payment_method: PaymentMethod, amount):
    payment_method.authenticate()
    payment_method.make_payment(amount)

#usage example
payment = CreditCard()
process_payment(payment, 150)

payment = PayPal()
process_payment(payment, 150)