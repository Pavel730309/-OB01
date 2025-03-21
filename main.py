class Store:
    def __init__(self, name, address):
        self.name = name  # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Словарь для хранения товаров и их цен

    def add_item(self, item_name, price):
        """Добавление товара в ассортимент"""
        if price >= 0:  # Проверка на корректность цены
            self.items[item_name] = price
            print(f"Товар '{item_name}' добавлен в ассортимент.")
        else:
            print("Ошибка: цена не может быть отрицательной.")

    def remove_item(self, item_name):
        """Удаление товара из ассортимента"""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """Получение цены товара по его названию"""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновление цены товара"""
        if item_name in self.items:
            if new_price >= 0:  # Проверка на корректность новой цены
                self.items[item_name] = new_price
                print(f"Цена товара '{item_name}' обновлена до {new_price}.")
            else:
                print("Ошибка: новая цена не может быть отрицательной.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def list_items(self):
        """Вывод списка всех товаров и их цен"""
        if not self.items:
            print("Ассортимент пуст.")
        else:
            print(f"Ассортимент магазина '{self.name}':")
            for item, price in self.items.items():
                print(f"{item}: {price}")


# Создание объектов класса Store
store1 = Store(name="Магазин Уголок", address="ул. Ленина, 5")
store2 = Store(name="Глобус", address="ул. Советская, 10")
store3 = Store(name="БыстроКупи", address="ул. Мира, 7")
store4 = Store(name="Магнит", address="ул. Победы, 3")
store5 = Store(name="Перекресток", address="ул. Коммунаров, 15")

# Добавление товаров в магазины
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store1.add_item("oranges", 0.6)

store2.add_item("milk", 1.2)
store2.add_item("bread", 0.8)
store2.add_item("eggs", 0.4)

store3.add_item("chips", 1.5)
store3.add_item("soda", 1.0)
store3.add_item("cookies", 2.0)

store4.add_item("potatoes", 0.3)
store4.add_item("carrots", 0.4)
store4.add_item("cucumbers", 0.5)

store5.add_item("toilet_paper", 3.0)
store5.add_item("shampoo", 5.0)
store5.add_item("soap", 2.5)

# Тестирование методов для магазина 'Магазин Уголок'
print("\nТестирование методов для магазина 'Магазин Уголок':")

# Вывод текущего ассортимента
store1.list_items()

# Добавление нового товара
store1.add_item("grapes", 0.9)

# Обновление цены товара
store1.update_price("bananas", 0.8)

# Удаление товара
store1.remove_item("oranges")

# Получение цены товара
print(f"Цена apples: {store1.get_price('apples')}")
print(f"Цена oranges: {store1.get_price('oranges')}")  # Должно вернуть None

# Вывод обновленного ассортимента
store1.list_items()