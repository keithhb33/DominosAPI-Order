from pizzapi import *
from pprint import pprint
import sys

customer = Customer('Donald', 'Trump', 'Donaldtrump@gmail.com', '1111111111')
address = Address('1234 address drive', 'san jose', 'ca', '90001')

store = address.closest_store()
menu = store.get_menu()

confirmation = input("Do you want to order pizza? ")
if confirmation.lower() == "yes" or confirmation.lower() == "y":
    print(
        "Item List:\n#1 - Small Hand Tossed Pizza - $9.49\n#2 - Medium Hand Tossed Pizza - $11.99\n#3 - Small Thin "
        "Pizza - $9.49\n#4 - Medium Thin Pizza - $11.99\n")

    number_of_items = int(input("How many items are you ordering? "))
    order = Order(store, customer, address)
    for i in range(number_of_items):
        order_item = str(input("Menu Item #"))
        if order_item.lower() == "one" or str('1'):
            order.add_item('10SCREEN')
        elif order_item.lower() == "two" or str('2'):
            order.add_item('12SCREEN')
        elif order_item.lower() == "three" or str('3'):
            order.add_item('10THIN')
        elif order_item.lower() == "four" or str('4'):
            order.add_item('12THIN')
        elif order_item.lower() != "four" or order_item.lower() != "three" or order_item.lower() != "two" or order_item.lower() != "one" or order_item.lower() != "4" or order_item.lower() != "3" or order_item.lower() != "2" or order_item.lower() != "1":
            print("Choose one of the options above. Ending program")
            sys.exit(0)
        else:
            print("Choose one of the options above. Ending program")
            sys.exit(0)

    card = PaymentObject('CREDITCARDNUMBER', 'EXP', 'CVV', 'ZIPCODE')
    pprint(vars(order))
    print("Ordering...")
    order.pay_with(card)
    print("Order Confirmed!")
    input("")
else:
    print("Order Canceled")
    input("")
    sys.exit(0)
