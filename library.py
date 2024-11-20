import json
import os
from typing import List, Dict, Union

class Lib:
    def __init__(self, filename: str = 'books.json'):
        """
        Инициализация библиотеки с загрузкой книг из файла.

        :param filename: Имя файла для хранения книг в формате JSON.
        """
        self.filename = filename
        self.books = self.load_books()
        self.last_id = self.generate_initial_id()


    def generate_initial_id(self) -> int:
        """
        Генерация начального ID на основе существующих книг.

        :return: Начальный ID.
        """
        if self.books:
            return max(book['id'] for book in self.books) + 1
        return 1


    def load_books(self) -> List[Dict[str, Union[int, str]]]:
        """
        Загрузка книг из файла.

        :return: Список книг.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []


    def save_books(self) -> None:
        """
        Сохранение списка книг в файл.
        """
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.books, f, ensure_ascii=False, indent=4)


    def add_book(self, title: str, author: str, year: str) -> None:
        """
        Добавление новой книги в библиотеку.

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания книги.
        """
        book_id = self.last_id
        self.books.append({
            'id': book_id,
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии'
        })
        self.last_id += 1
        self.save_books()


    def remove_book(self, book_id: int) -> None:
        """
        Удаление книги из библиотеки по ID.

        :param book_id: ID книги для удаления.
        """
        for book in self.books:
            if book['id'] == book_id:
                print(f"Книга под названием {book['title']} удалена")
                self.books.remove(book)
                self.save_books()
                return
        print("Книга с таким ID не найдена.")


    def search_books(self, query: str) -> List[Dict[str, Union[int, str]]]:
        """
        Поиск книг по названию, автору или году издания.

        :param query: Запрос для поиска.
        :return: Список найденных книг.
        """
        results = [book for book in self.books if query in book['title'] or query in book['author'] or query == str(book['year'])]
        return results


    def display_books(self) -> None:
        """
        Отображение всех книг в библиотеке.
        """
        for book in self.books:
            print(f"{book['id']} - {book['title']} - {book['author']} - {book['year']} - {book['status']}")


    def update_status(self, book_id: int, status: str) -> None:
        """
        Изменение статуса книги по ID.

        :param book_id: ID книги для изменения статуса.
        :param status: Новый статус книги.
        """
        for book in self.books:
            if book['id'] == book_id:
                book['status'] = status
                self.save_books()
                return
        print("Книга с таким ID не найдена.")
