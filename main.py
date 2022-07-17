from faker import Faker

from BaseContact import BaseContact
from BusinessContact import BusinessContact

fake = Faker()


def create_contacts(quantity, is_business):
    cards = []
    if is_business:
        for _ in range(quantity):
            cards.append(
                BusinessContact(name=fake.name(), private_number=fake.phone_number(), email=fake.email(),
                                job=fake.job(),
                                company=fake.company(), business_number=fake.phone_number()))
    else:
        for _ in range(quantity):
            cards.append(BaseContact(name=fake.name(), private_number=fake.phone_number(), email=fake.email()))
    return cards


def print_cards(card_list):
    for i in card_list:
        print(i)


def call_person(card_list):
    for i in card_list:
        i.contact()


cards_business = create_contacts(quantity=10, is_business=True)
cards_private = create_contacts(quantity=5, is_business=False)

print_cards(cards_business)
print("--------------------------------------------------------")
print_cards(cards_private)
print("--------------------------------------------------------")
print("Wykonuję połączenie")
call_person(cards_business)
print("--------------------------------------------------------")
print("Wykonuję połączenie")
call_person(cards_private)
