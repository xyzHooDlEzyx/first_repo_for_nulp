from bookshelf import Book
from bookshelf import BookShop


def main():
    book1 = Book("Song of Ice and Fire", "J. Martin", 400, 200, 1000, 250)
    book2 = Book("Harry Potter", "Joanne Rowling", 400, 100, 8000, 4000)
    book3 = Book("JoJo Bizarre Adventures", "H. Araki", 900, 300, 10000, 8000)

    bookshop = BookShop()
    bookshop.add_book(book1)
    bookshop.add_book(book2)
    bookshop.add_book(book3)

    top_price_books = bookshop.top_books_by_price(2)
    top_sales_books = bookshop.top_books_by_sales(2)

    print("\nTop books by price:")
    for book in top_price_books:
        print(book)
    print("\nTop books by sales:")
    for book in top_sales_books:
        print(book)

    bookshop.del_book(book1)


# bookshop.del_book(book1)


if __name__ == '__main__':
    main()
