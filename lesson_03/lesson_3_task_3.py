from address import Address
from mailing import Mailing

to_address = Address(
    "123456", "Москва", "Ленина", "10", "25"
)

from_address = Address(
    "654321", "Казань", "Пушкина", "5", "12"
)

my_mailing = Mailing(
    to_address, from_address, 500, "RU123456789"
)

print(
    f"Отправление {my_mailing.track} "
    f"из {my_mailing.from_address.index}, "
    f"{my_mailing.from_address.city}, "
    f"{my_mailing.from_address.street}, "
    f"{my_mailing.from_address.house} - "
    f"{my_mailing.from_address.apartment} "
    f"в {my_mailing.to_address.index}, "
    f"{my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, "
    f"{my_mailing.to_address.house} - "
    f"{my_mailing.to_address.apartment}. "
    f"Стоимость {my_mailing.cost} рублей."
)
