from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79001111111"),
    Smartphone("Samsung", "Galaxy S24", "+79002222222"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79003333333"),
    Smartphone("Huawei", "Pura 70", "+79004444444"),
    Smartphone("Google", "Pixel 9", "+79005555555")
]

for phone in catalog:
    print(
        f"{phone.brand} - {phone.model}. "
        f"{phone.phone_number}"
    )
