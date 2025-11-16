class Book:
    def __init__(self, title = "", author = "", pages = 1):
        self._title = title
        self._author = author
        self.set_pages(pages)

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_pages(self):
        return self._pages

    def set_title(self, title):
        self._title = title

    def set_author(self, author):
        self._author = author

    def set_pages(self, pages):
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self._pages = pages

    def info(self):
        print(f"Название: {self._title}")
        print(f"Автор: {self._author}")
        print(f"Количество страниц: {self._pages}")

    def is_short_book(self):
        return self._pages < 100

    def get_days_of_reading(self, pages_per_day):
        days = max(1, round(self._pages / pages_per_day))
        return f"Книгу можно прочитать за {days} дней"


class Actions:
    def __init__(self):
        self.books = []

    def add_book(self):
        print("\n--- Добавление новой книги ---")
        title = input("Введите название: ")
        author = input("Введите автора: ")

        pages = int(input("Введите количество страниц: "))

        book = Book(title, author, pages)
        self.books.append(book)
        print("Книга добавлена")

    def show_all_books(self):
        print("\n--- Все книги ---")
        if not self.books:
            print("Список книг пуст.")
            return

        for i in range(len(self.books)):
            book = self.books[i]
            print(f"{i + 1}. '{book.get_title()}'")

    def find_short_book(self):
        print("\n--- Короткие книги (короче 100 страниц) ---")
        short_books = [book for book in self.books if book.is_short_book()]

        if not short_books:
            print("Короткие книги не найдены.")
            return

        for i in range(len(short_books)):
            book = short_books[i]
            print(f"{i + 1}. '{book.get_title()}' - {book.get_author()} ({book.get_pages()} стр.)")

    def days_of_reading(self):
        self.show_all_books()
        if not self.books:
            return

        index = int(input("Введите номер книги: ")) - 1
        if 0 <= index < len(self.books):
            speed = int(input("Введите скорость чтения (страниц в день): "))
            print(self.books[index].get_days_of_reading(speed))
        else:
            print("Такой книги нет.")

    def show_info(self):
        self.show_all_books()
        if not self.books:
            return

        index = int(input("Введите номер книги для просмотра информации: ")) - 1
        if 0 <= index < len(self.books):
            print("\n--- Информация о книге ---")
            self.books[index].info()
        else:
            print("Такой книги нет.")

    def run_menu(self):
        while True:
            print("\n--- Меню управления книгами ---")
            print("1. Добавить книгу")
            print("2. Показать все книги")
            print("3. Показать информацию о книге")
            print("4. Найти короткие книги")
            print("5. Посчитать дни чтения")
            print("6. Вернуться в главное меню")

            choice = int(input("Выберите действие (1-6): "))

            match choice:
                case 1:
                    self.add_book()
                case 2:
                    self.show_all_books()
                case 3:
                    self.show_info()
                case 4:
                    self.find_short_book()
                case 5:
                    self.days_of_reading()
                case 6:
                    break
                case _:
                    print("Некорректный выбор.")


class Main:
    def __init__(self):
        self.book_actions = Actions()

    def demonstrate(self):
        print("\n=== Демонстрация работы класса Book ===")

        print("\n1. Создание экземпляров:")

        book1 = Book()
        print("Создана книга через конструктор без параметров")

        book2 = Book("Норвежский лес", "Харуки Мураками", 368)
        print("Создана книга через конструктор с параметрами")

        print("\n2. Работа с сеттерами:")
        book1.set_title("Обыкновенная история")
        book1.set_author("И.А. Гончаров")
        book1.set_pages(416)
        print("Установлены значения через сеттеры")

        print("\n3. Работа с геттерами:")
        print(f"Название = {book1.get_title()}")
        print(f"Автор = {book1.get_author()}")
        print(f"Страниц = {book1.get_pages()}")

        print("\n4. Метод info():")
        book1.info()

        print("\n5. Дополнительные методы:")
        print(f"Длинная книга: {book1.is_short_book()}")
        print(f"Длинная книга: {book2.is_short_book()}")
        print(book1.get_days_of_reading(50))
        print(book2.get_days_of_reading(30))

        self.book_actions.books.extend([book1, book2])

    def run(self):
        while True:
            print("\n=== Главное меню ===")
            print("1. Демонстрация работы класса Book")
            print("2. Управление книгами")
            print("3. Завершение программы")

            choice = int(input("Выберите действие (1-3): "))

            match choice:
                case 1:
                    self.demonstrate()
                case 2:
                    self.book_actions.run_menu()
                case 3:
                    print("Программа завершена")
                    break
                case _:
                    print("Некорректный выбор.")


Main().run()