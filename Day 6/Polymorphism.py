# Parent class
class Payment:
    def pay(self):
        print("Payment method selected")


# Child class GooglePay
class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay")


# Child class PhonePe
class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe")


# Child class CreditCard
class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")


# Creating objects
p = Payment()
gpay = GooglePay()
phonepe = PhonePe()
card = CreditCard()

# Calling pay() method
p.pay()
gpay.pay()
phonepe.pay()
card.pay()