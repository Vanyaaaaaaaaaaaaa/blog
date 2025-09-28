exchange_rates = {
    "EUR": 48.22000,
    "USD": 41.10000
}

uah = float(input("Введіть суму в гривнях: "))
currency = input("В яку валюту конвертувати (EUR або USD): ").upper()

if currency in exchange_rates:
    rate = exchange_rates[currency]
    result = uah / rate

    print(f"{uah:,.2f} грн = {round(result, 2):,.2f} {currency}")
else:
    print("помилка")
