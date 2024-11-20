from library import Lib

def main() -> None:
    """
    Главная функция для управления библиотекой.
    """
    library = Lib()

    while True:
        print("===========================")
        print("Меню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        print("===========================")

        choice = int(input("Выберите действие: "))

        match choice:  
            case 1:
                title = input("\nВведите название книги: ")
                author = input("Введите автора книги: ")
                year = input("Введите год издания: ")
                library.add_book(title, author, year)

            case 2:
                book_id = int(input("\nВведите ID книги для удаления: "))
                library.remove_book(book_id)
            
            case 3:
                query = input("\nВведите название, автора или год для поиска: ")
                results = library.search_books(query)
                if results:
                    for book in results:
                        print(f"{book['id']} - {book['title']} - {book['author']} - {book['year']} - {book['status']}")
                else:
                    print("Книги не найдены.")

            case 4:
                library.display_books()

            case 5:
                book_id = int(input("\nВведите ID книги для изменения статуса: "))
                status = input("Введите новый статус (в наличии/выдана): ")
                library.update_status(book_id, status)

            case 6:
                break

            case _:
                print("\nНеверный выбор, попробуйте снова.")

while main:
    main()