import requests

API_KEY = "d469c02f080f4fa99337d62c14522fc7"  # Ваш API ключ від OpenWeatherMap
BASE_URL = "https://api.weatherbit.io/v2.0/current"

def get_weather(city):
    """Отримує погодні умови для міста через OpenWeatherMap API."""
    try:
        # Параметри запиту
        params = {
            "lat": 50.4501,  # Широта для Києва
            "lon": 30.5236,   # Довгота для Києва
            "key": API_KEY,
            "lang": "uk"
        }
        
        # Запит до API
        response = requests.get(BASE_URL, params=params)
        
        # Перевіряємо статус запиту
        if response.status_code == 200:
            data = response.json()
            description = data["weather"][0]["description"]  # Опис погоди
            temperature = data["main"]["temp"]  # Температура
            return f"{description.capitalize()}, {temperature}°C"
        else:
            return "Неможливо отримати погоду"
    except Exception as e:
        print(f"Помилка при отриманні погодних умов: {e}")
        return "Помилка погоди"


def show_flights(flights):
    """Виводить усі рейси."""
    if not flights:
        print("Список рейсів порожній.")
        return
    print("\nСписок рейсів:")
    for flight in flights:
        print(f"{flight['номер']} | {flight['місто']} | {flight['час']} | {flight['статус']} | {flight['погода']}")
    print()                                                                                                                                          

def add_flight(flights):
    номер = input("Введіть номер рейсу: ")
    місто = input("Введіть місто призначення: ")
    час = input("Введіть час вильоту (HH:MM): ")
    статус = input("Введіть статус рейсу (Вчасно/Затримано/Скасовано): ")
    погода = get_weather(місто)
    flights.append({"номер": номер, "місто": місто, "час": час, "статус": статус, "погода": погода})
    print("Рейс додано успішно.\n")

def delete_flight(flights):
    """Видаляє рейс за номером."""
    номер = input("Введіть номер рейсу, який потрібно видалити: ")
    for flight in flights:
        if flight["номер"] == номер:
            flights.remove(flight)
            print("Рейс видалено.\n")
            return
    print("Рейс із таким номером не знайдено.\n")

def search_flights_by_city(flights):
    """Шукає рейси за містом."""
    місто = input("Введіть місто для пошуку: ")
    results = [flight for flight in flights if flight["місто"].lower() == місто.lower()]
    if results:
        print("\nЗнайдені рейси:")
        show_flights(results)
    else:
        print("Рейсів до цього міста не знайдено.\n")

def update_flight_status(flights):
    """Оновлює статус рейсу."""
    номер = input("Введіть номер рейсу для оновлення статусу: ")
    for flight in flights:
        if flight["номер"] == номер:
            новий_статус = input("Введіть новий статус (Вчасно/Затримано/Скасовано): ")
            flight["статус"] = новий_статус
            print("Статус оновлено.\n")
            return
    print("Рейс із таким номером не знайдено.\n")

def update_weather(flights):
    """Оновлює погодні умови для всіх рейсів."""
    for flight in flights:
        flight["погода"] = get_weather(flight["місто"])
    print("Погода оновлена для всіх рейсів.\n")

def main():
    flights = []
    print("=== Меню ===")
    options = ["Показати всі рейси", "Додати рейс", "Видалити рейс", "Пошук рейсів за містом", "Оновити статус рейсу", "Оновити погодні умови", "Вихід"]
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")
    while True:
        choice = int(input("Оберіть дію (1-6): "))
        if choice == 1:
            show_flights(flights)
        elif choice == 2:
            add_flight(flights)
        elif choice == 3:
            delete_flight(flights)
        elif choice == 4:
            search_flights_by_city(flights)
        elif choice == 5:
            update_flight_status(flights)
        elif choice == 6:
            update_weather(flights)
        elif choice == 7:
            print("Вы вышли из програмы.")
            break
        else:
            print("Неправильный выбор.")

main()