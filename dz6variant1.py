class Book:
    """Класс для представления книги."""

    def __init__(self, title: str = "NA", author: str = "NA", pages: int = 1) -> None:
        """Инициализация/конструктор класса.

        Args:
            title: Название книги.
            author: Автор книги.
            pages: Количество страниц.
        """

        self._title = title
        self._author = author
        self.set_pages(pages)

    def get_title(self) -> str:
        """Геттер для названия книги.

        Returns:
            title: Название книги.
        """

        return self._title

    def get_author(self) -> str:
        """Геттер для автора книги.

        Returns:
            author: Автор книги.
        """

        return self._author

    def get_pages(self) -> int:
        """Геттер для количества страниц.

        Returns:
            pages: Количество страниц.
        """

        return self._pages

    def set_title(self, title: str) -> None:
        """Сеттер для названия книги.

        Args:
            title: Название книги.
        """

        self._title = title

    def set_author(self, author: str) -> None:
        """Сеттер для автора книги.

        Args:
            author: Автор книги.
        """

        self._author = author

    def set_pages(self, pages: int) -> None:
        """Сеттер для количества страниц.

        Args:
            pages: Количество страниц.
        """

        if pages <= 0:
            print("Количество страниц должно быть больше 0")
        else:
            self._pages = pages

    def info(self) -> None:
        """Вывод информации о книге."""

        print(f"Название: {self._title}")
        print(f"Автор: {self._author}")
        print(f"Количество страниц: {self._pages}")

    def is_short_book(self) -> bool:
        """Проверка, является ли книга короткой.

        Returns:
            True если книга короче 100 страниц, иначе False.
        """

        return self._pages < 100

    def get_days_of_reading(self, pages_per_day: int) -> str:
        """Расчет количества дней для прочтения книги.

        Args:
            pages_per_day: Скорость чтения (страниц в день).

        Returns:
            Строка с информацией о количестве дней.
        """

        days = max(1, round(self._pages / pages_per_day))
        return f"Книгу можно прочитать за {days} дней"


class Actions:
    """Класс для управления коллекцией книг."""

    books = []

    def add_book(self) -> None:
        """Добавление новой книги в коллекцию."""

        print("\n--- Добавление новой книги ---")
        title = input("Введите название: ")
        author = input("Введите автора: ")

        pages_input = True
        while pages_input:
            try:
                pages = int(input("Введите количество страниц: "))
                if pages <= 0:
                    print("Количество страниц должно быть больше 0")
                else:
                    book = Book(title, author, pages)
                    self.books.append(book)
                    print("Книга добавлена")
                    pages_input = False
            except ValueError:
                print("Введите целое число")

    def show_all_books(self) -> None:
        """Отображение всех книг в коллекции."""

        print("\n--- Все книги ---")
        if not self.books:
            print("Список книг пуст.")
            return

        for i in range(len(self.books)):
            book = self.books[i]
            print(f"{i + 1}. '{book.get_title()}'")

    def find_short_book(self) -> None:
        """Поиск и отображение коротких книг."""

        print("\n--- Короткие книги (короче 100 страниц) ---")
        short_books = [book for book in self.books if book.is_short_book()]

        if not short_books:
            print("Короткие книги не найдены.")
            return

        for i in range(len(short_books)):
            book = short_books[i]
            print(f"{i + 1}. '{book.get_title()}' - {book.get_author()} ({book.get_pages()} стр.)")

    def days_of_reading(self) -> None:
        """Расчет дней чтения для выбранной книги."""

        self.show_all_books()
        if not self.books:
            return

        index_input = True
        while index_input:
            try:
                index = int(input("Введите номер книги: ")) - 1
                index_input = False
            except ValueError:
                print("Введите целое число")

        if 0 <= index < len(self.books):
            speed_input = True
            while speed_input:
                try:
                    speed = int(input("Введите скорость чтения (страниц в день): "))
                    speed_input = False
                except ValueError:
                    print("Введите целое число")
            print(self.books[index].get_days_of_reading(speed))
        else:
            print("Такой книги нет.")

    def show_info(self) -> None:
        """Отображение информации о выбранной книге."""

        self.show_all_books()
        if not self.books:
            return

        index_input = True
        while index_input:
            try:
                index = int(input("Введите номер книги для просмотра информации: ")) - 1
                index_input = False
            except ValueError:
                print("Введите целое число")

        if 0 <= index < len(self.books):
            print("\n--- Информация о книге ---")
            self.books[index].info()
        else:
            print("Такой книги нет.")

    def run_menu(self) -> None:
        """Запуск меню управления книгами."""

        is_running = True

        while is_running:
            print("\n--- Меню управления книгами ---")
            print("1. Добавить книгу")
            print("2. Показать все книги")
            print("3. Показать информацию о книге")
            print("4. Найти короткие книги")
            print("5. Посчитать дни чтения")
            print("6. Вернуться в главное меню")

            choice_input = True
            while choice_input:
                try:
                    choice = int(input("Выберите действие (1-6): "))
                    choice_input = False
                except ValueError:
                    print("Введите целое число")

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
                    is_running = False
                case _:
                    print("Некорректный выбор.")


class Main:
    """Главный класс приложения."""

    book_actions = Actions()

    def run(self) -> None:
        """Запуск главного меню приложения."""

        is_running = True

        while is_running:
            print("\n=== Главное меню ===")
            print("1. Управление книгами")
            print("2. Завершение программы")

            choice_input = True
            while choice_input:
                try:
                    choice = int(input("Выберите действие (1-2): "))
                    choice_input = False
                except ValueError:
                    print("Введите целое число")

            match choice:
                case 1:
                    self.book_actions.run_menu()
                case 2:
                    print("Программа завершена")
                    is_running = False
                case _:
                    print("Некорректный выбор.")


Main().run()
